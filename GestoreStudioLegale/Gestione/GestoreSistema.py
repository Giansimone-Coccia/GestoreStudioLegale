import pickle
import os.path

from PyQt5.QtWidgets import QMessageBox

from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Utilities.Utilities import Tools

class GestoreSistema:

    def __init__(self):
        self.listaAvvocati = []
        self.listaClienti = []

    def loginAdmin(self, pssw, user):
        tool =Tools()
        passEuser = tool.leggi('CredenzialiAdmin', 0).splitlines()
        print(passEuser)
        if pssw == passEuser[0] and user == passEuser[1]:
            return True
        self.failed()
        return False


    def loginAvvocato(self, pssw, codiceFiscale):
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                try:
                    avvocatiList = list(pickle.load(f))
                except EOFError as er:
                    self.problema()
        for avvocato in avvocatiList:
            if pssw == avvocato.getDatiAvvocato()['Password'] and codiceFiscale == avvocato.getDatiAvvocato()['Codice fiscale']:
                return True
        return False

    def loginCliente(self, pssw, codiceFiscale):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                try:
                    clientiList = list(pickle.load(f))
                except EOFError as er:
                    self.problema()
        for cliente in clientiList:
            if pssw == cliente.getDatiCliente()['Password'] and codiceFiscale == cliente.getDatiCliente()['Codice fiscale'] :
                return True
        return False




    def modificaCredenzialiAdmin(self, newPssw = '', newUser = ''):
        tool = Tools()
        if newPssw != '':
            tool.salvaAppend(newPssw,'CredenzialiAdmin')
        if newUser != '':
            tool.salvaAppend(newUser,'CredenzialiAdmin')


    def rimuoviAvvocato(self, avvocato = None):
        Avvocato.rimuoviAvvocato(avvocato.Id)


    def rimuoviCliente(self, cliente = None):
        Cliente.rimuoviCliente(cliente.Id)

    def salvaCliente(self, cliente):
        clienti = []
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            if os.path.getsize('GestoreStudioLegale/Dati/Clienti.pickle') == 0:
                clienti.append(cliente)
                with open('GestoreStudioLegale/Dati/Clienti.pickle', 'wb') as f:
                    pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
            else:
                if cliente.ricercaUtilizzatoreId(cliente.getDatiCliente()["Id"]) is None:
                    with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                        clienti = pickle.load(f)
                        clienti.append(cliente)
                    with open('GestoreStudioLegale/Dati/Clienti.pickle', 'wb') as f1:
                        pickle.dump(clienti, f1, pickle.HIGHEST_PROTOCOL)

    def problema(self):
        msg = QMessageBox()
        msg.setWindowTitle("Problema")
        msg.setText("Problema con lettura/scrittura file")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def failed(self):
        msg = QMessageBox()
        msg.setWindowTitle("Attenzione")
        msg.setText("Accesso non eseguito")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()