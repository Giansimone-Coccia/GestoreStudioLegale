import datetime

import pickle
import os.path

class CorsoAggiornamento:

    def __init__(self):
       self.crediti = 0
       self.ID = 0
       self.dataOraInizio = datetime.datetime(year=1970, month=1, day=1, hour=00, minute=00)
       self.dataOraFine = datetime.datetime(year=1970, month=1, day=1, hour=00, minute=00)
       self.tipo = []


    #non dovrebbe avere un ID?
    def aggiungiCorso(self):
        if os.path.isfile('Dati\CorsiAggiornamento.pickle'):
            with open('Dati\CorsiAggiornamento.pickle', 'rb') as f:
                corsiAggiornamento = pickle.load(f)
            corsiAggiornamento[ID] = self
        with open('Dati\CorsiAggiornamento.pickle', 'wb') as f:
            pickle.dump(corsiAggiornamento, f, pickle.HIGHEST_PROTOCOL)

    def getDatiCorso(self):
        return {
            'Crediti': self.crediti,
            'ID': self.ID,
            'Data e Ora Inizio': self.dataOraInizio,
            'Data e Ora Fine': self.dataOraFine,
            'Tipo Corso': self.tipo,
        }

    def