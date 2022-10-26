from PyQt5.QtWidgets import QWidget, QGridLayout

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteCliente.VistaHomeAppuntamentiC import VistaHomeAppuntamentiC
from GestoreStudioLegale.Viste.VisteCliente.VistaHomeParcelle import VistaHomeParcelle
from GestoreStudioLegale.Viste.VisteCliente.VistaHomeUdienze import VistaHomeUdienze


class VistaHomeCliente(QWidget):

    tool = Tools()

    def __init__(self, parent=None):
        super(VistaHomeCliente, self).__init__(parent)

        gLayout = QGridLayout()
        gLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        gLayout.addWidget(self.tool.createButton("Appuntamenti", self.reachAppuntamenti), 1, 0)
        gLayout.addWidget(self.tool.createButton("Parcelle", self.reachParcelle), 2, 0)
        gLayout.addWidget(self.tool.createButton("Udienze", self.reachUdienze), 3, 0)

        self.clientiList = self.tool.loadClienti()
        self.avvocatiList = self.tool.loadAvvocati()
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