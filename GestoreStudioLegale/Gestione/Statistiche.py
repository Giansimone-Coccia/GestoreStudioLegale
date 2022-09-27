import pickle
import os.path
from datetime import datetime, timedelta, time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure

from GestoreStudioLegale.Servizi.Udienza import Udienza
from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento

class Statistiche:

    def __init__(self):
        self.mediaUdienzeAmministrative = 0
        self.mediaUdienzeCivili = 0
        self.mediaUdienzeMinorili = 0
        self.mediaUdienzeMensili = 0
        self.mediaUdienzePenali = 0
        self.numeroAppuntamenti = 0

    def calcolaStatistiche(self):

        nUdienzeAmminsitrative=0
        nUdienzeCivili=0
        nUdienzeMinorili=0
        nUdienzePenali=0
        nUdienze=0
        nAppuntamenti=0

        '''def breve(lista,tribunale,nUdienze,nGiorni):
            for i in lista:
                if i.getDatiUdienza().get('Tipo Tribunale', None) == tribunale:
                    date = datetime.now()-timedelta(days = nGiorni)
                    if i.getDatiUdienza.get('Data e Ora Inizio') > date:
                        nUdienze += 1'''

        udienze = []
        if os.path.isfile('GestoreStudioLegale/Dati/Udienze.pickle'):
            with open('GestoreStudioLegale/Dati/Udienze.pickle', 'rb') as f:
                try:
                    udienze = pickle.load(f)
                except EOFError as er:
                    print("") #scrivere errore

            #breve(udienze,'amministrativo',nUdienzeAmminsitrative,365)
            for udienza in udienze:
                if udienza.tipoTribunale == 'amministrativa':
                    date = datetime.now() - timedelta(days=365)
                    if udienza.dataOraInizio > date:
                        nUdienzeAmminsitrative += 1
            #breve(udienze, 'civile', nUdienzeCivili, 365)
            for udienza in udienze:
                if udienza.tipoTribunale == 'civile':
                    date = datetime.now() - timedelta(days=365)
                    if udienza.dataOraInizio > date:
                        nUdienzeCivili += 1
            #breve(udienze, 'penale', nUdienzePenali, 365)
            for udienza in udienze:
                if udienza.tipoTribunale == 'penale':
                    date = datetime.now() - timedelta(days=365)
                    if udienza.dataOraInizio > date:
                        nUdienzePenali += 1
            #breve(udienze, 'minorile', nUdienzeMinorili, 365)
            for udienza in udienze:
                if udienza.tipoTribunale == 'minorile':
                    date = datetime.now() - timedelta(days=365)
                    if udienza.dataOraInizio > date:
                        nUdienzeMinorili += 1

            self.mediaUdienzeCivili = nUdienzeCivili/12
            self.mediaUdienzePenali = nUdienzePenali/12
            self.mediaUdienzeMinorili = nUdienzeMinorili/12
            self.mediaUdienzeAmministrative = nUdienzeAmminsitrative/12

            for udienza in udienze:
                date = datetime.now() - timedelta(days = 365)
                if udienza.dataOraInizio > date:
                    nUdienze += 1

            self.mediaUdienzeMensili = nUdienze/12

        appuntamenti=[]
        if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
            with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'rb') as f:
                try:
                    appuntamenti = pickle.load(f)
                except EOFError as er:
                    print("") #scrivere errore

            for appuntamento in appuntamenti:
                date = datetime.now() - timedelta(days = 365)
                if appuntamento.dataOraInizio > date:
                    nAppuntamenti += 1

            self.numeroAppuntamenti = nAppuntamenti

    def mostraGrafico(self,a='a'):
        my_dict = self.mostraStatistiche()

        myList = my_dict.items()
        #myList = sorted(myList)
        x = my_dict.keys()
        y = my_dict.values()
        if a == 'a':
            return x
        else:
            return y

        '''plt.bar(x, y)
        return plt
        
        canvas = FigureCanvas(Figure(figsize=(5, 3)))
        myList = my_dict.items()
        # myList = sorted(myList)
        x, y = zip(*myList)

        ax = canvas.figure.subplots(plt.bar(x,y))
        return ax'''

    def salvaSuFile(self):
        stats = {
            "Amminstrative" : self.mediaUdienzeAmministrative,
            "Civili" : self.mediaUdienzeCivili,
            "Minorili" : self.mediaUdienzeMinorili,
            "Mensili" : self.mediaUdienzeMensili,
            "Penali" : self.mediaUdienzePenali,
            "Appuntamenti" : self.numeroAppuntamenti,
        }
        if os.path.isfile('GestoreStudioLegale/Dati/Statistiche.pickle'):
            with open('GestoreStudioLegale/Dati/Statistiche.pickle', 'wb') as f:
                pickle.dump(stats, f, pickle.HIGHEST_PROTOCOL)

    def leggiFile(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Statistiche.pickle'):
            with open('GestoreStudioLegale/Dati/Statistiche.pickle', 'rb') as f:
                #d = {}
                d = pickle.load(f)
                #pickle.load(f)
                return d

    def mostraStatistiche(self): #modificare, c'è scritto void
        self.calcolaStatistiche()
        self.salvaSuFile()
        #statistica = statistica.lower()

        stats={}
        if os.path.isfile('GestoreStudioLegale/Dati/Statistiche.pickle'):
            with open('GestoreStudioLegale/Dati/Statistiche.pickle', 'rb') as f:
                try:
                    stats = dict(pickle.load(f))
                except EOFError as er:
                    print("errore!") #scrivere errore
        return stats

