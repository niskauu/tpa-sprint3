import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFormLayout, QGroupBox, QHBoxLayout, QMessageBox, QDateEdit

class VentanaAcompanantes(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Agregar Acompañantes")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.groupBox = QGroupBox("Datos del Acompañante")
        self.formLayout = QFormLayout()

        self.nombreLineEdit = QLineEdit()
        self.apellidoLineEdit = QLineEdit()
        self.rutLineEdit = QLineEdit()
        self.fechaNacimientoDateEdit = QDateEdit()
        self.telefonoLineEdit = QLineEdit()
        self.emailLineEdit = QLineEdit()

        self.formLayout.addRow(QLabel("Nombre:"), self.nombreLineEdit)
        self.formLayout.addRow(QLabel("Apellido:"), self.apellidoLineEdit)
        self.formLayout.addRow(QLabel("RUT:"), self.rutLineEdit)
        self.formLayout.addRow(QLabel("Fecha de Nacimiento:"), self.fechaNacimientoDateEdit)
        self.formLayout.addRow(QLabel("Teléfono:"), self.telefonoLineEdit)
        self.formLayout.addRow(QLabel("E-mail:"), self.emailLineEdit)

        self.groupBox.setLayout(self.formLayout)
        self.layout.addWidget(self.groupBox)

        self.agregarAcompananteButton = QPushButton("Agregar Acompañante")
        self.agregarAcompananteButton.clicked.connect(self.agregar_acompanante)
        self.layout.addWidget(self.agregarAcompananteButton)

    def agregar_acompanante(self):
        nombre = self.nombreLineEdit.text()
        apellido = self.apellidoLineEdit.text()
        rut = self.rutLineEdit.text()
        fecha_nacimiento = self.fechaNacimientoDateEdit.date().toString("yyyy-MM-dd")
        telefono = self.telefonoLineEdit.text()
        email = self.emailLineEdit.text()

        # Aqui supongo q hay hacer la cosa pa q se guarden en un csv idk

        QMessageBox.information(self, "Éxito", "Acompañante agregado correctamente.")

        # Pa limpiar los campos 
        self.nombreLineEdit.clear()
        self.apellidoLineEdit.clear()
        self.rutLineEdit.clear()
        self.telefonoLineEdit.clear()
        self.emailLineEdit.clear()

        self.nombreLineEdit.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaAcompanantes()
    ventana.show()
    sys.exit(app.exec())
