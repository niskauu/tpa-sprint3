import csv
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from IniciodeSesion import IniciarSesion
import os

class VentanaRegistro(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciarUI()

    def iniciarUI(self):
        self.setWindowTitle("Registro de cuentas")
        self.setFixedSize(400,250)

        self.ventanita = QVBoxLayout()

        self.label_correo = QLabel("Correo:")
        self.input_correo = QLineEdit()
        self.ventanita.addWidget(self.label_correo)
        self.ventanita.addWidget(self.input_correo)

        self.label_contrasena = QLabel("Contraseña:")
        self.input_contrasena = QLineEdit()
        self.input_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.ventanita.addWidget(self.label_contrasena)
        self.ventanita.addWidget(self.input_contrasena)

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
        correo = self.input_correo.text()
        contrasena = self.input_contrasena.text()

        if correo and contrasena:
            with open(f"{os.path.dirname(__file__)}/Dataset/usuarios.csv", "r", newline="") as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                filas = list(lector_csv)

            filas.append([correo, contrasena])

            with open("Dataset/usuarios.csv", "w", newline="") as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                escritor_csv.writerows(filas)

            QMessageBox.information(self, "Registro Exitoso", "El usuario ha sido registrado exitosamente.")

            self.input_correo.clear()
            self.input_contrasena.clear()
            self.hide()
            self.abrir_ventana_iniciar_sesion()

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