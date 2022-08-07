import pickle
import os.path
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Servizi.Avvocato import Avvocato

class GestoreSistema:

    def __init__(self):

        avvocati = []
        clienti = []
        self.listaAvvocati = []
        self.listaClienti = []

        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'rb') as f:
                try:
                    avvocati = pickle.load(f)
                    self.listaAvvocati.append(avvocati)
                except EOFError as er:
                        print("Errore")

        if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'rb') as f:
                try:
                    clienti = pickle.load(f)
                    self.listaClienti.append(clienti)
                except EOFError as er:
                    print("Errore")


    def aggiungiAvvocato(self, avvocato = None): #modifica

        self.listaAvvocati.append(avvocato)
        avvocati = []
        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'rb') as f:
                try:
                    avvocati = pickle.load(f)
                    avvocati.append(avvocato)
                except EOFError as er:
                    print("Errore")
        with open('Dati\Avvocati.pickle', 'wb') as f:
            pickle.dump(avvocati, f, pickle.HIGHEST_PROTOCOL)

    def aggiungiCliente(self, cliente = None):

        self.listaClienti.append(cliente)
        clienti=[]
        if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'rb') as f:
                try:
                    clienti = pickle.load(f)
                    clienti.append(cliente)
                except EOFError as er:
                    print("Errore")
        with open('Dati\Avvocati.pickle', 'wb') as f:
            pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    def rimuoviAvvocato(self, avvocato = None): #usa funzione di rimozione di avvocato

        self.listaAvvocati.remove(avvocato)
        Avvocato.rimuoviAvvocato(avvocato.Id)

    def rimuoviCliente(self, cliente = None):  #usa funzione di rimozione di cliente

        self.listaAvvocati.remove(cliente)
        Cliente.rimuoviCliente(cliente.Id)