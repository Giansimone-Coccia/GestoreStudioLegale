import pickle
import os.path
from Servizi.Avvocato import Avvocato
from Servizi.Cliente import Cliente

class GestoreSistema:

    def __init__(self):
        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'rb') as f:
                avvocati = dict(pickle.load(f))
                self.listaAvvocati = []
                self.listaAvvocati.append(avvocati.values())

        if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                self.listClienti = []
                self.listClienti.append(clienti.values())

    def aggiungiAvvocato(self, avvocato):
        self.listaAvvocati.append(avvocato)
        avvocati={}
        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'rb') as f:
                avvocati = pickle.load(f)
        avvocati[avvocato.getInfoUtilizzatore()['id']]=avvocato
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

    def rimuoviAvvocato(self, avvocato):
        self.listaAvvocati.remove(avvocato)
        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'wb+') as f:
                avvocati = dict(pickle.load(f))
                if avvocato in avvocati :
                    del avvocati[avvocato.getInfoUtilizzatore()['id']]
                    pickle.dump(avvocati, f, pickle.HIGHEST_PROTOCOL)

    def rimuoviCliente(self, cliente):  # Effettuo una ricerca tramite Id
        self.listaAvvocati.remove(cliente)
        if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'wb+') as f:
                clienti = dict(pickle.load(f))
                if cliente in clienti :
                    del clienti[cliente.getInfoUtilizzatore()['id']]
                    pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)