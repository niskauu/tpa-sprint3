import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QRadioButton, QPushButton, QTextEdit


class VentanaExcursion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Selección de Excursión")
        self.setGeometry(100, 100, 600, 200)

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        label = QLabel("Seleccione el tipo de excursión")
        layout.addWidget(label)

        light_radio = QRadioButton("Excursión Light")
        light_desc = QTextEdit()
        light_desc.setPlainText(
            '''         Corresponde a una excursión de tipo caminata de
            6 horas en total por senderos de complejidad baja con hermosos 
            lugares de vegetación nativa y afluentes de agua, ideal para 
            grupos familiares con niños o personas de 3ra edad.
            Su valor es de $10.000 por persona.'''
        )
        light_desc.setReadOnly(True)
        layout.addWidget(light_radio)
        layout.addWidget(light_desc)

        plus_radio = QRadioButton("Excursión Plus")
        plus_desc = QTextEdit()
        plus_desc.setPlainText(
            '''         Corresponde a una excursión de tipo hiking de 3 días 
            en total por una cadena montañosa, experiencia de campamento 
            y contemplación de glaciares y cascadas, ideal para grupos de
            personas con capacidades físicas compatibles con la exigencia de la
            caminata.
            Su valor es de $50.000 por persona.'''
        )
        plus_desc.setReadOnly(True)
        layout.addWidget(plus_radio)
        layout.addWidget(plus_desc)

        heavy_radio = QRadioButton("Excursión Heavy")
        heavy_desc = QTextEdit()
        heavy_desc.setPlainText(
            '''         Corresponde a una excursión de tipo hiking de 5 días en total 
            por una cadena montañosa y con navegación en afluentes locales. 
            Se incluyen actividades extremas de Rapel, Canopi, Rafting y Escalada. 
            Las actividades requieren de capacidades físicas compatibles con la 
            complejidad de la excursión.
            Su valor es de $100.000 por persona.'''
        )
        heavy_desc.setReadOnly(True)
        layout.addWidget(heavy_radio)
        layout.addWidget(heavy_desc)

        continue_button = QPushButton("Continuar")
        layout.addWidget(continue_button)

        continue_button.clicked.connect(self.continuar_clicked)

    def continuar_clicked(self):
        print("Botón Continuar ha sido presionado.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaExcursion()
    ventana.show()
    sys.exit(app.exec())
