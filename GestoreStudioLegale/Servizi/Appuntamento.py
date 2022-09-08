import datetime

import pickle
import os.path

class Appuntamento():

    def __init__(self):
       self.Cliente = None
       self.Avvocato = None
       self.ID = ''
       self.dataOraFine = datetime.datetime(year=1970 ,month=1 , day=1 , hour=00 , minute=00 )
       self.dataOraInizio = datetime.datetime (year=1970 ,month=1 , day=1 , hour=00 , minute=00 )
       self.tipoProcedimento = ''

    def aggiornaAppuntamento(self, Cliente = None, Avvocato = None,
                            dataOraInizio=datetime.datetime(year=1970, month=1, day=1, hour=00, minute=00),
                            dataOraFine=datetime.datetime(year=1970, month=1, day=1, hour=00, minute=00),
                            tipoProcedimento = ''):
            if Cliente != None:
                self.Cliente = Cliente
            elif Avvocato != None:
                self.Avvocato = Avvocato
            elif dataOraInizio != datetime.datetime(year=1970, month=1, day=1, hour=00, minute=00):
                self.dataOraInizio = dataOraInizio
            elif dataOraFine != datetime.datetime(year=1970, month=1, day=1, hour=00, minute=00):
                self.dataOraFine = dataOraFine
            elif tipoProcedimento != '':
                self.tipoProcedimento = tipoProcedimento

            self.rimuoviAppuntamento(self.ID)
            self.creaAppuntamento( self.Cliente, self.Avvocato, self.dataOraInizio, self.dataOraFine,
                             self.ID, self.tipoProcedimento)
            print("Aggiornato")

    def creaAppuntamento(self, Cliente, Avvocato, dataOraInizio, dataOraFine, ID, tipoProcedimento ):
        self.Cliente = Cliente
        self.Avvocato = Avvocato
        self.dataOraInizio = datetime.datetime.strptime(dataOraInizio, "%d/%m/%Y,%H:%M")
        self.dataOraFine = datetime.datetime.strptime(dataOraFine, "%d/%m/%Y,%H:%M")
        self.ID = ID
        self.tipoProcedimento = tipoProcedimento

        appuntamenti = []

        if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
            if os.path.getsize('GestoreStudioLegale/Dati/Appuntamenti.pickle') == 0:
                appuntamenti.append(self)
                with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'wb') as f1:
                    pickle.dump(appuntamenti, f1, pickle.HIGHEST_PROTOCOL)
            else:
                if self.ricercaAppuntamentoID(self.ID) is None:
                    with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'rb') as f:
                        appuntamenti = pickle.load(f)
                        appuntamenti.append(self)

                    with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'wb') as f1:
                        pickle.dump(appuntamenti, f1, pickle.HIGHEST_PROTOCOL)

    def getDatiAppuntamento(self):
        d = {}
        d['Cliente'] = self.Cliente
        d['Avvocato'] = self.Avvocato
        d['Data e Ora Inizio'] = self.dataOraInizio
        d['Data e Ora Fine'] = self.dataOraFine
        d['ID'] = self.ID
        d['Tipo Procedimento'] = self.tipoProcedimento
        print(d)
        return d


    def ricercaAppuntamentoCliente (self, Cliente):
        listaAppuntamenti=[]
        if os.path.isfile('GestoreStudioLegale/Dati/Appuntamento.pickle'):
            with open('GestoreStudioLegale/Dati/Appuntamento.pickle', 'rb') as f:
                appuntamenti = pickle.load(f)
                for appuntamento in appuntamenti:
                    if appuntamento.Cliente.Id == Cliente.Id:
                        listaAppuntamenti.append(appuntamento)
                return listaAppuntamenti
        else:
            return None

    def ricercaAppuntamentoDataInizio (self, DataInizio):
        if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
            with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'rb') as f:
                appuntamenti = pickle.load(f)
                for appuntamento in appuntamenti:
                    if appuntamento.DataInizio == DataInizio:
                        return appuntamento
                return None
        else:
            return None

    def ricercaAppuntamentoID(self, ID):
        if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
            with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'rb') as f:
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




