import pickle
import os.path
from datetime import datetime,timedelta,time

# from Servizi.Udienza import Udienza
# from Servizi.Appuntamento import Appuntamento
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

        def breve(lista,tribunale,nUdienze,nGiorni):
            for i in lista:
                if i.getDatiUdienza.get('Tipo Tribunale',None) == tribunale:
                    data=datetime.now()-timedelta(days = nGiorni)
                    if i > data:
                        nUdienze += 1

        udienze = []
        if os.path.isfile('Dati\Udienze.pickle'):
            with open('Dati\Udienze.pickle', 'rb') as f:
                try:
                    udienze = pickle.load(f)
                except EOFError as er:
                    print("Errore")

            breve(udienze,'Tribunale Amministrativo',nUdienzeAmminsitrative,365)
            breve(udienze, 'Tribunale Civile', nUdienzeCivili, 365)
            breve(udienze, 'Tribunale Penale', nUdienzePenali, 365)
            breve(udienze, 'Tribunale Minorile', nUdienzeMinorili, 365)

            self.mediaUdienzeCivili = nUdienzeCivili/12
            self.mediaUdienzePenali = nUdienzePenali/12
            self.mediaUdienzeMinorili = nUdienzeMinorili/12
            self.mediaUdienzeAmministrative = nUdienzeAmminsitrative/12

            for i in udienze:
                data = datetime.now() - timedelta(days = 365)
                if i > data:
                    nUdienze += 1

            self.mediaUdienzeMensili = nUdienze/12

        if os.path.isfile('Dati\Appuntamenti.pickle'):
            with open('Dati\Appuntamenti.pickle', 'rb') as f:
                try:
                    appuntamenti = pickle.load(f)
                except EOFError as er:
                    print("Errore")

            for i in appuntamenti:
                data = datetime.now() - timedelta(days = 365)
                if i > data:
                    nAppuntamenti += 1

            self.numeroAppuntamenti = nAppuntamenti

    #def mostraGrafico(self): #non lo so

    def salvaSuFile (self):
        stats = {
            "mediaUdienzeAmminstrative" : self.mediaUdienzeAmministrative,
            "mediaUdienzeCivili" : self.mediaUdienzeCivili,
            "mediaUdienzeMinorili" : self.mediaUdienzeMinorili,
            "mediaUdienzeMensili" : self.mediaUdienzeMensile,
            "mediaUdienzePenali" : self.mediaUdienzePenali,
            "numeroAppuntamenti" : self.numeroAppuntamenti,
        }
        with open('Dati\Statistiche.pickle', 'wb') as f:
            pickle.dump(stats, f, pickle.HIGHEST_PROTOCOL)

    def mostraStatistiche(self,statistica = ""): #modificare, c'è scritto void
        self.calcolaStatistiche()
        statistica = statistica.lower()

        if os.path.isfile('Dati\Statistiche.pickle'):
            with open('Dati\Statistiche.pickle', 'rb') as f:
                stats = dict(pickle.load(f))

        if statistica == "udienze amministrative":
            return stats["mediaUdienzeAmminstrative"]
        elif statistica == "udienze civili":
            return stats["mediaUdienzeCivili"]
        elif statistica == "udienze minorili":
            return stats["mediaUdienzeMinorili"]
        elif statistica == "udienze penali":
            return stats["mediaUdienzePenali"]
        elif statistica == "udienze mensili":
            return stats["mediaUdienzeMensili"]
        elif statistica == "numero appuntamenti":
            return stats["numeroAppuntamenti"]
        else:
            return stats