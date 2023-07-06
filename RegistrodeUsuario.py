import csv
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from IniciodeSesion import IniciarSesion

class VentanaRegistro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de cuentas")
        self.setFixedSize(400,300)

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
        
        self.link_iniciar_sesion = QLabel("<a href='#'>¿Ya tiene una cuenta?</a>")
        self.link_iniciar_sesion.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.link_iniciar_sesion.setOpenExternalLinks(False)
        self.link_iniciar_sesion.linkActivated.connect(self.abrir_iniciar_sesion)
        self.ventanita.addWidget(self.link_iniciar_sesion)
        
        self.setLayout(self.ventanita)
        
    def registrar(self):
        usuario = self.input_usuario.text()
        contraseña = self.input_contraseña.text()
        
        if usuario and contraseña:
            with open("dataset/usuarios.csv", "a", newline="") as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                escritor_csv.writerow([usuario, contraseña])
                
            QMessageBox.information(self, "Registro Exitoso", "El usuario ha sido registrado exitosamente.")
            
            self.input_usuario.clear()
            self.input_contraseña.clear()
        else:
            QMessageBox.warning(self, "Error de Registro", "Por favor, ingrese un usuario y una contraseña.")
            
    def abrir_iniciar_sesion(self):
        self.hide()
        ventana_iniciar_sesion = IniciarSesion()
        ventana_iniciar_sesion.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana_signin = VentanaRegistro()
    ventana_signin.show()
    
    sys.exit(app.exec())
