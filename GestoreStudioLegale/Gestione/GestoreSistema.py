import pickle
import os.path
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Servizi.Avvocato import Avvocato

class GestoreSistema:

    def _init_(self):

        self.listaAvvocati = []
        self.listaClienti = []
        self.psswAmministratore = "password"
        self.userAmministratore = "admin"

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
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                try:
                    clientiList = pickle.load(f)
                    self.listaClienti.append(clientiList)
                    #print(self.listaClienti)
                except EOFError as er:
                    print("Errore")
        for cliente in clientiList:
            if pssw == cliente.getDatiCliente()['Password'] and codiceFiscale == cliente.getDatiCliente()['Codice fiscale'] :
                print("Accesso effetuato")
                print(cliente)
                return True
        print("Accesso fallito")


    def loginAvvocato(self, pssw, codiceFiscale): #da modificare in Ea
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                try:
                    avvocatiList = pickle.load(f)
                    self.listaAvvocati.append(avvocatiList)
                    #print(self.listaAvvocati)
                except EOFError as er:
                    print("Errore")
        for avvocato in avvocatiList:
            if pssw == avvocato.getDatiAvvocato()['Password'] and codiceFiscale == avvocato.getDatiAvvocato()['Codice fiscale']:
                print("Accesso effetuato")
                print(avvocato)
                return True
        print("Accesso fallito")


    def loginAdmin(self, pssw, user): #da modificare in Ea
            if pssw == self.psswAmministratore and user == self.userAmministratore:
                print("Accesso effetuato")
                return
            print("Accesso fallito")


    def modificaCredenzialiAdmin(self, newPssw = '', newUser = ''): #da modificare in Ea
        if newPssw != '':
            self.psswAmministratore = newPssw
        if newUser != '':
            self.userAmministratore = newUser
        print(self.psswAmministratore)
        print(self.userAmministratore)


    def rimuoviAvvocato(self, avvocato = None): #usa funzione di rimozione di avvocato
        Avvocato.rimuoviAvvocato(avvocato.Id)
        print("Fatto")


    def rimuoviCliente(self, cliente = None):  #usa funzione di rimozione di cliente
        Cliente.rimuoviCliente(cliente.Id)
        print("Fatto")