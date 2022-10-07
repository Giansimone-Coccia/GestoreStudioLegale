from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QMainWindow, QScrollArea, QHBoxLayout
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Servizi.Cliente import Cliente


#modificare dimensioni tasti in utilities
class ParcellaRicercata(QMainWindow):

    parcelleList = []
    avvocatiList = []
    clientiList = []
    tool = Tools()

    def __init__(self, parcelle,parent=None):
        super(ParcellaRicercata, self).__init__(parent)
        tool = Tools()
        self.parcelleTrovate = []
        print("ciaoo45")
        for parcella in parcelle:
            self.parcelleTrovate.append(parcella)

        self.cWidget = QWidget()  # contiene tutto
        self.outerLayout = QVBoxLayout()
        #self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box

        self.grifLayout = QGridLayout()

        self.outerLayout.addWidget(tool.rewindButton(self.rewind1), 1)
        #self.outerLayout.addLayout(self.button_layout, 1)
        self.outerLayout.addWidget(self.scroll, 9)
        #self.button_layout.addWidget(tool.createButton("Inserisci", self.aggiungiParcella))
        #self.button_layout.addWidget(tool.createButton("Cerca", self.cercaParcella))
        self.cWidget.setLayout(self.outerLayout)

        self.getDatiP()
        self.widget.setLayout(self.grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.cWidget)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(800, 600)
        self.setWindowTitle("Parcelle")
        self.show()

    def getDatiP(self):
        self.parcelleList = self.tool.loadParcelle()
        self.avvocatiList = self.tool.loadAvvocati()
        tool = Tools()
        #parc = []
        i=1

        '''for avvocato in self.avvocatiList:
            #print("noia")
            print (self.tool.leggi().rsplit()[0])
            print (avvocato.codiceFiscale)
            print(avvocato.getDatiAvvocato()['clienti'])
            if avvocato.codiceFiscale == self.tool.leggi().rsplit()[0]:
               #print("coglione")
               print(avvocato.getDatiAvvocato()['clienti'])
               clienti = avvocato.getDatiAvvocato()['clienti']
               #print("ciao")
               print(clienti)
               #print("cag")
               for cliente in clienti:
                    #print("cioooo")
                    for parcella in self.parcelleList:
                        if parcella.Cliente.codiceFiscale == cliente.codiceFiscale:
                            #print("cad")
                            parc.append(parcella)
                            print (parc)
            '''
        for par in self.parcelleTrovate:
            label = QLabel()
            textLabel2 = QLabel()
            textLabel2.setText(
                'Cliente: ' + '\n' + 'NOME: ' + f"{par.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Nome']}" + '\n' + 'COGNOME: ' + f"{par.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Cognome']}" + '\n' + 'ID: ' + f"{par.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{par.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{par.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{par.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Numero telefono']}")
            textLabel2.setGeometry(QRect(0, 0, 350, 20))
            textLabel2.setFont(QFont('Arial', 10))
            textLabel2.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(textLabel2, i, 1, 1, 2)
            i += 1
            label.setText(
                'Parcella: '+'\n'+ 'INTESTATARIO: '+f"{par.getDatiParcellaCliente()['intestatario']}"+ '\n'+'IMPORTO: '+f"{par.getDatiParcellaCliente()['importo']}"+'€'+'\n'+'ID: '+f"{par.getDatiParcellaCliente()['ID']}"+'\n'+'IDENTIFICATIVO: '+f"{par.getDatiParcellaCliente()['identificativo']}")
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

    def aggiungiParcella(self):
        pass

    def cercaParcella(self):
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
        from GestoreStudioLegale.Viste.VisteAvvocato.RicercaParcelle import RicercaParcelle
        self.vistaHome = RicercaParcelle()
        self.vistaHome.show()
        self.close()