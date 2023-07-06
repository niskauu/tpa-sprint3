import sys
from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFormLayout, QGroupBox


class VentanaPagos(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ventana de Pagos")
        self.setGeometry(100, 100, 500, 200)
        
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

        # Botones
        self.volver_button = QPushButton("Volver")
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
        botones_layout.addWidget(self.volver_button)
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
