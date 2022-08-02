import datetime

import Cliente
import pickle
import os.path

class Appuntamento():

    def __init__(self):
       self.Cliente = Cliente
       self.ID = []
       self.dataOraFine = datetime.datetime(year=1970 ,month=1 , day=1 , hour=00 , minute=00 )
       self.dataOraInizio = datetime.datetime (year=1970 ,month=1 , day=1 , hour=00 , minute=00 )
       self.tipoProcedimento = ''

    def aggiornaAppuntamento

    def creaAppuntamento(self, Cliente, dataOraInizio, dataOraFine, ID, tipoProcedimento ):
        self.Cliente = Cliente
        self.dataOraInizio = dataOraInizio
        self.dataOraFine = dataOraFine
        self.ID = ID
        self.tipoProcedimento = tipoProcedimento

        if os.path.isfile('Dati\Appuntamenti.pickle'):
            with open('Dati\Appuntamenti.pickle', 'rb') as f:
                appuntamenti = pickle.load(f)
            appuntamenti[ID] = self
        with open('Dati\Appuntamenti.pickle', 'wb') as f:
            pickle.dump(appuntamenti, f, pickle.HIGHEST_PROTOCOL)

    def getDatiAppuntamento(self):
        return{
            'Cliente': self.Cliente,
            'Data e Ora Inizio': self.dataOraInizio,
            'Data e Ora Fine': self.dataOraFine,
            'ID': self.ID,
            'Tipo Procedimento': self.tipoProcedimento
        }

    def ricercaAppuntamentoCliente (self, Cliente): #Il parametro deve essere una stringa
        if os.path.isfile('Dati\Appuntamenti.pickle'):
            with open('Dati\Appuntamenti.pickle', 'rb') as f:
                appuntamenti = dict(pickle.load(f))
                for appuntamento in udienze.values():
                    if appuntamento.Cliente is Cliente:
                        return appuntamento
                return None
        else:
            return None

    def ricercaAppuntamentoDataInizio (self, DataInizio):
        if os.path.isfile('Dati\Appuntamenti.pickle'):
            with open('Dati\Appuntamenti.pickle', 'rb') as f:
                appuntamenti = dict(pickle.load(f))
                for appuntamento in appuntamenti.values():
                    if appuntamento.DataInizio == DataInizio:
                        return appuntamento
                return None
        else:
            return None

    def ricercaAppuntamentoID(self, ID):
        if os.path.isfile('Dati\Appuntamenti.pickle'):
            with open('Dati\Appuntamenti.pickle', 'rb') as f:
                appuntamenti = dict(pickle.load(f))
                for appuntamento in appuntamenti.values():
                    if appuntamento.ID == ID:
                        return appuntamento
                return None
        else:
            return None


    def rimuoviAppuntamento (self, ID):
        if os.path.isfile('Dati\Appuntamenti.pickle'):
            with open('Dati\Appuntamenti.pickle', 'wb+') as f:
                appuntamenti = dict(pickle.load(f))
                if self.ricercaAppuntamentoID(ID):
                    del appuntamenti[self.ID]
                    pickle.dump(appuntamenti, f, pickle.HIGHEST_PROTOCOL)


    def visualizzaParcella (self, ID)
        if os.path.isfile('Dati\Appuntamenti.pickle'):
            with open('Dati\Appuntamenti.pickle', 'rb') as f:
                appuntamenti = dict(pickle.load(f))
                for appuntamento in appuntamenti.values():
                    if appuntamento.ID == ID:
                        return appuntamento
                    else:
                        return None


