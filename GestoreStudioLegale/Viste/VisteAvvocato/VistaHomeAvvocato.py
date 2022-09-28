from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

# from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAppuntamentiA import VistaAppuntamentiA
from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAppuntamentiA import VistaHomeAppuntamentiA
from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeParcelle import VistaHomeParcelle
from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeUdienze import VistaHomeUdienze

class VistaHomeAvvocato(QWidget):

    def __init__(self, parent=None):
        super(VistaHomeAvvocato, self).__init__(parent)
        tool = Tools()
        gLayout = QGridLayout()
        gLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        gLayout.addWidget(self.createButton("Gestisci Appuntamenti", self.reachAppuntamenti), 1, 0)
        gLayout.addWidget(self.createButton("Parcelle", self.reachParcelle), 2, 0)
        gLayout.addWidget(self.createButton("Udienze", self.reachUdienze), 3, 0, 1, 2)
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
        self.vistaParcelle = VistaHomeParcelle()
        self.vistaParcelle.show()
        self.close()

    def reachUdienze(self):
        pass
        self.vistaUdienze = VistaHomeUdienze()
        self.vistaUdienze.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VistaHome import VistaHome
        self.vistaH = VistaHome()
        self.vistaH.show()
        self.close()
