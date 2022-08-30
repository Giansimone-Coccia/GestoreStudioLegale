from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QSizePolicy

from GestoreStudioLegale.Viste.VistaHomeAppuntamentiC import VistaHomeAppuntamenti
from GestoreStudioLegale.Viste.VistaHomeParcelle import VistaHomeParcelle
from GestoreStudioLegale.Viste.VistaHomeUdienze import VistaHomeUdienze


class VistaHomeCliente(QWidget):

    def __init__(self, parent=None):
        super(VistaHomeCliente, self).__init__(parent)
        gLayout = QGridLayout()
        gLayout.addWidget(self.createButton("Appuntamenti", self.reachAppuntamenti), 0, 0)
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
        self.vistaAppuntamenti = VistaHomeAppuntamenti()
        self.vistaAppuntamenti.show()
        self.close()

    def reachParcelle(self):
        self.vistaParcelleH = VistaHomeParcelle()
        self.vistaParcelleH.show()
        self.close()

    def reachUdienze(self):
        self.vistaUdienze = VistaHomeUdienze()
        self.vistaUdienze.show()
        self.close()