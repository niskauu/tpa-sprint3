import csv
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from IniciodeSesion import IniciarSesion

class VentanaRegistro(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciarUI()

    def iniciarUI(self):
        self.setWindowTitle("Registro de cuentas")
        self.setFixedSize(400,250)

        self.ventanita = QVBoxLayout()

        self.label_usuario = QLabel("Correo:")
        self.input_usuario = QLineEdit()
        self.ventanita.addWidget(self.label_usuario)
        self.ventanita.addWidget(self.input_usuario)

        self.label_contraseña = QLabel("Contraseña:")
        self.input_contraseña = QLineEdit()
        self.input_contraseña.setEchoMode(QLineEdit.EchoMode.Password)
        self.ventanita.addWidget(self.label_contraseña)
        self.ventanita.addWidget(self.input_contraseña)

        self.boton_registrar = QPushButton("Registrar")
        self.boton_registrar.clicked.connect(self.registrar)
        self.ventanita.addWidget(self.boton_registrar)

        self.iniciar_sesion_boton = QPushButton("¿Ya tienes una cuenta?")
        self.iniciar_sesion_boton.clicked.connect(self.abrir_ventana_iniciar_sesion)
        self.iniciar_sesion_boton.setObjectName("enlace-button")  # Agregar clase CSS
        self.ventanita.addWidget(self.iniciar_sesion_boton)

        self.setLayout(self.ventanita)

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

    def registrar(self):
        usuario = self.input_usuario.text()
        contraseña = self.input_contraseña.text()

        if usuario and contraseña:
            with open("Dataset/usuarios.csv", "r", newline="") as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                filas = list(lector_csv)

            filas.append([usuario, contraseña])

            with open("Dataset/usuarios.csv", "w", newline="") as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                escritor_csv.writerows(filas)

            QMessageBox.information(self, "Registro Exitoso", "El usuario ha sido registrado exitosamente.")

            self.input_usuario.clear()
            self.input_contraseña.clear()
        else:
            QMessageBox.warning(self, "Error de Registro", "Por favor, ingrese un usuario y una contraseña.")

    def abrir_ventana_iniciar_sesion(self):
        self.ventana_iniciar_sesion = IniciarSesion()
        self.ventana_iniciar_sesion.show()
        self.hide()

'''if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_signin = VentanaRegistro()
    ventana_signin.show()
    sys.exit(app.exec())'''