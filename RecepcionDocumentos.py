import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QCheckBox, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ventana de Documentos")
        self.setGeometry(100, 100, 500, 500)

        texto = QLabel('''Dado el tipo de excursión escogida, requerimos 
                documentos médicos que acrediten sus capacidades físicas. 
                Este procedimiento es por y para su seguridad.''', self)
        texto.setGeometry(20, 20, 360, 50)

        docs_requeridos = QLabel('''En el siguiente cuadro adjunte: 
                        constancia médica, declaración jurada, y 
                        opcionalmente anexos (electrocardiograma, 
                        radiografías y tomografías).''', self)
        docs_requeridos.setGeometry(20, 70, 360, 60)

        doc_edit = QTextEdit(self)
        doc_edit.setGeometry(20, 140, 360, 120)

        presencial = QLabel('''Si lo desea, puede presentar los documentos de 
        manera presencial el día de la excursión, para ello, 
        debe aceptar las siguientes condiciones:''', self)
        presencial.setGeometry(20, 260, 360, 50)

        condiciones = QLabel('''1. Usted acepta presentar los documentos 
        correspondientes el dia de la excuersion.
        2.Si udted no presenta los documentos, 
        usted acepta que no puede participar de la excursion
        3. Si no participa de la excuersion, 
        usted acepta que no tiene derecho a reembolso''', self)
        condiciones.setGeometry(40, 310, 320, 100)

        self.checkbox = QCheckBox("He leído y acepto los términos y condiciones", self)
        self.checkbox.setGeometry(20, 450, 280, 20)

        continuar = QPushButton("Continuar", self)
        continuar.setGeometry(320, 460, 60, 20)
        continuar.clicked.connect(self.continue_button_clicked)

    def continue_button_clicked(self):
        if self.checkbox.isChecked():
            print("jijiji")
        else:
            print("acepta las weas primero")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
