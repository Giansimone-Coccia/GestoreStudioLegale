from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from GestoreStudioLegale.Viste.VisteAdmin.VistaModificaPassword import VistaModificaPassword
from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaAvvocati import VistaVisualizzaAvvocati
from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaClienti import VistaVisualizzaClienti
#from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaStatistiche import VistaVisualizzaStatistiche
#from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaStatistiche import VistaVisualizzaStatistiche
from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaStatistiche import VistaVisualizzaStatistiche


class VistaHomeAdmin(QWidget):

    def __init__(self, parent=None):
        super(VistaHomeAdmin, self).__init__(parent)

        tool=Tools()
        gLayout = QGridLayout()
        gLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        gLayout.addWidget(tool.createButton("Modifica Password", self.reachModificaPassword), 1, 0)
        gLayout.addWidget(tool.createButton("Mostra Avvocati", self.reachAvvocati), 1, 1)
        gLayout.addWidget(tool.createButton("Mostra Clienti", self.reachClienti), 2, 0)
        gLayout.addWidget(tool.createButton("Mostra Statistiche", self.reachStatistiche), 2, 1)
        self.setLayout(gLayout)
        self.resize(500, 400)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()


    def reachModificaPassword(self):
        self.vistaModPassword = VistaModificaPassword()
        self.vistaModPassword.show()
        self.close()

    def reachAvvocati(self):
        self.vistaVisualizzaA = VistaVisualizzaAvvocati()
        self.vistaVisualizzaA.show()
        self.close()

    def reachClienti(self):
        self.vistaVisualizzaC = VistaVisualizzaClienti()
        self.vistaVisualizzaC.show()
        self.close()

    def reachStatistiche(self):
        self.vistaVisualizzaS = VistaVisualizzaStatistiche()
        self.vistaVisualizzaS.show()
        #self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.LoginAdmin import LoginAdmin
        self.vistaHome = LoginAdmin()
        self.vistaHome.show()
        self.close()