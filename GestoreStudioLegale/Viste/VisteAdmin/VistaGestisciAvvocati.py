from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaAvvocati import VistaVisualizzaAvvocati


class VistaGestisciAvvocati (QWidget):

    def __init__(self, parent=None):
        super(VistaGestisciAvvocati, self).__init__(parent)
        tool=Tools()
        gLayout = QGridLayout()
        gLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        gLayout.addWidget(tool.createButton("Modifica Avvocati", self.reachModificaAvvocati), 1, 0)
        gLayout.addWidget(tool.createButton("Visualizza Avvocati", self.reachVisualizzaAvvocati), 2, 0)
        self.setLayout(gLayout)
        self.resize(500, 400)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()

    def reachModificaAvvocati(self):
        pass

    def reachVisualizzaAvvocati(self):
        self.vistaVisualizzaAvvocati = VistaVisualizzaAvvocati()
        self.vistaVisualizzaAvvocati.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeAdmin import VistaHomeAdmin
        self.vistaHome = VistaHomeAdmin()
        self.vistaHome.show()
        self.close()
        tool=Tools()
        gLayout = QGridLayout()
        gLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        gLayout.addWidget(tool.createButton("Modifica Avvocati", self.reachModificaAvvocati), 1, 0)
        gLayout.addWidget(tool.createButton("Visualizza Avvocati", self.reachVisualizzaAvvocati), 2, 0)
        self.setLayout(gLayout)
        self.resize(500, 400)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()

    def reachModificaAvvocati(self):
        pass

    def reachVisualizzaAvvocati(self):
        self.vistaVisualizzaAvvocati = VistaVisualizzaAvvocati()
        self.vistaVisualizzaAvvocati.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeAdmin import VistaHomeAdmin
        self.vistaHome = VistaHomeAdmin()
        self.vistaHome.show()
        self.close()
