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

        corsi = []

        if os.path.isfile('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle'):
            if os.path.getsize('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle') == 0:
                corsi.append(self)
                with open('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle', 'wb') as f1:
                    pickle.dump(corsi, f1, pickle.HIGHEST_PROTOCOL)
            else:
                if self.ricercaCorsoCodice(self.ID) is None:
                    with open('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle', 'rb') as f:
                        corsi = pickle.load(f)
                        corsi.append(self)
                    with open('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle', 'wb') as f1:
                        pickle.dump(corsi, f1, pickle.HIGHEST_PROTOCOL)


    def getDatiCorso(self):
        d = {}
        d['Nome'] = self.nome
        d['Crediti'] = self.crediti
        d['ID'] = self.ID
        d['Data e Ora Inizio'] = self.dataOraInizio
        d['Data e Ora Fine'] = self.dataOraFine
        d['Tipo Corso'] = self.tipo
        return d


    def ricercaCorsoCodice(self, ID):
        if os.path.isfile('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle'):
            with open('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle', 'rb') as f:
                corsiAggiornamento = dict(pickle.load(f))
                for corsoAggiornamento in corsiAggiornamento.values():
                    if corsoAggiornamento.ID == ID:
                        return corsoAggiornamento
                return None
        else:
            return None

    def ricercaCorsoNome(self, nome): #aggiungi la variabile nome in ea
        if os.path.isfile('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle'):
            with open('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle', 'rb') as f:
                corsiAggiornamento = dict(pickle.load(f))
                for corsoAggiornamento in corsiAggiornamento.values():
                    if corsoAggiornamento.nome == nome:
                        return corsoAggiornamento
                return None
        else:
            return None

    def ricercaCorsoTipo(self, tipo):
        listaCorsi = []
        if os.path.isfile('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle'):
            with open('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle', 'rb') as f:
                corsiAggiornamento = dict(pickle.load(f))
                for corsoAggiornamento in corsiAggiornamento.values():
                    if corsoAggiornamento.tipo == tipo:
                        listaCorsi.append(corsoAggiornamento)
                return listaCorsi
            return None
        else:
            return None

    @staticmethod
    def rimuoviCorso (CorsoAggiornamento):
        try:
            corsi = []
            if os.path.isfile('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle'):
                with open('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle', 'rb') as f:
                    corsi = pickle.load(f)
            for corso in corsi:
                if corso.ID == ID:
                    corsi.remove(corso)
                else:
                    print("Corso non trovato")
            with open('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle', 'wb') as f1:
                pickle.dump(corsi, f1, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            print("Finito")