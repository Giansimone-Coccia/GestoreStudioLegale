from PyQt5.QtWidgets import QWidget, QGridLayout

from GestoreStudioLegale.Viste.VisteAdmin.VisteAdminCorso.VistaHomeCorsoAgg import VistaHomeCorsoAgg
from GestoreStudioLegale.Viste.VisteAdmin.VisteAdminCredenziali.VistaModificaCredenziali import VistaModificaCredenziali
from GestoreStudioLegale.Viste.VisteAdmin.VisteAdminAvvocato.VistaVisualizzaAvvocati import VistaVisualizzaAvvocati
from GestoreStudioLegale.Viste.VisteAdmin.VisteAdminCliente.VistaVisualizzaClienti import VistaVisualizzaClienti
from GestoreStudioLegale.Utilities.Utilities import Tools
#from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaStatistiche import VistaVisualizzaStatistiche


class VistaHomeAdmin(QWidget):

    tool=Tools()

    def __init__(self, parent=None):
        super(VistaHomeAdmin, self).__init__(parent)

        gLayout = QGridLayout()
        gLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        gLayout.addWidget(self.tool.createButton("Modifica Credenziali", self.reachCredenziali), 1, 0)
        gLayout.addWidget(self.tool.createButton("Mostra Avvocati", self.reachAvvocati), 2, 1)
        gLayout.addWidget(self.tool.createButton("Mostra Clienti", self.reachClienti), 2, 0)
        gLayout.addWidget(self.tool.createButton("Mostra Statistiche", self.reachStatistiche), 1, 1)
        gLayout.addWidget(self.tool.createButton("Corsi aggiornamento", self.reachCorsiAgg), 3, 0,1,2)
        self.setLayout(gLayout)
        self.resize(500, 400)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()

    def reachAvvocati(self):
        self.vistaVisualizzaA = VistaVisualizzaAvvocati()
        self.vistaVisualizzaA.show()
        self.close()

    def reachClienti(self):
        self.vistaVisualizzaC = VistaVisualizzaClienti()
        self.vistaVisualizzaC.show()
        self.close()

    def reachCorsiAgg(self):
        self.vistaCorsi = VistaHomeCorsoAgg()
        self.vistaCorsi.show()
        self.close()

    def reachCredenziali(self):
        self.vistaModC = VistaModificaCredenziali()
        self.vistaModC.show()
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