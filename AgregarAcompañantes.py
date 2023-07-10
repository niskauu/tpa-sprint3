import sys
from PyQt6.QtWidgets import QApplication, QDateEdit, QMessageBox, QComboBox, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFormLayout, QGroupBox
import os

class VentanaAcompanante(QMainWindow):
    def __init__(self,nro_reserva):
        super().__init__()
        self.nro_acompanantes=0
        self.nro_reserva = nro_reserva

        self.setWindowTitle("Ventana de Acompañantes")
        self.setGeometry(100, 100, 500, 200)

        # Etiquetas
        self.texto_label = QLabel("A continuación ingrese los datos del o la acompañante:") 
        self.nombre_label = QLabel("Nombre:")
        self.apellido_label = QLabel("Apellido:")
        self.rut_label = QLabel("Rut:")
        self.nacimiento_label = QLabel("Fecha de Nacimiento:")
        self.telefono_label = QLabel("Telefono:")
        self.nro_emer_label = QLabel("Número de Emergencia:")

        # Campos de entrada de texto
        self.nombre_lineedit = QLineEdit()
        self.apellido_lineedit = QLineEdit()
        self.rut_lineedit = QLineEdit()
        self.nacimiento_dateedit = QDateEdit()
        self.telefono_lineedit = QLineEdit()
        self.nro_emer_lineedit = QLineEdit()

        # Botones
        self.boton_continuar = QPushButton("Continuar")
        self.boton_continuar.clicked.connect(self.seguro)
        self.agregar_boton = QPushButton("Agregar Acompañante")
        self.agregar_boton.clicked.connect(self.agregar_acompanante)

        # Grupo para la columna izquierda
        grupo_izquierda = QGroupBox()
        izquierda_layout = QFormLayout()
        izquierda_layout.addRow(self.nombre_label, self.nombre_lineedit)
        izquierda_layout.addRow(self.apellido_label, self.apellido_lineedit)
        izquierda_layout.addRow(self.rut_label, self.rut_lineedit)
        grupo_izquierda.setLayout(izquierda_layout)

        # Grupo para la columna derecha
        grupo_derecha = QGroupBox()
        derecha_layout = QFormLayout()
        derecha_layout.addRow(self.nacimiento_label, self.nacimiento_dateedit)
        derecha_layout.addRow(self.telefono_label, self.telefono_lineedit)
        derecha_layout.addRow(self.nro_emer_label, self.nro_emer_lineedit)
        grupo_derecha.setLayout(derecha_layout)

        # QHBoxLayout para combinar los grupos izquierdo y derecho
        layout_principal = QHBoxLayout()
        layout_principal.addWidget(grupo_izquierda)
        layout_principal.addWidget(grupo_derecha)

        # QHBoxLayout para los botones inferiores
        layout_botones = QHBoxLayout()
        layout_botones.addWidget(self.boton_continuar)
        layout_botones.addWidget(self.agregar_boton)

        # QVBoxLayout para combinar el diseño principal con los botones inferiores
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.texto_label)
        layout_vertical.addLayout(layout_principal)
        layout_vertical.addLayout(layout_botones)

        # Widget contenedor y establecer el diseño principal
        widget = QWidget()
        widget.setLayout(layout_vertical)
        self.setCentralWidget(widget)

    def agregar_acompanante(self):
        nombre = self.nombre_lineedit.text()
        apellido = self.apellido_lineedit.text()
        rut = self.rut_lineedit.text()
        fecha_nacimiento = self.nacimiento_dateedit.date().toString("dd-MM-yyyy")
        telefono = self.telefono_lineedit.text()
        nro_emer = self.nro_emer_lineedit.text()

        if nombre and apellido and rut and fecha_nacimiento and telefono and nro_emer:
            self.nro_acompanantes =+1
            archivo = open(f"{os.path.dirname(__file__)}/Dataset/reserva.csv", "a")
            datos = f"{self.nro_reserva},{nombre},{apellido},{rut},{fecha_nacimiento},{telefono},{nro_emer}"
            archivo.write(datos)
            archivo.close()

            QMessageBox.information(self, "Éxito", "Acompañante agregado correctamente.")
            # para limpiar los campos
            self.nombre_lineedit.clear()
            self.apellido_lineedit.clear()
            self.rut_lineedit.clear()
            self.nacimiento_dateedit.clear()
            self.telefono_lineedit.clear()
            self.nro_emer_lineedit.clear()

            self.nombre_lineedit.setFocus()
        
        else:
            QMessageBox.warning(self,"Error", "No puede dejar campos vacios", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)

    def seguro(self):
        consulta = QMessageBox.information(self, "Pregunta", "¿Desea continuar? No podrá agregar más acompañantes", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if consulta == QMessageBox.StandardButton.Yes:
            self.abrir_ventana_excursion()
        elif consulta == QMessageBox.StandardButton.No:
            return

    def abrir_ventana_excursion(self):
        from TipodeExcursion import VentanaExcursion
        self.ventana_excursion = VentanaExcursion(self.nro_reserva, self.nro_acompanantes)
        self.ventana_excursion.show()
        self.hide()

'''if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaAcompanante()
    window.show()
    sys.exit(app.exec())'''