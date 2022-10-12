from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QMainWindow, QScrollArea, QHBoxLayout
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Servizi.Cliente import Cliente


#modificare dimensioni tasti in utilities
from GestoreStudioLegale.Viste.VisteAvvocato.VistaEliminaUdienze import VistaEliminaUdienze
from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeUdienze import VistaHomeUdienze


class UdienzaRicercata(QMainWindow):

    udienzeList = []
    avvocatiList = []
    clientiList = []
    tool = Tools()

    def __init__(self, udienze,parent=None):
        super(UdienzaRicercata, self).__init__(parent)

        self.udienzeTrovate = []
        print("ciaoo45")
        for u in udienze:
            self.udienzeTrovate.append(u)
            #self.udienzeList.append(u)

        self.cWidget = QWidget()  # contiene tutto
        self.outerLayout = QVBoxLayout()
        #self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box

        self.grifLayout = QGridLayout()

        self.outerLayout.addWidget(self.tool.rewindButton(self.rewind1), 1)
        #self.outerLayout.addLayout(self.button_layout, 1)
        self.outerLayout.addWidget(self.scroll, 9)
        #self.button_layout.addWidget(self.tool.createButton("Inserisci", self.aggiungiUdienza))
        #self.button_layout.addWidget(self.tool.createButton("Cerca", self.cercaUdienza))
        self.cWidget.setLayout(self.outerLayout)

        self.getDatiU()
        self.widget.setLayout(self.grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        #self.setCentralWidget(self.scroll)
        self.setCentralWidget(self.cWidget)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(800, 600)
        self.setWindowTitle("Udienze")
        self.show()

    def getDatiU(self):
        self.udienzeList = self.tool.loadUdienze()
        self.avvocatiList = self.tool.loadAvvocati()
        self.clientiList = self.tool.loadClienti()
        tool = Tools()
        ud = []
        #clientiL = []
        i=1

        '''
        for avvocato in self.avvocatiList:
            if avvocato.codiceFiscale == self.tool.leggi().rsplit()[0]:
               clienti = avvocato.getDatiAvvocato()['clienti']
               #for cliente in self.clientiList:
               for cliente in clienti:
                   for udienza in self.udienzeList:
                      if udienza.Cliente.codiceFiscale == cliente.codiceFiscale:
                         #ud.append(udienza)
                         print("ciao24")
                         ud.append(udienza)
                         print("ciao25")
                         #break
                         #print(self.udienzeList)                     #CRUSHA NON FUNZIONA
                         #print(self.udienzeList.__getitem__(3))
                         #print(ud)
        print("ciao26")
        '''

        #for u in self.udienzeTrovate:
        for u in self.udienzeTrovate:
            print("hei bro")
            label = QLabel()
            #print(u)
            textLabel2 = QLabel()
            print(u.getDatiUdienza()['Cliente'].getDatiCliente()['Nome'])
            print("tra i due clienti")
            textLabel2.setText(
                'Cliente: ' + '\n' + 'NOME: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Nome']}" + '\n' + 'COGNOME: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Cognome']}" + '\n' + 'ID: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Numero telefono']}")
            textLabel2.setGeometry(QRect(0, 0, 350, 20))
            textLabel2.setFont(QFont('Arial', 10))
            textLabel2.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(textLabel2, i, 1, 1,2)
            i += 1
            dataIn = u.getDatiUdienza()['Data e Ora Inizio'].strftime("%m/%d/%Y, %H:%M:%S")
            dataFin = u.getDatiUdienza()['Data e Ora Fine'].strftime("%m/%d/%Y, %H:%M:%S")
            label.setText(
                #'Udienza: ' + '\n' + 'CITTA TRIBUNALE: ' + f"{u.getDatiUdienza()['Città Tribunale']}" + '\n' + 'TIPO TRIBUNALE: ' + f"{u.getDatiUdienza()['Tipo Tribunale']}" + '\n' + 'ID: ' + f"{u.getDatiUdienza()['ID']}" + '\n' + 'DATA ORA INIZIO: ' + f"{dataIn}" + '\n' + 'DATA ORA FINE: ' + f"{dataFin}")
               'Udienza: ' + '\n' + 'CITTA TRIBUNALE: ' + f"{u.getDatiUdienza()['Città Tribunale']}" + '\n' + 'TIPO TRIBUNALE: ' + f"{u.getDatiUdienza()['Tipo Tribunale']}" + '\n' + 'ID: ' + f"{u.getDatiUdienza()['ID']}" + '\n' + 'DATA ORA INIZIO: ' + f"{u.getDatiUdienza()['Data e Ora Inizio']}" + '\n' + 'DATA ORA FINE: ' + f"{u.getDatiUdienza()['Data e Ora Fine']}")

            label.setGeometry(QRect(0, 0, 350, 20))
            label.setFont(QFont('Arial', 10))
            label.setStyleSheet("border: 1px solid black;")
            print("ciao2054")
            self.grifLayout.addWidget(label,i,1,1,2)
            i += 1
            self.grifLayout.addWidget(tool.createButton("Modifica", lambda checked,  a = u: self.aggiornaUdienza(a)), i, 1)
            self.grifLayout.addWidget(
                tool.createButton("Elimina", lambda checked, a = u.getDatiUdienza()['ID']: self.rimuoviUdienza(a)),i,2)
            i += 1
            print("ecco ciao9")

    def aggiungiUdienza(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaIserisciUdienza import VistaInserisciUdienza
        self.vistaInserimento = VistaInserisciUdienza()
        self.vistaInserimento.show()
        self.close()

    def aggiornaUdienza(self, udienza):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaAggiornaUdienza import VistaAggiornaUdienza
        self.vistaAggiorna = VistaAggiornaUdienza()
        self.vistaAggiorna.udienza = udienza
        self.vistaAggiorna.show()
        self.close()

    def rimuoviUdienza(self, id):
        self.subWindow = VistaEliminaUdienze()
        self.subWindow.setData(id)
        self.subWindow.show()
        self.close()

    def cercaUdienza(self):
        pass

    def getDatiC(self):
        self.clientiList = self.tool.loadClienti()
        tool = Tools()
        print("ngul a mammt")
        print(tool.leggi())
        for cliente in self.clientiList:
            if cliente.codiceFiscale == str(tool.leggi()).rsplit()[0]:
                    return cliente.getDatiCliente()

    def rewind1(self):
        self.vistaHome = VistaHomeUdienze()
        self.vistaHome.show()
        self.close()