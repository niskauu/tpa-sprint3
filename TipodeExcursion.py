from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QRadioButton, QPushButton, QTextEdit, QGroupBox, QButtonGroup
from PyQt6.QtGui import QPixmap
import sys
import csv
import codecs
import io

class VentanaExcursion(QMainWindow):
    def __init__(self, numero_reserva):
        super().__init__()
        self.numero_reserva = numero_reserva

        self.setWindowTitle("Selección de Excursión")
        self.setGeometry(100, 100, 800, 500)

        contenedor_principal = QVBoxLayout()

        layout_horizontal = QHBoxLayout()

        self.grupo_botones = QButtonGroup() 

        # Excursión Light
        light_box = QGroupBox("Opción 1:")
        light_layout = QVBoxLayout()

        light_radio = QRadioButton("Excursion Light")
        light_layout.addWidget(light_radio)
        self.grupo_botones.addButton(light_radio)

        light_imagen = QLabel()
        light_pixmap = QPixmap("images/excursion_light.png")
        light_imagen.setPixmap(light_pixmap)
        light_imagen.setScaledContents(True)
        light_imagen.setFixedSize(250, 150)
        light_layout.addWidget(light_imagen)

        light_precio = QLabel("Su valor es de $10.000 por persona.")
        light_desc = QTextEdit()
        light_desc.setPlainText(
            '''Corresponde a una excursión de tipo caminata de 6 horas en total por senderos de complejidad baja con hermosos lugares de vegetación nativa y afluentes de agua, ideal para grupos familiares con niños o personas de 3ra edad.'''
        )
        light_desc.setReadOnly(True)
        light_layout.addWidget(light_precio)
        light_layout.addWidget(light_desc)

        light_box.setLayout(light_layout)
        layout_horizontal.addWidget(light_box)

        # Excursión Plus
        plus_box = QGroupBox("Opción 2:")
        plus_layout = QVBoxLayout()

        plus_radio = QRadioButton("Excursion Plus")
        plus_layout.addWidget(plus_radio)
        self.grupo_botones.addButton(plus_radio)

        plus_imagen = QLabel()
        plus_pixmap = QPixmap("images/excursion_plus.png")
        plus_imagen.setPixmap(plus_pixmap)
        plus_imagen.setScaledContents(True)
        plus_imagen.setFixedSize(250, 150)
        plus_layout.addWidget(plus_imagen)

        plus_precio = QLabel("Su valor es de $50.000 por persona.")
        plus_desc = QTextEdit()
        plus_desc.setPlainText(
            '''Corresponde a una excursión de tipo hiking de 3 días en total por una cadena montañosa, experiencia de campamento y contemplación de glaciares y cascadas, ideal para grupos de personas con capacidades físicas compatibles con la exigencia de la caminata.'''
        )
        plus_desc.setReadOnly(True)
        plus_layout.addWidget(plus_precio)
        plus_layout.addWidget(plus_desc)

        plus_box.setLayout(plus_layout)
        layout_horizontal.addWidget(plus_box)

        # Excursión Heavy
        heavy_box = QGroupBox("Opción 3:")
        heavy_layout = QVBoxLayout()

        heavy_radio = QRadioButton("Excursion Heavy")
        heavy_layout.addWidget(heavy_radio)
        self.grupo_botones.addButton(heavy_radio)

        heavy_imagen = QLabel()
        heavy_pixmap = QPixmap("images/excursion_heavy.png")
        heavy_imagen.setPixmap(heavy_pixmap)
        heavy_imagen.setScaledContents(True)
        heavy_imagen.setFixedSize(250, 150)
        heavy_layout.addWidget(heavy_imagen)

        heavy_precio = QLabel("Su valor es de $100.000 por persona.")
        heavy_desc = QTextEdit()
        heavy_desc.setPlainText(
            '''Corresponde a una excursión de tipo hiking de 5 días en total por una cadena montañosa y con navegación en afluentes locales. 
Se incluyen actividades extremas de Rapel, Canopi, Rafting y Escalada.
Las actividades requieren de capacidades físicas compatibles con la complejidad de la excursión.'''
        )
        heavy_desc.setReadOnly(True)
        heavy_layout.addWidget(heavy_precio)
        heavy_layout.addWidget(heavy_desc)

        heavy_box.setLayout(heavy_layout)
        layout_horizontal.addWidget(heavy_box)

        contenedor_principal.addLayout(layout_horizontal)  # Agregar layout en el contenedor principal

        botones_layout = QHBoxLayout()

        volver_boton = QPushButton("Volver")
        botones_layout.addWidget(volver_boton)

        continuar_button = QPushButton("Continuar")
        botones_layout.addWidget(continuar_button)

        # Agregar el layout de los botones al contenedor principal
        contenedor_principal.addLayout(botones_layout)

        widget = QWidget()
        widget.setLayout(contenedor_principal)  # Establecer el contenedor principal como diseño

        self.setCentralWidget(widget)

        continuar_button.clicked.connect(self.continuar_clicked)
        volver_boton.clicked.connect(self.volver_clicked)

    def continuar_clicked(self):
        from RecepcionDocumentos import Documentos
        from VentanadePago import VentanaPagos
        opcion_excursion = self.grupo_botones.checkedButton()

        if opcion_excursion is not None:
            tipo_excursion = opcion_excursion.text()

            # Convertir el texto al formato adecuado
            tipo_excursion = tipo_excursion.encode("utf-8").decode("utf-8")

            # Save data to CSV file
            data = [self.numero_reserva, tipo_excursion]
            with io.open("Dataset/tipoexcursion.csv", "a", encoding="utf-8-sig", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)

            if opcion_excursion.text() == "Excursion Plus" or opcion_excursion.text() == "Excursion Heavy":
                respuesta = QMessageBox.question(
                    self, 
                    "Advertencia", 
                    "Para estas excursiones debe poseer:\n1.- Constancia médica\n2.- Declaración jurada\n3.- Anexos (electrocardiogramas, radiografías y/o tomografías).\n¿Desea continuar?", 
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )
                if respuesta == QMessageBox.StandardButton.Yes:
                    self.ventana_documentos = Documentos(self.numero_reserva)
                    self.ventana_documentos.show()
                    self.hide()
            elif opcion_excursion.text() == "Excursion Light":
                respuesta = QMessageBox.question(
                    self, 
                    "Advertencia", 
                    "Para realizar la reserva debe abonar un 50% del valor total. ¿Desea continuar?", 
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )

                if respuesta == QMessageBox.StandardButton.Yes:
                    self.ventana_pagos = VentanaPagos(self.numero_reserva)
                    self.ventana_pagos.show()
                    self.hide()
        else:
            QMessageBox.warning(
                self,
                "Advertencia",
                "Antes de continuar debe seleccionar una excursión",
                QMessageBox.StandardButton.Ok,
            )

    def volver_clicked(self):
        from FormulariodeReserva import Reserva
        self.ventana_reserva = Reserva()
        self.ventana_reserva.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaExcursion()
    ventana.show()
    sys.exit(app.exec())
