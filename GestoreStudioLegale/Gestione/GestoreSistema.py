import pickle
import os.path
from Servizi.Avvocato import Avvocato
from Servizi.Cliente import Cliente

class Statistiche:

    def __init__(self):
        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'rb') as f:
                avvocati = dict(pickle.load(f))
                self.listaAvvocati = avvocati



        if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                self.listClienti = clienti


    def aggiungiAvvocato(self, avvocato):
        self.listaAvvocati.append(avvocato)
        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'rb') as f:
                avvocati = pickle.load(f)

        with open('Dati\Avvocati.pickle', 'wb') as f:
            pickle.dump(avvocati, f, pickle.HIGHEST_PROTOCOL)

    def aggiungiCliente(self, cliente):
        self.listaClienti.append(cliente)
        clienti={}
        if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        clienti[Id] = Cliente
        with open('Dati\Avvocati.pickle', 'wb') as f:
            pickle.dump(avvocati, f, pickle.HIGHEST_PROTOCOL)