import pickle
import os.path
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Servizi.Avvocato import Avvocato

class GestoreSistema:

    def __init__(self):

        self.listaAvvocati = []
        self.listaClienti = []
        self.psswAmministratore = "password"
        self.userAmministratore = "admin"

        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                try:
                    avvocati = pickle.load(f)
                    self.listaAvvocati.append(avvocati)
                    print(self.listaAvvocati)
                except EOFError as er:
                        print("Errore")


        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                try:
                    clienti = pickle.load(f)
                    self.listaClienti.append(clienti)
                    print(self.listaClienti)
                except EOFError as er:
                    print("Errore")


    def loginCliente(self, pssw, codiceFiscale): #da modificare in Ea
        for cliente in self.listaClienti:
            if pssw is cliente.getDatiCliente()['Password'] and codiceFiscale is cliente.getDatiCliente()['Codice fiscale'] :
                print("Accesso effetuato")
                return
        print("Accesso fallito")


    def loginAvvocato(self, pssw, codiceFiscale): #da modificare in Ea
        for avvocato in self.listaAvvocati:
            if pssw == avvocato.getDatiAvvocato()['Password'] and codiceFiscale == avvocato.getDatiAvvocato()['Codice fiscale']:
                print("Accesso effetuato")
                return
        print("Accesso fallito")


    def loginAdmin(self, pssw, user): #da modificare in Ea
            if pssw == self.psswAmministratore and user == self.userAmministratore:
                print("Accesso effetuato")
                return
            print("Accesso fallito")


    def modificaCredenzialiAdmin(self,newPssw,newUser): #da modificare in Ea
        self.psswAmministratore = newPssw
        self.userAmministratore = newUser


    def rimuoviAvvocato(self, avvocato = None): #usa funzione di rimozione di avvocato

        self.listaAvvocati.remove(avvocato)
        Avvocato.rimuoviAvvocato(avvocato.Id)


    def rimuoviCliente(self, cliente = None):  #usa funzione di rimozione di cliente

        self.listaAvvocati.remove(cliente)
        Cliente.rimuoviCliente(cliente.Id)