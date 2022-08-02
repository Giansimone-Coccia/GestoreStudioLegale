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


    #non manca la creazione del corso? il nome? il codice?
    """
        def aggiungiCorso(self, crediti, ID, dataOraInizio, dataOraFine, tipo ):
        self.crediti = crediti
        self.ID = ID
        self.dataOraInizio = dataOraInizio
        self.dataOraFine = dataOraFine
        self.tipo = tipo
        
         if os.path.isfile('Dati\CorsiAggiornamento.pickle'):
            with open('Dati\CorsiAggiornamento.pickle', 'rb') as f:
                corsiAggiornamento = pickle.load(f)
            corsiAggiornamento[ID] = self
        with open('Dati\CorsiAggiornamento.pickle', 'wb') as f:
            pickle.dump(corsiAggiornamento, f, pickle.HIGHEST_PROTOCOL)
    """
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

    #codice?
    def ricercaCorsoCodice(self, codice):
        if os.path.isfile('Dati\CorsiAggiornamento.pickle'):
            with open('Dati\CorsiAggiornamento.pickle', 'rb') as f:
                corsiAggiornamento = dict(pickle.load(f))
                for corsiAggiornamento in corsiAggiornamento.values():
                    if corsiAggiornamento.codice == codice:
                        return corsoAggiornamento
                return None
        else:
            return None

    def ricercaCorsoNome(self, nome):
        if os.path.isfile('Dati\CorsiAggiornamento.pickle'):
            with open('Dati\CorsiAggiornamento.pickle', 'rb') as f:
                corsiAggiornamento = dict(pickle.load(f))
                for corsiAggiornamento in corsiAggiornamento.values():
                    if corsiAggiornamento.nome == nome:
                        return corsoAggiornamento
                return None
        else:
            return None

    def ricercaCorsoTipo(self, tipo):
        if os.path.isfile('Dati\CorsiAggiornamento.pickle'):
            with open('Dati\CorsiAggiornamento.pickle', 'rb') as f:
                corsiAggiornamento = dict(pickle.load(f))
                for corsiAggiornamento in corsiAggiornamento.values():
                    if corsiAggiornamento.tipo == tipo:
                        return corsoAggiornamento
                return None
        else:
            return None

    #il codice è l'ID? (id=int, codice=str)
    def rimuoviCorso (self, CorsoAggiornamento):
        if os.path.isfile('Dati\CorsiAggiornamento.pickle'):
            with open('Dati\CorsiAggiornamento.pickle', 'wb+') as f:
                corsiAggiornamento = dict(pickle.load(f))
                if self.ricercaUdienzaCodice(CorsoAggiornamento.codice()):
                    del corsiAggiornamento[self.ID]
                    pickle.dump(corsiAggiornamento, f, pickle.HIGHEST_PROTOCOL)


