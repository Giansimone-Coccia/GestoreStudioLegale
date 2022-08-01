import datetime

from Servizi.Cliente import Cliente
from Servizi.Avvocato import Avvocato
import pickle
import os.path

class Udienza(Udienza):

    def __init__(self):
       self.Cliente = Cliente
       self.Avvocato = Avvocato
       self.cittaTribunale = []
       self.ID = []
       self.dataOraFine = datetime.datetime(year=1970 ,month=1 , day=1 , hour=00 , minute=00 )
       self.dataOraInizio = datetime.datetime (year=1970 ,month=1 , day=1 , hour=00 , minute=00 )
       self.tipoTribunale = []

    def aggiornaUdienza

    def creaUdienza(self, Avvocato, cittaTribunale, Cliente, dataOraInizio, dataOraFine, ID, tipoTribunale ):
        self.Avvocato = Avvocato
        self.cittaTribunale = cittaTribunale
        self.Cliente = Cliente
        self.dataOraInizio = dataOraInizio
        self.dataOraFine = dataOraFine
        self.ID = ID
        self.tipoTribunale = tipoTribunale

        if os.path.isfile('Dati\Udienze.pickle'):
            with open('Dati\Udienze.pickle', 'rb') as f:
                udienze = pickle.load(f)
            udienze[ID] = self
        with open('Dati\Udienze.pickle', 'wb') as f:
            pickle.dump(udienze, f, pickle.HIGHEST_PROTOCOL)

    def getDatiUdienza(self):
        return{
            'Avvocato': self.Avvocato,
            'Città Tribunale': self.cittaTribunale,
            'Cliente': self.Cliente,
            'Data e Ora Inizio': self.dataOraInizio,
            'Data e Ora Fine': self.dataOraFine,
            'ID': self.ID,
            'Tipo Tribunale': self.tipoTribunale
        }

    def ricercaUdienzaCliente (self, Cliente):
        if os.path.isfile('Dati\Udienze.pickle'):
            with open('Dati\Udienze.pickle', 'rb') as f:
                udienze = dict(pickle.load(f))
                for udienza in udienze.values():
                    if udienza.Cliente is Cliente:
                        return udienza
                return None
        else:
            return None

    def ricercaUdienzaDataInizio (self, DataInizio):
        if os.path.isfile('Dati\Udienze.pickle'):
            with open('Dati\Udienze.pickle', 'rb') as f:
                udienze = dict(pickle.load(f))
                for udienza in udienze.values():
                    if udienza.DataInizio == DataInizio:
                        return udienza
                return None
        else:
            return None

    def ricercaUdienzaID(self, ID):
        if os.path.isfile('Dati\Udienze.pickle'):
            with open('Dati\Udienze.pickle', 'rb') as f:
                udienze = dict(pickle.load(f))
                for udienza in udienze.values():
                    if udienza.ID == ID:
                        return udienza
                return None
        else:
            return None

    def ricercaUdienzaTipo(self, tipoTribunale):
        if os.path.isfile('Dati\Udienze.pickle'):
            with open('Dati\Udienze.pickle', 'rb') as f:
                udienze = dict(pickle.load(f))
                for udienza in udienze.values():
                    if udienza.tipoTribunale == tipoTribunale:
                        return tipoTribunale
                return None
        else:
            return None

    def rimuoviUdienza (self, ID):
        if os.path.isfile('Dati\Udienze.pickle'):
            with open('Dati\Udienze.pickle', 'wb+') as f:
                udienze = dict(pickle.load(f))
                if self.ricercaUdienzaID(ID):
                    del udienze[self.ID]
                    pickle.dump(udienze, f, pickle.HIGHEST_PROTOCOL)


    def visualizzaParcella (self, ID)
        if os.path.isfile('Dati\Udienze.pickle'):
            with open('Dati\Udienze.pickle', 'rb') as f:
                udienze = dict(pickle.load(f))
                for udienza in udienze.values():
                    if udienza.ID == ID:
                        return udienza
                    else:
                        return None


