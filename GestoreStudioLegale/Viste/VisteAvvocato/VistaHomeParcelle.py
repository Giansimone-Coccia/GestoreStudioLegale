from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QMainWindow, QScrollArea
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Servizi.Cliente import Cliente

class VistaHomeParcelle(QMainWindow):

    parcelleList = []
    avvocatiList = []
    clientiList = []
    tool = Tools()

    def __init__(self, parent=None):
        super(VistaHomeParcelle, self).__init__(parent)
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.grifLayout = QGridLayout()
        self.grifLayout.addWidget(self.tool.rewindButton(self.rewind1), 0, 0)
        self.getDatiP()
        self.widget.setLayout(self.grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(800, 600)
        self.setWindowTitle("Parcelle")
        self.show()

    def getDatiP(self):
        self.parcelleList = self.tool.loadParcelle()
        self.avvocatiList = self.tool.loadAvvocati()
        tool = Tools()
        parc = []
        i=0

        print("ca")
        #print(avvocato.getDatiAvvocato()['clienti'])

        for avvocato in self.avvocatiList:
            print("noia")
            print (self.tool.leggi().rsplit()[0])
            print (avvocato.codiceFiscale)
            if avvocato.codiceFiscale == self.tool.leggi().rsplit()[0]:
               print("coglione")
               print(avvocato.getDatiAvvocato()['clienti'])
               clienti = avvocato.getDatiAvvocato()['clienti']
               print("ciao")
               print(clienti)
               print("cag")
               for cliente in clienti:
                    print("cioooo")
                    for parcella in self.parcelleList:
                        if parcella.Cliente.codiceFiscale == cliente.codiceFiscale:
                            print("cad")
                            parc.append(parcella)
                            print (parc)

        for p in parc:
            label = QLabel()
            print(p)
            label.setText(
                'Parcella: '+'\n'+ 'INTESTATARIO: '+f"{p.getDatiParcellaCliente()['intestatario']}"+ '\n'+'IMPORTO: '+f"{p.getDatiParcellaCliente()['importo']}"+'€'+'\n'+'ID: '+f"{p.getDatiParcellaCliente()['ID']}"+'\n'+'IDENTIFICATIVO: '+f"{p.getDatiParcellaCliente()['identificativo']}")
            label.setGeometry(QRect(0, 0, 350, 20))
            label.setFont(QFont('Arial', 10))
            label.setStyleSheet("border: 1px solid black;")
            print("ciao2")
            self.grifLayout.addWidget(label,i,1,1,2)
            i += 1
            self.grifLayout.addWidget(tool.createButton("Modifica", self.aggiornaParcella), i, 1)
            self.grifLayout.addWidget(
                tool.createButton("Elimina", self.rimuoviParcella),i,2)
            i += 1
            print("cos")

    def aggiungiParcella(self):
        pass

    def aggiornaParcella(self):
        pass

    def rimuoviParcella(self):
        pass

    def getDatiC(self):
        self.clientiList = self.tool.loadClienti()
        tool = Tools()
        print(tool.leggi())
        for cliente in self.clientiList:
            if cliente.codiceFiscale == str(tool.leggi()).rsplit()[0]:
                    return cliente.getDatiCliente()

    def rewind1(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAvvocato import VistaHomeAvvocato
        self.vistaHome = VistaHomeAvvocato()
        self.vistaHome.show()
        self.close()
