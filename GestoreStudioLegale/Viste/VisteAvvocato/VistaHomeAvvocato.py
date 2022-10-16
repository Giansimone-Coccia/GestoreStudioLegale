from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAvvocato.VistaAggiungiCliente import VistaAggiungiCliente
from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAppuntamentiA import VistaHomeAppuntamentiA
from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeParcelle import VistaHomeParcelle
from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeUdienze import VistaHomeUdienze

class VistaHomeAvvocato(QWidget):

    def __init__(self, parent=None):
        super(VistaHomeAvvocato, self).__init__(parent)
        tool = Tools()
        gLayout = QGridLayout()
        gLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)

        tool = Tools()
        self.clientiList = tool.loadClienti()
        self.avvocatiList = tool.loadAvvocati()

        for avvocato in self.avvocatiList:
            if avvocato.codiceFiscale == tool.leggi().rsplit()[0]:
                self.avvClientiList = avvocato.clienti
                for clienteAvv in self.avvClientiList:
                    i=0
                    for cliente in self.clientiList:
                        if clienteAvv.getDatiCliente()["Id"] == cliente.getDatiCliente()["Id"]:
                            i=1
                    if i == 0:
                        self.avvClientiList.remove(clienteAvv)
                        avvocato.aggiornaAvvocato(clienti=self.avvClientiList)
                        for cliennte in self.avvClientiList:
                            print(cliennte.getDatiCliente())

        gLayout.addWidget(self.createButton("Gestisci Appuntamenti", self.reachAppuntamenti), 1, 0)
        gLayout.addWidget(self.createButton("Parcelle", self.reachParcelle), 2, 0)
        gLayout.addWidget(self.createButton("Udienze", self.reachUdienze), 3, 0, 1, 2)
        gLayout.addWidget(self.createButton("Aggiungi cliente", self.reachAggiungiCliente), 4, 0, 1, 2)
        gLayout.addWidget(self.createButton("Scegli corso aggiornamento", self.reachSceltaCorso), 5, 0, 1, 2)
        self.setLayout(gLayout)
        self.resize(600, 500)
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
        self.vistaParcelle = VistaHomeParcelle()
        self.vistaParcelle.show()
        self.close()

    def reachUdienze(self):
        self.vistaUdienze = VistaHomeUdienze()
        self.vistaUdienze.show()
        self.close()

    def reachAggiungiCliente(self):
        self.vistaAggCliente = VistaAggiungiCliente()
        self.vistaAggCliente.show()
        self.close()

    def reachSceltaCorso(self):
        pass

    def rewind(self):
        from GestoreStudioLegale.Viste.VistaHome import VistaHome
        self.vistaH = VistaHome()
        self.vistaH.show()
        self.close()