from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

# from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAppuntamentiA import VistaAppuntamentiA
from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAppuntamentiA import VistaHomeAppuntamentiA


class VistaHomeAvvocato(QWidget):

    def __init__(self, parent=None):
        super(VistaHomeAvvocato, self).__init__(parent)
        gLayout = QGridLayout()
        gLayout.addWidget(self.createButton("Gestisci Appuntamenti", self.reachAppuntamenti), 0, 0)
        gLayout.addWidget(self.createButton("Parcelle", self.reachParcelle), 1, 0)
        gLayout.addWidget(self.createButton("Udienze", self.reachUdienze), 2, 0, 1, 2)
        self.setLayout(gLayout)
        self.resize(500, 400)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()

    def createButton(self, nome, on_click):
        button = QPushButton(nome)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setFont(QFont('Arial', 10))
        button.clicked.connect(on_click)
        return button

    def reachAppuntamenti(self):
        self.vistaAppuntamenti = VistaHomeAppuntamentiA()
        self.vistaAppuntamenti.show()
        self.close()

    def reachParcelle(self):
        pass
        #self.vistaAppuntamenti = VistaHomeAppuntamentiA()
        #self.vistaAppuntamenti.show()
        #self.close()

    def reachUdienze(self):
        pass
        #self.vistaAppuntamenti = VistaHomeAppuntamentiA()
        #self.vistaAppuntamenti.show()
        #self.close()
