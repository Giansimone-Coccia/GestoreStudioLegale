import datetime

from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Servizi.Avvocato import Avvocato
import pickle
import os.path

class Udienza:

    def __init__(self):
       self.Cliente = None
       self.Avvocato = None
       self.cittaTribunale = ''
       self.ID = ''
       self.dataOraFine = datetime.datetime(year=1970 ,month=1 , day=1 , hour=00 , minute=00 )
       self.dataOraInizio = datetime.datetime (year=1970 ,month=1 , day=1 , hour=00 , minute=00 )
       self.tipoTribunale = ''

    def aggiornaUdienza(self, cittaTribunale = '', tipoTribunale = '', dataOraInizio = datetime.datetime(year=1970 ,month=1 , day=1 , hour=00 , minute=00 ),
                        dataOraFine = datetime.datetime(year=1970 ,month=1 , day=1 , hour=00 , minute=00 ),
                        Cliente = None, Avvoccato = None):
        if cittaTribunale != '':
            self.cittaTribunale = cittaTribunale
        elif tipoTribunale != '':
            self.tipoTribunale = tipoTribunale
        elif dataOraInizio != datetime.datetime(year=1970 ,month=1 , day=1 , hour=00 , minute=00 ):
            self.dataOraInizio = dataOraInizio
        elif dataOraFine != datetime.datetime(year=1970 ,month=1 , day=1 , hour=00 , minute=00 ):
            self.dataOraFine = dataOraFine
        elif Cliente != None:
            self.Cliente = Cliente
        elif Avvoccato != None:
            self.Avvocato = Avvocato

        self.rimuoviUdienza(self.ID)
        self.creaUdienza(self.Avvocato, self.cittaTribunale, self.Cliente, self.dataOraInizio, self.dataOraFine, self.ID, self.tipoTribunale)
        print("Aggiornato")

    def creaUdienza(self, Avvocato, cittaTribunale, Cliente, dataOraInizio, dataOraFine, ID, tipoTribunale ):
        self.Avvocato = Avvocato
        self.cittaTribunale = cittaTribunale
        self.Cliente = Cliente
        self.dataOraInizio = dataOraInizio
        self.dataOraFine = dataOraFine
        self.ID = ID
        self.tipoTribunale = tipoTribunale

        udienze = []

        if os.path.isfile('GestoreStudioLegale/Dati/Udienze.pickle'):
            #if os.stat('GestoreStudioLegale/Dati/Udienze.pickle').st_size != 0:
            if os.path.getsize('GestoreStudioLegale/Dati/Udienze.pickle') == 0:
                udienze.append(self)
                with open('GestoreStudioLegale/Dati/Udienze.pickle', 'wb') as f1:
                    pickle.dump(udienze, f1, pickle.HIGHEST_PROTOCOL)
                #raise EOFError
            else:
                if self.ricercaUdienzaID(self.ID) is None:
                    with open('GestoreStudioLegale/Dati/Udienze.pickle', 'rb') as f:
                    #try:
                        udienze = pickle.load(f)
                        udienze.append(self)
                    #except EOFError as er:
                    #   print("Errore")
                    with open('GestoreStudioLegale/Dati/Udienze.pickle', 'wb') as f1:
                        pickle.dump(udienze, f1, pickle.HIGHEST_PROTOCOL)


    def getDatiUdienza(self): #errore dizionario
        d = {}
        d['Avvocato'] = self.Avvocato
        d['Città Tribunale'] = self.cittaTribunale
        d['Cliente'] = self.Cliente
        d['Data e Ora Inizio'] = self.dataOraInizio
        d['Data e Ora Fine'] = self.dataOraFine
        d['ID'] = self.ID
        d['Tipo Tribunale'] = self.tipoTribunale
        print(d)
        return d

    def ricercaUdienzaCliente (self, cliente):
        listaUdienze=[]

        if os.path.isfile('GestoreStudioLegale/Dati/Udienze.pickle'):
            with open('GestoreStudioLegale/Dati/Udienze.pickle', 'rb') as f:
                udienze = pickle.load(f)
                for udienza in udienze:
                    if udienza.Cliente.Id == cliente.Id:
                        listaUdienze.append(udienza)
                return listaUdienze
        else:
            return None

    def ricercaUdienzaDataInizio (self, DataInizio):
        if os.path.isfile('GestoreStudioLegale/Dati/Udienze.pickle'):
            with open('GestoreStudioLegale/Dati/Udienze.pickle', 'rb') as f:
                udienze = pickle.load(f)
                for udienza in udienze:
                    if udienza.dataOraInizio == DataInizio:
                        return udienza
                return None
        else:
            return None

    def ricercaUdienzaID(self, ID):
        if os.path.isfile('GestoreStudioLegale/Dati/Udienze.pickle'):
            with open('GestoreStudioLegale/Dati/Udienze.pickle', 'rb') as f:
                udienze = pickle.load(f)
                for udienza in udienze:
                    if udienza.ID == ID:
                        return udienza
                return None
        else:
            return None

    def ricercaUdienzaTipo(self, tipoTribunale):
        listaUdienze=[]
        if os.path.isfile('GestoreStudioLegale/Dati/Udienze.pickle'):
            with open('GestoreStudioLegale/Dati/Udienze.pickle', 'rb') as f:
                udienze = pickle.load(f)
                for udienza in udienze:
                    if udienza.tipoTribunale == tipoTribunale:
                        listaUdienze.append(udienza)
                return listaUdienze
            return None
        else:
            return None

    @staticmethod
    def rimuoviUdienza (ID):
        try:
            udienze = []
            if os.path.isfile('GestoreStudioLegale/Dati/Udienze.pickle'):
                with open('GestoreStudioLegale/Dati/Udienze.pickle', 'rb') as f:
                    udienze = pickle.load(f)
            for udienza in udienze:
                if udienza.ID == ID:
                    udienze.remove(udienza)
                else:
                    print("Udienza non trovato")
            with open('GestoreStudioLegale/Dati/Udienze.pickle', 'wb') as f1:
                pickle.dump(udienze, f1, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
                print("Finito")



