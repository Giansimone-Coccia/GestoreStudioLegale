import pickle
import os.path
import datetime
import os

class Backup():

    def __init__(self):
        self.data = datetime.datetime(year=1970, month=1, day=1)
        self.frequenza = 24

    def eseguiBackuo(self): # da vedere
        file_path = 'Dati\Backup.pickle'
        os.remove(file_path)
        self.salvaDatiAppuntamento()
        self.salvaDatiParcella()
        self.salvaDatiCorsoAggiornamento()
        self.salvaDatiUtilizzatore()

    def modificaData(self, nuovaData): #ricorda su enterprise
        self.data=nuovaData

    def modificaFrequenza(self, nuovaFrequenza):  #ricorda su enterprise
        self.frequenza=nuovaFrequenza

    def salvaDatiAppuntamento(self):
        if os.path.isfile('Dati\Appuntamenti.pickle'):
            with open('Dati\Appuntamenti.pickle', 'rb') as f:
                appuntamenti = pickle.load(f)
        with open('Dati\Backup.pickle', 'wb') as f:
            pickle.dump(appuntamenti, f, pickle.HIGHEST_PROTOCOL)

    def salvaDatiParcella(self):
        if os.path.isfile('Dati\Parcelle.pickle'):
            with open('Dati\Parcelle.pickle', 'rb') as f:
                parcelle = pickle.load(f)
        with open('Dati\Backup.pickle', 'wb') as f:
            pickle.dump(parcelle, f, pickle.HIGHEST_PROTOCOL)

    def salvaDatiUtilizzatore(self):
        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'rb') as f:
                avvocati = pickle.load(f)
        with open('Dati\Backup.pickle', 'wb') as f:
            pickle.dump(avvocati, f, pickle.HIGHEST_PROTOCOL)

            if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        with open('Dati\Backup.pickle', 'wb') as f:
            pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    def salvaDatiCorsoAggiornamento(self):
        if os.path.isfile('Dati\Parcelle.pickle'):
            with open('Dati\CoriDiAggiornamento.pickle', 'rb') as f:
                corsiDiAggiornamento = pickle.load(f)
        with open('Dati\Backup.pickle', 'wb') as f:
            pickle.dump(corsiDiAggiornamento, f, pickle.HIGHEST_PROTOCOL)