import sys
import csv
from PyQt6.QtWidgets import QApplication, QComboBox, QMessageBox, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFormLayout, QGroupBox

class VentanaPagos(QMainWindow):
    def __init__(self, numero_reserva):
        super().__init__()

        self.setWindowTitle("Ventana de Pagos")
        self.setGeometry(100, 100, 500, 200)

        self.numero_reserva = numero_reserva
        
        # Etiquetas
        self.total_label = QLabel()  # Etiqueta para mostrar el total a pagar
        self.total_label.setText(f"Total a pagar: ${self.calcular_total_pagar()}")
        self.nombre_label = QLabel("Nombre:")
        self.apellido_label = QLabel("Apellido:")
        self.rut_label = QLabel("Rut:")
        self.tipo_pago_label = QLabel("Forma de pago:")
        self.nro_tarjeta_label = QLabel("Número de tarjeta:")
        self.cvc_label = QLabel("CVC:")

        # Campos de entrada de texto
        self.nombre_lineedit = QLineEdit()
        self.apellido_lineedit = QLineEdit()
        self.rut_lineedit = QLineEdit()
        self.nro_tarjeta_lineedit = QLineEdit()
        self.cvc_lineedit = QLineEdit()

        # ComboBox
        self.tipo_pago_combobox = QComboBox()
        self.tipo_pago_combobox.addItem("Débito")
        self.tipo_pago_combobox.addItem("Crédito")

        # Botones
        #self.volver_button = QPushButton("Volver")
        self.pago_boton = QPushButton("Realizar Pago")
        self.pago_boton.clicked.connect(self.realizar_pago)

        # Grupo para la columna izquierda
        group_izquierda = QGroupBox()
        layout_derecho = QFormLayout()
        layout_derecho.addRow(self.nombre_label, self.nombre_lineedit)
        layout_derecho.addRow(self.apellido_label, self.apellido_lineedit)
        layout_derecho.addRow(self.rut_label, self.rut_lineedit)
        group_izquierda.setLayout(layout_derecho)

        # Grupo para la columna derecha
        derecha_grupo = QGroupBox()
        layout_izquierda = QFormLayout()
        layout_izquierda.addRow(self.tipo_pago_label, self.tipo_pago_combobox)
        layout_izquierda.addRow(self.nro_tarjeta_label, self.nro_tarjeta_lineedit)
        layout_izquierda.addRow(self.cvc_label, self.cvc_lineedit)
        derecha_grupo.setLayout(layout_izquierda)

        # QHBoxLayout para combinar los grupos izquierdo y derecho
        layout_principal = QHBoxLayout()
        layout_principal.addWidget(group_izquierda)
        layout_principal.addWidget(derecha_grupo)

        # QHBoxLayout para los botones inferiores
        botones_layout = QHBoxLayout()
        #botones_layout.addWidget(self.volver_button)
        botones_layout.addWidget(self.pago_boton)

        # QVBoxLayout para combinar el diseño principal con los botones inferiores
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.total_label)
        layout_vertical.addLayout(layout_principal)
        layout_vertical.addLayout(botones_layout)

        # Widget contenedor y establecer el diseño principal
        widget = QWidget()
        widget.setLayout(layout_vertical)
        self.setCentralWidget(widget)

    def calcular_total_pagar(self):
        with open("Dataset/acompañantes.csv", "r", encoding="iso-8859-1") as file:
            reader = csv.reader(file)
            conteo_acompañantes = sum(1 for row in reader if row[0] == self.numero_reserva)
        print("conteo_acompañantes:", conteo_acompañantes)

        with open("Dataset/tipoexcursion.csv", "r", encoding="iso-8859-1") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.numero_reserva:
                    tipo_excursion = row[1]
                    break
        print("tipo_excursion:", tipo_excursion)

        monto_pagar = 0
        if tipo_excursion == "Excursion Light":
            monto_pagar = (conteo_acompañantes + 1) * 5000
        elif tipo_excursion == "Excursion Plus":
            monto_pagar = (conteo_acompañantes + 1) * 25000
        elif tipo_excursion == "Excursion Heavy":
            monto_pagar = (conteo_acompañantes + 1) * 50000
        print("monto_pagar:", monto_pagar)

        return monto_pagar

    def realizar_pago(self):
        nombre = self.nombre_lineedit.text()
        apellido = self.apellido_lineedit.text()
        rut_cliente = self.rut_lineedit.text()
        forma_pago = self.tipo_pago_combobox.currentText()
        numero_tarjeta = self.nro_tarjeta_lineedit.text()
        cvc = self.cvc_lineedit.text()

        if not (nombre and apellido and rut_cliente and numero_tarjeta and cvc):
            QMessageBox.warning(self, "Advertencia", "Debe rellenar todos los campos.")
            return

        respuesta = QMessageBox.question(
            self,
            "Verificación",
            "Verifique que todos sus datos estén correctos antes de realizar el pago.",
            QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Yes,
        )

        if respuesta == QMessageBox.StandardButton.Yes:
            datos_pago = [
                self.calcular_total_pagar(),
                nombre,
                apellido,
                rut_cliente,
                forma_pago,
                numero_tarjeta,
                cvc
            ]

            with open("Dataset/registrodepagos.csv", "a", encoding="utf-8-sig", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(datos_pago)

            QMessageBox.information(self, "Confirmación", "El pago ha sido confirmado y la reserva se ha realizado con éxito.")
            respuesta_final = QMessageBox.question(
                self,
                "Volver al inicio",
                "¿Desea volver al inicio?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Close,
            )

            if respuesta_final == QMessageBox.StandardButton.Yes:
                from FormulariodeReserva import Reserva
                self.ventana_reserva = Reserva()
                self.ventana_reserva.show()
                self.hide()

            else:
                self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaPagos()
    window.show()
    sys.exit(app.exec())
