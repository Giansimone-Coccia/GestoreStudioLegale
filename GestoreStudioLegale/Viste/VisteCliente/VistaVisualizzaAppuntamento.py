from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaVisualizzaAppuntamento(QWidget):

    appuntamentiList = []
    clientiList = []

    def __init__(self, parent=None):
        super(VistaVisualizzaAppuntamento, self).__init__(parent)
        tool = Tools()
        grifLayout = QGridLayout()
        grifLayout.addWidget(tool.rewindButton(self.rewindHomeCliente), 0, 0)
        textLabel1 = QLabel()
        textLabel2 = QLabel()
        textLabel1.setText("Di seguito la lista degli appuntamenti con le informazioni relative al cliente")
        textLabel1.setGeometry(QRect(0, 0, 200, 150))
        textLabel1.setFont(QFont('Arial', 10))
        textLabel2.setText(
            'Cliente: ' + '\n' + 'NOME: ' + f"{self.getDatiC()['Nome']}" + '\n' + 'COGNOME: ' + f"{self.getDatiC()['Cognome']}" + '\n' + 'ID: ' + f"{self.getDatiC()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{self.getDatiC()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{self.getDatiC()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{self.getDatiC()['Numero telefono']}")
        textLabel2.setGeometry(QRect(0, 0, 350, 10))
        textLabel2.setFont(QFont('Arial', 10))
        textLabel2.setStyleSheet("border: 1px solid black;")
        textLabel3 = QLabel()
        print("ciao3")
        textLabel3.setText(
            'Appuntamento: '+'\n'+ 'TIPO PROCEDIMENTO: '+f"{self.getDatiA()['Tipo Procedimento']}"+'\n'+'ID: '+f"{self.getDatiA()['ID']}"+'\n'+'DATA E ORA INIZIO: '+f"{self.getDatiA()['Data e Ora Inizio']}"+'\n'+'DATA E ORA FINE'+f"{self.getDatiA()['Data e Ora Fine']}")
        textLabel3.setGeometry(QRect(0, 0, 350, 20))
        textLabel3.setFont(QFont('Arial', 10))
        print("ciao90")
        textLabel2.setText('Cliente: '+'\n'+ 'NOME: '+f"{self.getDatiC()['Nome']}"+ '\n'+'COGNOME: '+f"{self.getDatiC()['Cognome']}"+'\n'+'ID: '+f"{self.getDatiC()['Id']}"+'\n'+'CODICE FISCALE: '+f"{self.getDatiC()['Codice fiscale']}"+'\n'+'EMAIL: '+f"{self.getDatiC()['Email']}"+'\n'+'NUMERO TELEFONO: '+f"{self.getDatiC()['Numero telefono']}")
        textLabel2.setGeometry(QRect(0, 0, 350, 10))
        textLabel2.setFont(QFont('Times', 10))
        textLabel2.setStyleSheet("border: 1px solid black;")
        textLabel3 = QLabel()
        textLabel3.setText('Appuntamento: '+'\n'+ 'TIPO PROCEDIMENTO: '+f"{self.getDatiA()['Tipo Procedimento']}"+'\n'+'ID: '+f"{self.getDatiA()['ID']}")
        textLabel3.setGeometry(QRect(0, 0, 350, 20))
        textLabel3.setFont(QFont('Arial', 10))
        textLabel3.setStyleSheet("border: 1px solid black;")
        grifLayout.addWidget(textLabel2, 1, 1)
        grifLayout.addWidget(textLabel1, 2, 1)
        grifLayout.addWidget(textLabel3, 3, 1)
        self.setLayout(grifLayout)
        self.resize(500, 400)
        self.setWindowTitle("Appuntamenti")
        self.show()

    def loadDateA(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
            with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'rb') as f:
                self.appuntamentiList = list(pickle.load(f))

    def loadDateC(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                self.clientiList = list(pickle.load(f))

    def getDatiA(self):
        self.loadDateA()
        tool = Tools()
        for appuntamento in self.appuntamentiList:
            if appuntamento.ID == str(tool.leggi):
                return appuntamento.getDatiAppuntamento()
            #print(appuntamento.Cliente.Id)
            for appuntamento1 in self.getDatiC()['appuntamentoCliente']:
               if appuntamento1 == appuntamento:
                  return appuntamento.getDatiAppuntamento()


    def getDatiC(self):
        self.loadDateC()
        tool = Tools()
        for cliente in self.clientiList:
            print("ciao1")
            #print(self.clientiList)
            #print(cliente.codiceFiscale)
            if str(cliente.codiceFiscale) == str(tool.leggi()):
            #print(tool.leggi())
            #if 'cc' == str(tool.leggi()):
                print('fatto')
                #print(cliente.codiceFiscale)
            if cliente.codiceFiscale == str(tool.leggi()).rsplit()[0]:
                #if cliente.codiceFiscale == str(tool.leggi(n=0)).rsplit()[0]:
                print('fuck')
                return cliente.getDatiCliente()

    def rewindHomeCliente(self):
        from GestoreStudioLegale.Viste.VisteCliente.VistaHomeAppuntamentiC import VistaHomeAppuntamentiC
        self.vistaHome = VistaHomeAppuntamentiC()
        self.vistaHome.show()
        self.close()

    def getNum(self):
        n = 0
        self.loadDateA()
        for appuntamento in self.appuntamentiList:
            n+=1
        return n