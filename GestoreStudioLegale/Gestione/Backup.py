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
        appuntamenti = []
        if os.path.isfile('Dati\Appuntamenti.pickle'):
            with open('Dati\Appuntamenti.pickle', 'rb') as f:
                try:
                    appuntamenti = pickle.load(f)
                except EOFError as er:
                    print("Errore")
        with open('Dati\Backup.pickle', 'wb') as f:
            pickle.dump(appuntamenti, f, pickle.HIGHEST_PROTOCOL)

    def salvaDatiParcella(self):
        parcelle = []
        if os.path.isfile('Dati\Parcelle.pickle'):
            with open('Dati\Parcelle.pickle', 'rb') as f:
                try:
                    parcelle = pickle.load(f)
                except EOFError as er:
                    print("Errore")
        with open('Dati\Backup.pickle', 'wb') as f:
            pickle.dump(parcelle, f, pickle.HIGHEST_PROTOCOL)

    def salvaDatiUtilizzatore(self):
        avvocati = []
        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'rb') as f:
                try:
                    avvocati = pickle.load(f)
                except EOFError as er:
                    print("Errore")
        with open('Dati\Backup.pickle', 'wb') as f:
            pickle.dump(avvocati, f, pickle.HIGHEST_PROTOCOL)

        clienti=[]
        if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'rb') as f:
                try:
                    clienti = pickle.load(f)
                except EOFError as er:
                    print("Errore")
        with open('Dati\Backup.pickle', 'wb') as f:
            pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    def salvaDatiCorsoAggiornamento(self):
        corsiDiAggiornamento = []
        if os.path.isfile('Dati\Parcelle.pickle'):
            with open('Dati\CoriDiAggiornamento.pickle', 'rb') as f:
                try:
                    corsiDiAggiornamento = pickle.load(f)
                except EOFError as er:
                    print("Errore")
        with open('Dati\Backup.pickle', 'wb') as f:
            pickle.dump(corsiDiAggiornamento, f, pickle.HIGHEST_PROTOCOL)