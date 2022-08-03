import datetime

import pickle
import os.path

class CorsoAggiornamento:

    def __init__(self):
       self.nome = ''
       self.crediti = 0
       self.ID = '' #mettilo stringa in ea
       self.dataOraInizio = datetime.datetime(year=1970, month=1, day=1, hour=00, minute=00)
       self.dataOraFine = datetime.datetime(year=1970, month=1, day=1, hour=00, minute=00)
       self.tipo = ''

    def creaCorso(self, nome, crediti, ID, dataOraInizio, dataOraFine, tipo ): #modifica in ea
        self.nome = nome
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


    def getDatiCorso(self):
        return {
            'Nome': self.nome,
            'Crediti': self.crediti,
            'ID': self.ID,
            'Data e Ora Inizio': self.dataOraInizio,
            'Data e Ora Fine': self.dataOraFine,
            'Tipo Corso': self.tipo,
        }


    def ricercaCorsoCodice(self, ID):
        if os.path.isfile('Dati\CorsiAggiornamento.pickle'):
            with open('Dati\CorsiAggiornamento.pickle', 'rb') as f:
                corsiAggiornamento = dict(pickle.load(f))
                for corsoAggiornamento in corsiAggiornamento.values():
                    if corsoAggiornamento.ID == ID:
                        return corsoAggiornamento
                return None
        else:
            return None

    def ricercaCorsoNome(self, nome): #aggiungi la variabile nome in ea
        if os.path.isfile('Dati\CorsiAggiornamento.pickle'):
            with open('Dati\CorsiAggiornamento.pickle', 'rb') as f:
                corsiAggiornamento = dict(pickle.load(f))
                for corsoAggiornamento in corsiAggiornamento.values():
                    if corsoAggiornamento.nome == nome:
                        return corsoAggiornamento
                return None
        else:
            return None

    def ricercaCorsoTipo(self, tipo):
        if os.path.isfile('Dati\CorsiAggiornamento.pickle'):
            with open('Dati\CorsiAggiornamento.pickle', 'rb') as f:
                corsiAggiornamento = dict(pickle.load(f))
                for corsoAggiornamento in corsiAggiornamento.values():
                    if corsoAggiornamento.tipo == tipo:
                        listaCorsi = [corsoAggiornamento]
                return listaCorsi
            return None
        else:
            return None

    def rimuoviCorso (self, CorsoAggiornamento):
        if os.path.isfile('Dati\CorsiAggiornamento.pickle'):
            with open('Dati\CorsiAggiornamento.pickle', 'wb+') as f:
                corsiAggiornamento = dict(pickle.load(f))
                if self.ricercaUdienzaCodice(CorsoAggiornamento.codice()):
                    del corsiAggiornamento[self.ID]
                    pickle.dump(corsiAggiornamento, f, pickle.HIGHEST_PROTOCOL)