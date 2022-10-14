from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteCliente.VistaHomeAppuntamentiC import VistaHomeAppuntamentiC
from GestoreStudioLegale.Viste.VisteCliente.VistaHomeParcelle import VistaHomeParcelle
from GestoreStudioLegale.Viste.VisteCliente.VistaHomeUdienze import VistaHomeUdienze


class VistaHomeCliente(QWidget):

    def __init__(self, parent=None):
        super(VistaHomeCliente, self).__init__(parent)
        tool = Tools()
        gLayout = QGridLayout()
        gLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        gLayout.addWidget(tool.createButton("Appuntamenti", self.reachAppuntamenti), 1, 0)
        gLayout.addWidget(tool.createButton("Parcelle", self.reachParcelle), 2, 0)
        gLayout.addWidget(tool.createButton("Udienze", self.reachUdienze), 3, 0, 1, 3)

        self.clientiList = tool.loadClienti()
        self.avvocatiList = tool.loadAvvocati()
        self.appC = []

        self.setLayout(gLayout)
        self.resize(500, 400)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()

    def reachAppuntamenti(self):
        self.vistaAppuntamenti = VistaHomeAppuntamentiC()
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

    def rewind(self):
        from GestoreStudioLegale.Viste.VistaHome import VistaHome
        self.vistaH = VistaHome()
        self.vistaH.show()
        self.close()

