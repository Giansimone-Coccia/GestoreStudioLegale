import datetime

from GestoreStudioLegale.Servizi.Cliente import Cliente
import pickle
import os.path

class Appuntamento():

    def __init__(self):
       self.Cliente = Cliente
       self.ID = []
       self.dataOraFine = datetime.datetime(year=1970 ,month=1 , day=1 , hour=00 , minute=00 )
       self.dataOraInizio = datetime.datetime (year=1970 ,month=1 , day=1 , hour=00 , minute=00 )
       self.tipoProcedimento = ''

    #def aggiornaAppuntamento(self):

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
        d = {}
        d['Cliente'] = self.Cliente
        d['Data e Ora Inizio'] = self.dataOraInizio
        d['Data e Ora Fine'] = self.dataOraFine
        d['ID'] = self.ID
        d['Tipo Procedimento'] = self.tipoProcedimento
        print(d)
        return d


    def ricercaAppuntamentoCliente (self, Cliente): #Il parametro deve essere una stringa
        if os.path.isfile('Dati\Appuntamenti.pickle'):
            with open('Dati\Appuntamenti.pickle', 'rb') as f:
                appuntamenti = pickle.load(f)
                for appuntamento in appuntamenti:
                    if appuntamento.Cliente is Cliente:
                        listaAppuntamenti = [appuntamento]
                return listaAppuntamenti
            return None
        else:
            return None

    def ricercaAppuntamentoDataInizio (self, DataInizio):
        if os.path.isfile('Dati\Appuntamenti.pickle'):
            with open('Dati\Appuntamenti.pickle', 'rb') as f:
                appuntamenti = pickle.load(f)
                for appuntamento in appuntamenti:
                    if appuntamento.DataInizio == DataInizio:
                        return appuntamento
                return None
        else:
            return None

    def ricercaAppuntamentoID(self, ID):
        if os.path.isfile('Dati\Appuntamenti.pickle'):
            with open('Dati\Appuntamenti.pickle', 'rb') as f:
                appuntamenti = pickle.load(f)
                for appuntamento in appuntamenti:
                    if appuntamento.ID == ID:
                        return appuntamento
                return None
        else:
            return None

    @staticmethod
    def rimuoviAppuntamento (ID):
        try:
            appuntamenti = []
            if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
                with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'rb') as f:
                    appuntamenti = pickle.load(f)
            for appuntamento in appuntamenti:
                if appuntamento.ID == ID:
                    appuntamenti.remove(appuntamento)
                else:
                    print("Appuntamento non trovato")
            with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'wb') as f1:
                pickle.dump(appuntamenti, f1, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            print("Finito")


    def visualizzaAppuntamento (self, ID):
        if os.path.isfile('Dati\Appuntamenti.pickle'):
            with open('Dati\Appuntamenti.pickle', 'rb') as f:
                appuntamenti = pickle.load(f)
                for appuntamento in appuntamenti:
                    if appuntamento.ID == ID:
                        return appuntamento
                    else:
                        return None


