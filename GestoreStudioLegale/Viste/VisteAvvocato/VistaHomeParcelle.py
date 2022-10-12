from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QMainWindow, QScrollArea, QHBoxLayout
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Servizi.Cliente import Cliente

#modificare dimensioni tasti in utilities
from GestoreStudioLegale.Viste.VisteAvvocato.VistaEliminaParcelle import VistaEliminaParcelle


class VistaHomeParcelle(QMainWindow):

    parcelleList = []
    avvocatiList = []
    clientiList = []
    tool = Tools()

    def __init__(self, parent=None):
        super(VistaHomeParcelle, self).__init__(parent)
        tool = Tools()

        self.cWidget = QWidget()  # contiene tutto
        self.outerLayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box

        self.grifLayout = QGridLayout()

        self.outerLayout.addWidget(tool.rewindButton(self.rewind1), 1)
        self.outerLayout.addLayout(self.button_layout, 1)
        self.outerLayout.addWidget(self.scroll, 8)
        self.button_layout.addWidget(tool.createButton("Inserisci", self.aggiungiParcella))
        self.button_layout.addWidget(tool.createButton("Cerca", self.cercaParcella))
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
        parc = []
        i=1

        for avvocato in self.avvocatiList:
            if avvocato.codiceFiscale == self.tool.leggi().rsplit()[0]:
               clienti = avvocato.getDatiAvvocato()['clienti']
               for cliente in clienti:
                    for parcella in self.parcelleList:
                        if parcella.Cliente.codiceFiscale == cliente.codiceFiscale:
                            parc.append(parcella)
                            print(parc)
        for p in parc:
            label = QLabel()
            textLabel2 = QLabel()
            textLabel2.setText(
                'Cliente: ' + '\n' + 'NOME: ' + f"{p.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Nome']}" + '\n' + 'COGNOME: ' + f"{p.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Cognome']}" + '\n' + 'ID: ' + f"{p.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{p.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{p.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{p.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Numero telefono']}")
            textLabel2.setGeometry(QRect(0, 0, 350, 20))
            textLabel2.setFont(QFont('Arial', 10))
            textLabel2.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(textLabel2, i, 1, 1, 2)
            i += 1
            label.setText(
                'Parcella: '+'\n'+ 'INTESTATARIO: '+f"{p.getDatiParcellaCliente()['intestatario']}"+ '\n'+'IMPORTO: '+f"{p.getDatiParcellaCliente()['importo']}"+'€'+'\n'+'ID: '+f"{p.getDatiParcellaCliente()['ID']}"+'\n'+'IDENTIFICATIVO: '+f"{p.getDatiParcellaCliente()['identificativo']}")
            label.setGeometry(QRect(0, 0, 350, 20))
            label.setFont(QFont('Arial', 10))
            label.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(label,i,1,1,2)
            i += 1
            #self.grifLayout.addWidget(tool.createButton("Modifica", self.aggiornaParcella), i, 1)
            self.grifLayout.addWidget(self.tool.createButton("Modifica", lambda checked,  a = p: self.aggiornaParcella(a)), i, 1)
            self.grifLayout.addWidget(
                self.tool.createButton("Elimina", lambda checked, a = p.getDatiParcellaCliente()['ID']: self.rimuoviParcella(a)),i,2)
            i += 1

    def aggiungiParcella(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaInserisciParcellaA import VistaInserisciParcellaA
        self.aggiunta = VistaInserisciParcellaA()
        self.aggiunta.show()
        self.close()

    def cercaParcella(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.RicercaParcelle import RicercaParcelle
        self.vistaAvvocatoR = RicercaParcelle()
        self.vistaAvvocatoR.show()
        self.close()

    def aggiornaParcella(self, parcella):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaAggiornaParcella import VistaAggiornaParcella
        self.vistaAggiorna = VistaAggiornaParcella()
        self.vistaAggiorna.parcella = parcella
        self.vistaAggiorna.show()
        self.close()

    def rimuoviParcella(self, id):
        self.subWindow = VistaEliminaParcelle()
        self.subWindow.setData(id)
        self.subWindow.show()
        self.close()

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
