import pickle
import os.path
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Utilities.Utilities import Tools

class GestoreSistema:

    def _init_(self):

        self.listaAvvocati = []
        self.listaClienti = []
        '''self.psswAmministratore = "password"
        self.userAmministratore = "admin"'''



        '''if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                try:
                    avvocati = pickle.load(f)
                    self.listaAvvocati.append(avvocati)
                    print(self.listaAvvocati)
                except EOFError as er:
                        print("Errore")'''


        '''if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                try:
                    clienti = pickle.load(f)
                    self.listaClienti.append(clienti)
                    print(self.listaClienti)
                except EOFError as er:
                    print("Errore")'''


    def loginCliente(self, pssw, codiceFiscale): #da modificare in Ea
        print("shit")
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                try:
                    print("7777")
                    clientiList = list(pickle.load(f))
                    #self.listaClienti.append(clientiList)
                    print("9866")

                    #print(self.listaClienti)
                except EOFError as er:
                    print("Errore")
        for cliente in clientiList:
            if pssw == cliente.getDatiCliente()['Password'] and codiceFiscale == cliente.getDatiCliente()['Codice fiscale'] :
                print("Accesso effetuato")
                #print(cliente)
                return True
        print("Accesso fallito")
        return False


    def loginAvvocato(self, pssw, codiceFiscale): #da modificare in Ea
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                try:
                    avvocatiList = list(pickle.load(f))
                    #self.listaAvvocati.append(avvocatiList)
                    #print(self.listaAvvocati)
                except EOFError as er:
                    print("Errore")
        for avvocato in avvocatiList:
            if pssw == avvocato.getDatiAvvocato()['Password'] and codiceFiscale == avvocato.getDatiAvvocato()['Codice fiscale']:
                print("Accesso effetuato")
                #print(avvocato)
                return True
        print("Accesso fallito")
        return False


    def loginAdmin(self, pssw, user):#modifica in ea
        tool =Tools()
        passEuser = tool.leggi('CredenzialiAdmin', 0).splitlines()
        print(passEuser)
        if pssw == passEuser[0] and user == passEuser[1]:
            print("Accesso effetuato")
            return True
        print("Accesso fallito")
        return False




    def modificaCredenzialiAdmin(self, newPssw = '', newUser = ''): #da modificare in Ea
        tool = Tools()
        if newPssw != '':
            tool.salvaAppend(newPssw,'CredenzialiAdmin')
        if newUser != '':
            tool.salvaAppend(newUser,'CredenzialiAdmin')
        print(newPssw)
        print(newUser)


    def rimuoviAvvocato(self, avvocato = None): #usa funzione di rimozione di avvocato
        Avvocato.rimuoviAvvocato(avvocato.Id)
        print("Fatto")


    def rimuoviCliente(self, cliente = None):  #usa funzione di rimozione di cliente
        Cliente.rimuoviCliente(cliente.Id)
        print("Fatto")