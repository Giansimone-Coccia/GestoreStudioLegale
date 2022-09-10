from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QVBoxLayout

from GestoreStudioLegale.Utilities.Utilities import Tools
#from GestoreStudioLegale.Viste.VisteCliente.VistaHomeCliente import VistaHomeCliente
from GestoreStudioLegale.Viste.VisteCliente.VistaPrenotaAppuntamentiC import VistaPrenotaAppuntamentiC
from GestoreStudioLegale.Viste.VisteCliente.VistaVisualizzaAppuntamento import VistaVisualizzaAppuntamento


class VistaHomeAppuntamentiC (QWidget):

    tool = Tools()

    def __init__(self, parent=None):
        super(VistaHomeAppuntamentiC, self).__init__(parent)
        gLayout = QGridLayout()
        gLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        gLayout.addWidget(self.tool.createButton("Prenota Appuntamento", self.reachPrenotaAppuntamento), 1, 0)
        gLayout.addWidget(self.tool.createButton("Visualizza Appuntamento", self.reachVisualizzaAppuntamento), 2, 0)
        self.setLayout(gLayout)
        self.resize(500, 400)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()

    def reachPrenotaAppuntamento(self):
        self.vistaPrenotazione = VistaPrenotaAppuntamentiC()
        self.vistaPrenotazione.show()
        self.close()

    def reachVisualizzaAppuntamento(self):
        self.vistaAppuntamento = VistaVisualizzaAppuntamento()
        self.vistaAppuntamento.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteCliente.VistaHomeCliente import VistaHomeCliente
        self.vistaHome = VistaHomeCliente()
        self.vistaHome.show()
        self.close()


