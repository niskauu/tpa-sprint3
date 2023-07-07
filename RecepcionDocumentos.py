import sys
from PyQt6.QtWidgets import QApplication, QFileDialog, QMessageBox, QMainWindow, QLabel, QTextEdit, QCheckBox, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea

class Documentos(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ventana de Documentos")
        self.setGeometry(100, 100, 600, 500)

        # Widget principal para el diseño vertical
        widget = QWidget(self)
        self.setCentralWidget(widget)

        # Layout vertical para los widgets
        layout_vertical = QVBoxLayout()
        widget.setLayout(layout_vertical)

        texto = QLabel('''Dado el tipo de excursión escogida, requerimos documentos médicos que acrediten sus capacidades físicas. 
Este procedimiento es por y para su seguridad.''')
        layout_vertical.addWidget(texto)

        docs_requeridos = QLabel('''\nEn el siguiente cuadro adjunte: 
                                                1.- Constancia médica *
                                                2.- Declaración jurada *
                                                3.- Anexos (electrocardiogramas, radiografías y/o tomografías)''')
        layout_vertical.addWidget(docs_requeridos)

        advertencia = QLabel('''\nLos documentos marcados con un asterisco (*) son obligatorios para asistir a la excursión.
De no presentar alguno, no podrá participar, es su responsabilidad adjuntar dichos documentos.''')
        layout_vertical.addWidget(advertencia)

        self.doc_archivos = QTextEdit()
        layout_vertical.addWidget(self.doc_archivos)

        adjuntar_btn = QPushButton("Seleccione archivos")
        adjuntar_btn.clicked.connect(self.adjuntar_archivos)
        layout_vertical.addWidget(adjuntar_btn)

        presencial = QLabel('''Si lo desea, puede presentar los documentos de manera presencial el día de la excursión.
Para ello, debe aceptar las siguientes condiciones:''')
        layout_vertical.addWidget(presencial)

        condiciones = QLabel('''
        1. Usted acepta presentar los documentos correspondientes el día de la excursión.
        2. Si usted no presenta los documentos, usted acepta que no puede participar de la excursión.
        3. Si no participa de la excursión, usted acepta que no tiene derecho a reembolso.\n''')
        layout_vertical.addWidget(condiciones)

        self.checkbox = QCheckBox("He leído y acepto los términos y condiciones")
        layout_vertical.addWidget(self.checkbox)

        layout_botones = QHBoxLayout()
        layout_vertical.addLayout(layout_botones)

        volver = QPushButton("Volver")
        volver.clicked.connect(self.volver_presionado)
        layout_botones.addWidget(volver)

        continuar = QPushButton("Continuar")
        continuar.clicked.connect(self.continuar_presionado)
        layout_botones.addWidget(continuar)

    def adjuntar_archivos(self):
        archivos, _ = QFileDialog.getOpenFileNames(self, "Adjuntar archivos")
        if archivos:
            self.doc_archivos.setText("\n".join(archivos))

    def continuar_presionado(self):
        from VentanadePago import VentanaPagos

        archivos_adjuntados = bool(self.doc_archivos.toPlainText())
        terminos_aceptados = self.checkbox.isChecked()

        if archivos_adjuntados or terminos_aceptados:
            if archivos_adjuntados and terminos_aceptados:
                QMessageBox.warning(self, "Advertencia", "No puede adjuntar archivos y aceptar los términos al mismo tiempo.")
            else:
                self.ventana_pagos = VentanaPagos()
                self.ventana_pagos.show()
                self.hide()
        else:
            QMessageBox.warning(
                self,
                "Advertencia",
                "Antes de continuar debe adjuntar sus archivos o aceptar los términos para presentar los documentos presencialmente.",
                QMessageBox.StandardButton.Ok,
            )

    def volver_presionado(self):
        from TipodeExcursion import VentanaExcursion
        self.ventana_excursion = VentanaExcursion()
        self.ventana_excursion.show()
        self.hide()

'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Documentos()
    window.show()
    sys.exit(app.exec())'''