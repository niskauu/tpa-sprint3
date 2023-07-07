import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox, QLabel
from PyQt6.QtGui import QFont

class IniciarSesion(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciarUI()

    def iniciarUI(self):
        self.setFixedSize(400, 200)
        self.setWindowTitle("Inicio de Sesion")
        self.iniciar_sesion()
        self.show()

    def iniciar_sesion(self):
        self.estaloggeado = False

        titulo = QLabel()
        titulo.setText("Inicio De Sesion")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        titulo.setFont(font)

        correo_label = QLabel()
        correo_label.setText("Correo: ")

        self.correo_input = QLineEdit()

        contrasenia_label = QLabel()
        contrasenia_label.setText("Contraseña: ")

        self.contrasenia_input = QLineEdit()
        self.contrasenia_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        iniciar_boton = QPushButton()
        iniciar_boton.setText("Ingresar")
        iniciar_boton.clicked.connect(self.ingresar)

        registro_boton = QPushButton()
        registro_boton.setText("¿No tienes una cuenta?")
        registro_boton.clicked.connect(self.abrir_ventana_registro)
        registro_boton.setObjectName("enlace-button")  # Agregar clase CSS

        layout = QVBoxLayout()
        layout.addWidget(titulo)
        layout.addWidget(correo_label)
        layout.addWidget(self.correo_input)
        layout.addWidget(contrasenia_label)
        layout.addWidget(self.contrasenia_input)
        layout.addWidget(iniciar_boton)
        layout.addWidget(registro_boton)

        self.setLayout(layout)

        self.setStyleSheet("""
            #enlace-button {
                border: none;
                padding: 0;
                background: none;
                color: blue;
                text-decoration: underline;
            }
            #enlace-button:hover {
                color: red;
            }
        """)

    def ingresar(self):
        intento = f"{self.correo_input.text()},{self.contrasenia_input.text()}"
        autorizado = False
        try:
            with open("Dataset/usuarios.csv", "r") as archivo_usuarios:
                for linea in archivo_usuarios:
                    if linea.strip() == intento:
                        autorizado = True
                        break

            if autorizado:
                self.abrir_reserva()
                QMessageBox.information(self, "Informacion", "Se ha iniciado sesion", QMessageBox.StandardButton.Close)
                self.hide()
            else:
                QMessageBox.warning(self, "Error", "Los datos son incorrectos", QMessageBox.StandardButton.Close)
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "El archivo usuarios.csv no existe.", QMessageBox.StandardButton.Close)

    def abrir_reserva(self):
        from FormulariodeReserva import Reserva
        self.abrir_ventana = Reserva()
        self.abrir_ventana.show()

    def abrir_ventana_registro(self):
        from RegistrodeUsuario import VentanaRegistro
        self.ventana_registro = VentanaRegistro()
        self.ventana_registro.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    iniciar = IniciarSesion()
    iniciar.show()
    sys.exit(app.exec())
