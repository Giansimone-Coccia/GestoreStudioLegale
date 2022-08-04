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


    def aggiungiAvvocato(self, Avvocato = None): #modifica

        self.listaAvvocati.append(Avvocato)
        avvocati = {}
        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'rb') as f:
                avvocati = pickle.load(f)
        avvocati[Avvocato.id] = Avvocato
        with open('Dati\Avvocati.pickle', 'wb') as f:
            pickle.dump(avvocati, f, pickle.HIGHEST_PROTOCOL)

    def aggiungiCliente(self, cliente):

        self.listaClienti.append(cliente)
        clienti={}
        if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        clienti[cliente.getInfoUtilizzatore()['id']] = cliente
        with open('Dati\Avvocati.pickle', 'wb') as f:
            pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    def rimuoviAvvocato(self, avvocato): #usa funzione di rimozione di avvocato

        self.listaAvvocati.remove(avvocato)
        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'wb+') as f:
                avvocati = dict(pickle.load(f))
                if avvocato in avvocati :
                    del avvocati[avvocato.getInfoUtilizzatore()['id']]
                    pickle.dump(avvocati, f, pickle.HIGHEST_PROTOCOL)

    def rimuoviCliente(self, cliente):  #usa funzione di rimozione di cliente

        self.listaAvvocati.remove(cliente)
        if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'wb+') as f:
                clienti = dict(pickle.load(f))
                if cliente in clienti :
                    del clienti[cliente.getInfoUtilizzatore()['id']]
                    pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)