import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QRadioButton, QPushButton, QTextEdit, QGroupBox, QButtonGroup
from PyQt6.QtGui import QPixmap

class VentanaExcursion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Selección de Excursión")
        self.setGeometry(100, 100, 800, 500)
        contenedor_principal = QVBoxLayout()

        layout_horizontal = QHBoxLayout()

        self.grupo_botones = QButtonGroup() 

        # Excursión Light
        light_box = QGroupBox("Excursión Light")
        light_layout = QVBoxLayout()

        light_radio = QRadioButton()
        light_layout.addWidget(light_radio)
        self.grupo_botones.addButton(light_radio)

        light_imagen = QLabel()
        light_pixmap = QPixmap("images/excursion_light.png")
        light_imagen.setPixmap(light_pixmap)
        light_imagen.setScaledContents(True)
        light_imagen.setFixedSize(250, 150)
        light_layout.addWidget(light_imagen)

        light_precio = QLabel("Su valor es de $10.000 por persona.")
        light_desc = QTextEdit()
        light_desc.setPlainText(
            '''Corresponde a una excursión de tipo caminata de 6 horas en total por senderos de complejidad baja con hermosos lugares de vegetación nativa y afluentes de agua, ideal para grupos familiares con niños o personas de 3ra edad.'''
        )
        light_desc.setReadOnly(True)
        light_layout.addWidget(light_precio)
        light_layout.addWidget(light_desc)

        light_box.setLayout(light_layout)
        layout_horizontal.addWidget(light_box)

        # Excursión Plus
        plus_box = QGroupBox("Excursión Plus")
        plus_layout = QVBoxLayout()

        plus_radio = QRadioButton()
        plus_layout.addWidget(plus_radio)
        self.grupo_botones.addButton(plus_radio)

        plus_imagen = QLabel()
        plus_pixmap = QPixmap("images/excursion_plus.png")
        plus_imagen.setPixmap(plus_pixmap)
        plus_imagen.setScaledContents(True)
        plus_imagen.setFixedSize(250, 150)
        plus_layout.addWidget(plus_imagen)

        plus_precio = QLabel("Su valor es de $50.000 por persona.")
        plus_desc = QTextEdit()
        plus_desc.setPlainText(
            '''Corresponde a una excursión de tipo hiking de 3 días en total por una cadena montañosa, experiencia de campamento y contemplación de glaciares y cascadas, ideal para grupos de personas con capacidades físicas compatibles con la exigencia de la caminata.'''
        )
        plus_desc.setReadOnly(True)
        plus_layout.addWidget(plus_precio)
        plus_layout.addWidget(plus_desc)

        plus_box.setLayout(plus_layout)
        layout_horizontal.addWidget(plus_box)

        # Excursión Heavy
        heavy_box = QGroupBox("Excursión Heavy")
        heavy_layout = QVBoxLayout()

        heavy_radio = QRadioButton()
        heavy_layout.addWidget(heavy_radio)
        self.grupo_botones.addButton(heavy_radio)

        heavy_imagen = QLabel()
        heavy_pixmap = QPixmap("images/excursion_heavy.png")
        heavy_imagen.setPixmap(heavy_pixmap)
        heavy_imagen.setScaledContents(True)
        heavy_imagen.setFixedSize(250, 150)
        heavy_layout.addWidget(heavy_imagen)

        heavy_precio = QLabel("Su valor es de $100.000 por persona.")
        heavy_desc = QTextEdit()
        heavy_desc.setPlainText(
            '''Corresponde a una excursión de tipo hiking de 5 días en total por una cadena montañosa y con navegación en afluentes locales. 
Se incluyen actividades extremas de Rapel, Canopi, Rafting y Escalada.
Las actividades requieren de capacidades físicas compatibles con la complejidad de la excursión.'''
        )
        heavy_desc.setReadOnly(True)
        heavy_layout.addWidget(heavy_precio)
        heavy_layout.addWidget(heavy_desc)

        heavy_box.setLayout(heavy_layout)
        layout_horizontal.addWidget(heavy_box)

        contenedor_principal.addLayout(layout_horizontal)  # Agregar layout en el contenedor principal

        botones_layout = QHBoxLayout()
        
        volver_boton = QPushButton("Volver")
        botones_layout.addWidget(volver_boton)

        continuar_button = QPushButton("Continuar")
        botones_layout.addWidget(continuar_button)

        # Agregar el layout de los botones al contenedor principal
        contenedor_principal.addLayout(botones_layout)

        widget = QWidget()
        widget.setLayout(contenedor_principal)  # Establecer el contenedor principal como diseño

        self.setCentralWidget(widget)

        continuar_button.clicked.connect(self.continuar_clicked)
        volver_boton.clicked.connect(self.volver_clicked)

    def continuar_clicked(self):
        opcion_excursion = self.grupo_botones.checkedButton()
        if opcion_excursion is not None:
            print("Excursión seleccionada:", opcion_excursion.text())
        else:
            print("No se ha seleccionado ninguna excursión.")

    def volver_clicked(self):
        print("Botón Volver presionado.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaExcursion()
    ventana.show()
    sys.exit(app.exec())

