import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton, QGridLayout, QLabel, QDateEdit, QCalendarWidget, QMessageBox
from PyQt6.QtGui import QFont
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

class Reserva(QWidget):

    def __init__(self):
        super().__init__()
        self.iniciarUI()
    
    def iniciarUI(self):
        self.setFixedSize(600, 400) #geometria de la ventana
        self.setWindowTitle("Formulario De Reserva de Excursion")
        self.reservar()
        self.show()

    def reservar(self):
        
        #titulo
        titulo = QLabel()
        titulo.setText("Inicio De Sesion")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        titulo.setFont(font)

        #nombre
        nombre_label = QLabel()
        nombre_label.setText("Nombre: ")

        self.nombre_input = QLineEdit()

        #apellido
        apellido_label = QLabel()
        apellido_label.setText("Apellidos: ")

        self.apellido_input = QLineEdit()

        #rut
        rut_label = QLabel()
        rut_label.setText("Rut: ")

        self.rut_input = QLineEdit()

        #fecha de nacimiento
        fecha_nacimiento = QLabel()
        fecha_nacimiento.setText("Fecha de Nacimiento: ")
        self.fecha_nacimiento = QDateEdit()
        self.fecha_nacimiento.setCalendarPopup(True)
        self.fecha_nacimiento.setMinimumDate(date.today()-relativedelta(years=100))
        self.fecha_nacimiento.setMaximumDate(date.today()-relativedelta(years=18))

        #telefono
        telefono_label = QLabel()
        telefono_label.setText("Telefono: ")

        self.telefono_input = QLineEdit()
        
        #email
        email_label = QLabel()
        email_label.setText("E-mail: ")

        self.email_input = QLineEdit()

        #calendario para fecha de inicio de la excursion
        fecha_inicio = QLabel()
        fecha_inicio.setText("Fecha Inicio De la Excursion: ")
        self.fecha_inicio = QCalendarWidget()
        self.fecha_inicio.setFixedSize(350,200)
            #minimo y maximo
        self.fecha_inicio.setMinimumDate(date.today())
        self.fecha_inicio.setMaximumDate(date.today()+timedelta(days=60))

        #boton
        boton = QPushButton()
        boton.setText("Continuar")
        boton.clicked.connect(self.guardar_reserva)

        # Agregar botón "Agregar Acompañante"
        boton_agregar_acompanante = QPushButton()
        boton_agregar_acompanante.setText("Agregar Acompañante")
        boton_agregar_acompanante.clicked.connect(self.mostrar_ventana_acompanante)

        #layouts
        layout_main = QVBoxLayout()
    
        layout_labels1 = QVBoxLayout()
        layout_labels1.addWidget(nombre_label)
        layout_labels1.addWidget(apellido_label)
        layout_labels1.addWidget(rut_label)

        layout_input1 = QVBoxLayout()
        layout_input1.addWidget(self.nombre_input)
        layout_input1.addWidget(self.apellido_input)
        layout_input1.addWidget(self.rut_input)

        layout_labels2 = QVBoxLayout()
        layout_labels2.addWidget(fecha_nacimiento)
        layout_labels2.addWidget(telefono_label)
        layout_labels2.addWidget(email_label)

        layout_input2 = QVBoxLayout()
        layout_input2.addWidget(self.fecha_nacimiento)
        layout_input2.addWidget(self.telefono_input)
        layout_input2.addWidget(self.email_input)

        layouts = QHBoxLayout()
        layouts.addLayout(layout_labels1)
        layouts.addLayout(layout_input1)
        layouts.addLayout(layout_labels2)
        layouts.addLayout(layout_input2)

        fecha_inicio_layout = QGridLayout()
        fecha_inicio_layout.addWidget(fecha_inicio,0,1)
        fecha_inicio_layout.addWidget(self.fecha_inicio,1,1)

        fecha_inicio_widget = QWidget()
        fecha_inicio_widget.setLayout(fecha_inicio_layout)

        layout_main.addWidget(titulo)
        layout_main.addLayout(layouts)
        layout_main.addWidget(fecha_inicio_widget)
        layout_main.addWidget(boton)
        layout_main.addWidget(boton_agregar_acompanante)

        self.setLayout(layout_main)

    def func_aux(self):
        return True
    
    def mostrar_ventana_acompanante(self):
        from AgregarAcompañantes import VentanaAcompanante
        self.ventana_acompanante = VentanaAcompanante()
        self.ventana_acompanante.show()

    #guarda datos
    def guardar_reserva(self):
        from TipodeExcursion import VentanaExcursion
        if self.nombre_input.isModified() == True and self.apellido_input.isModified() == True and self.rut_input.isModified() == True and self.telefono_input.isModified() == True and self.email_input.isModified() == True:
            #guardar
            archivo = open("Dataset/reserva.csv", "a")
            fecha_inicio_temp = self.fecha_inicio.selectedDate().toPyDate()
            
            datos = f"{self.nombre_input.text()},{self.apellido_input.text()},{self.rut_input.text()},{self.fecha_nacimiento.text()},{self.telefono_input.text()},{self.email_input.text()},{fecha_inicio_temp.strftime('%d-%m-%Y')}\n"
            archivo.write(datos)
            archivo.close()

            self.ventana_excursion = VentanaExcursion()
            self.ventana_excursion.show()
            self.hide()
        else:
            QMessageBox.warning(self,"Error", "No puede dejar campos vacios", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)

'''if __name__ == "__main__":    
    app = QApplication(sys.argv)
    iniciar = Reserva()
    sys.exit(app.exec())'''