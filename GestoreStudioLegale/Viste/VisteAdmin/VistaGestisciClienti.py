from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QVBoxLayout

from GestoreStudioLegale.Utilities.Utilities import Tools
#from GestoreStudioLegale.Viste.VisteCliente.VistaHomeCliente import VistaHomeCliente
from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaClienti import VistaVisualizzaClienti
from GestoreStudioLegale.Viste.VisteCliente.VistaVisualizzaAppuntamento import VistaVisualizzaAppuntamento


class VistaGestisciClienti (QWidget):

    def __init__(self, parent=None):
        super(VistaGestisciClienti, self).__init__(parent)

        tool=Tools()
        gLayout = QGridLayout()

        gLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        gLayout.addWidget(tool.createButton("Modifica Clienti", self.reachModificaClienti), 1, 0)
        gLayout.addWidget(tool.createButton("Visualizza Clienti", self.reachVisualizzaClienti), 2, 0)

        self.setLayout(gLayout)
        self.resize(500, 400)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()

    def reachModificaClienti(self):
        pass

    def reachVisualizzaClienti(self):
        self.vistaVisualizzaClienti = VistaVisualizzaClienti()
        self.vistaVisualizzaClienti.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeAdmin import VistaHomeAdmin
        self.vistaHome = VistaHomeAdmin()
        self.vistaHome.show()
        self.close()
