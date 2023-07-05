import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QFormLayout, QWidget, QComboBox


class VentanaPagos(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ventana de Pagos")

        # Etiquetas
        self.total_label = QLabel("Total a pagar: $100")  # hay que hacer que muestre el valor que corresponde
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

        # Botón
        self.pago_button = QPushButton("Realizar Pago")
        self.pago_button.clicked.connect(self.realizar_pago)

        # Diseño del formulario
        layout = QFormLayout()
        layout.addRow(self.total_label)
        layout.addRow(self.nombre_label, self.nombre_lineedit)
        layout.addRow(self.apellido_label, self.apellido_lineedit)
        layout.addRow(self.rut_label, self.rut_lineedit)
        layout.addRow(self.tipo_pago_label, self.tipo_pago_combobox)
        layout.addRow(self.nro_tarjeta_label, self.nro_tarjeta_lineedit)
        layout.addRow(self.cvc_label, self.cvc_lineedit)
        layout.addRow(self.pago_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def realizar_pago(self):
        nombre = self.nombre_lineedit.text()
        apellido = self.apellido_lineedit.text()
        id_cliente = self.rut_lineedit.text()
        forma_pago = self.tipo_pago_combobox.currentText()
        numero_tarjeta = self.nro_tarjeta_lineedit.text()
        cvc = self.cvc_lineedit.text()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaPagos()
    window.show()
    sys.exit(app.exec())

