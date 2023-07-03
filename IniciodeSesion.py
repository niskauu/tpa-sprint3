import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox, QLabel
from PyQt6.QtGui import QFont
from FormulariodeReserva import Reserva

class IniciarSesion(QWidget):

    #init + iniciar ui
    def __init__(self):
        super().__init__()
        self.iniciarUI()

    def iniciarUI(self):
        self.setFixedSize(400,200) #geometria de la ventana
        self.setWindowTitle("Inicio de Sesion")
        self.iniciar_sesion()
        self.show()
    
    def iniciar_sesion(self): #establecer diseño de la ventana
        self.estaloggeado = False #la persona no ha iniciado sesion

        #titulo
        titulo = QLabel()
        titulo.setText("Inicio De Sesion")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        titulo.setFont(font)

        #correo
        correo_label = QLabel()
        correo_label.setText("Correo: ")

        self.correo_input = QLineEdit()

        #contraseña
        contrasenia_label = QLabel()
        contrasenia_label
        contrasenia_label.setText("Contraseña: ")

        self.contrasenia_input = QLineEdit()
        self.contrasenia_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        #boton iniciar sesion
        iniciar_boton = QPushButton()
        iniciar_boton.setText("Ingresar")
            #conectar la interaccion con ingresar a la ventana principar
        iniciar_boton.clicked.connect(self.ingresar)

        layout = QVBoxLayout()
        layout.addWidget(titulo)
        layout.addWidget(correo_label)
        layout.addWidget(self.correo_input)
        layout.addWidget(contrasenia_label)
        layout.addWidget(self.contrasenia_input)
        layout.addWidget(iniciar_boton)

        self.setLayout(layout)

    #manejo de usuario si existe o no
    def ingresar(self):
        intento = f"{self.correo_input.text()},{self.contrasenia_input.text()}"
        autorizado = False
        try:
            archivo_usuarios = open("Dataset/usuarios.csv", "r")
            for linea in archivo_usuarios:
                print(linea)
                if linea == intento:
                    autorizado = True
            if autorizado == True:
                #Funcion conectar con la otra ventana
                self.abrir_reserva()
                archivo_usuarios.close()
                QMessageBox.information(self, "Informacion", "Se ha iniciado sesion", QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                self.hide()
            else:
                QMessageBox.warning(self, "Error", "Los datos son incorrectos", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "El archivo usuarios.csv no existe.", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)


        
    #se abre ventana de registro de reserva
    def abrir_reserva(self):
        self.abrir_ventana = Reserva()
        self.abrir_ventana.show()

if __name__ == "__main__":    
    app = QApplication(sys.argv)
    iniciar = IniciarSesion()
    sys.exit(app.exec())
