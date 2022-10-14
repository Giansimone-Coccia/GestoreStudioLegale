from __future__ import print_function

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QMainWindow, QScrollArea, QHBoxLayout
import pickle
import os

from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento
from GestoreStudioLegale.Utilities.Utilities import Tools

class VistaVisualizzaAppuntamento(QMainWindow):

    tool = Tools()
    clientiList = []
    appuntamentiList = []
    #clientiList = tool.loadClienti()

    def __init__(self, parent = None):
        super(VistaVisualizzaAppuntamento, self).__init__(parent)

        self.cWidget = QWidget()
        self.outerLayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.grifLayout = QGridLayout()
        self.outerLayout.addWidget(self.tool.rewindButton(self.rewindHomeCliente), 1)
        labelC = QLabel()
        labelC.setText('Cliente: ' + '\n' + 'NOME: ' + f"{self.getDatiC()['Nome']}" + '\n' + 'COGNOME: ' + f"{self.getDatiC()['Cognome']}" + '\n' + 'ID: ' + f"{self.getDatiC()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{self.getDatiC()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{self.getDatiC()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{self.getDatiC()['Numero telefono']}")
        self.outerLayout.addWidget(labelC, 0)
        labelC.setGeometry(QRect(0, 0, 350, 20))
        labelC.setFont(QFont('Arial', 10))
        labelC.setStyleSheet("border: 1px solid black;")
        self.outerLayout.addLayout(self.button_layout, 1)
        self.outerLayout.addWidget(self.scroll, 8)
        self.cWidget.setLayout(self.outerLayout)

        self.getDatiA()
        self.widget.setLayout(self.grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.cWidget)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(800, 600)
        self.setWindowTitle("Appuntamenti")
        self.show()

    def getDatiA(self):
        #self.clientiList = self.tool.loadClienti()
        self.appuntamentiList = self.tool.loadAppuntamenti()

        #self.clientiList = self.tool.loadClienti()
        i = 1
        appuntamentiL = []

        #for appuntamento in self.appuntamentiList:
            #print(appuntamento.Cliente.codiceFiscale) #STAMPA TUTTI GLI APPUNTAMENTI
            #print(self.getDatiC()['Codice fiscale'])
            #if appuntamento.Cliente.codiceFiscale == self.getDatiC()['Codice fiscale']:
        #for cliente in self.clientiList:
            #print(cliente.codiceFiscale)
            #print(str(self.tool.leggi(n=0)).rsplit()[0])


        for appuntamento in self.appuntamentiList:
            print(self.appuntamentiList)
            #if appuntamento.Cliente.Id == cliente.Id:
            #if appuntamento.Cliente.codiceFiscale == self.tool.leggi(n=0).rsplit()[0]:
            if appuntamento.Cliente.codiceFiscale == self.tool.leggi(n=0).rsplit()[0]:
            #if 'cc' == self.tool.leggi(n=0).rsplit()[0]:
               appuntamentiL.append(appuntamento)
               print("b")
               print("s")
            print(appuntamento.getDatiAppuntamento()['Cliente'])
        for app in appuntamentiL:
            #print(cliente.codiceFiscale)
            #print(appuntamento.Cliente.codiceFiscale)
            #print(type(cliente.codiceFiscale))
            #print(type(appuntamento.Cliente.codiceFiscale))
            #print("ciaoo3")
            label = QLabel()
            #print("ciaoo4")
            tool = Tools()
            nome = ""
            cognome = ""
            avvocatiList = tool.loadAvvocati()
            for avvocato in avvocatiList:
                for appuntamento in avvocato.appuntamentiAvvocato:
                    if appuntamento.ID == app.ID:
                        nome = avvocato.nome
                        cognome = avvocato.cognome

            if(nome !="" and cognome != ""):
                datIn = app.getDatiAppuntamento()['Data e Ora Inizio'].strftime("%m/%d/%Y, %H:%M:%S")
                datFin = app.getDatiAppuntamento()['Data e Ora Fine'].strftime("%m/%d/%Y, %H:%M:%S")
                label.setText(
                    'Appuntamento: ' + '\n' + 'TIPO PROCEDIMENTO: ' + f"{app.getDatiAppuntamento()['Tipo Procedimento']}" + '\n' + 'ID: ' + f"{app.getDatiAppuntamento()['ID']}" + '\n' + 'DATA E ORA INIZIO: ' + f"{datIn}" + '\n' + 'DATA E ORA FINE: ' + f"{datFin}" + '\n' + 'AVVOCATO: ' + f"{nome} {cognome}")
                label.setGeometry(QRect(0, 0, 350, 20))
                #label.setText(
                #   'Appuntamento: ' + '\n' + 'Data e ora inizio: ' + f"{appuntamento.dataOraInizio}" + '\n' + 'Data e ora fine: ' + f"{appuntamento.dataOraFine}" + '\n' + 'ID: ' + f"{appuntamento.ID}" + '\n' + 'Tipo procedimento: ' + f"{appuntamento.tipoProcedimento}")
                label.setFont(QFont('Arial', 10))
                label.setStyleSheet("border: 1px solid black;")
                #print("ciaoo5")
                self.grifLayout.addWidget(label, i, 1, 1, 2)
                #print("ciao78")
                i += 1
            print("ciao89")

    def getDatiC(self):
        clientiList = self.tool.loadClienti()
        for cliente in clientiList:
            if cliente.codiceFiscale == str(self.tool.leggi(n=0)).rsplit()[0]:
                return cliente.getDatiCliente()

    def rewindHomeCliente(self):
        from GestoreStudioLegale.Viste.VisteCliente.VistaHomeAppuntamentiC import VistaHomeAppuntamentiC
        self.vistaHome = VistaHomeAppuntamentiC()
        self.vistaHome.show()
        self.close()

    def getNum(self):
        n = 0
        self.appuntamentiList = self.tool.loadAppuntamenti()
        for appuntamento in self.appuntamentiList:
            n+=1
        return n