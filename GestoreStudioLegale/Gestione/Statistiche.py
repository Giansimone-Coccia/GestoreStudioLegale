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
        self.mediaUdienzeMensile = 0
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
                    a = str(datetime.now())
                    b = str(i.getDatiUdienza.get('Data e Ora Inizio',None))
                    aa = time.strptime(a, '%Y-%m-%d %H:%M:%S')
                    aaa = datetime.datetime.fromtimestamp(time.mktime(aa))
                    bb = time.strptime(b, '%Y-%m-%d %H:%M:%S')
                    bbb = datetime.datetime.fromtimestamp(time.mktime(bb))
                    if (aaa - bbb).days < nGiorni:
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
                a = str(datetime.now())
                b = str(i.getDatiUdienza.get('Data e Ora Inizio',None))
                aa = time.strptime(a, '%Y-%m-%d %H:%M:%S')
                aaa = datetime.datetime.fromtimestamp(time.mktime(aa))
                bb = time.strptime(b, '%Y-%m-%d %H:%M:%S')
                bbb = datetime.datetime.fromtimestamp(time.mktime(bb))
                if (aaa - bbb).days < 365:
                    nUdienze += 1

            self.mediaUdienzeMensile = nUdienze/12

        if os.path.isfile('Dati\Appuntamenti.pickle'):
            with open('Dati\Appuntamenti.pickle', 'rb') as f:
                appuntamenti = dict(pickle.load(f))

            for i in appuntamenti:
                a = str(datetime.now())
                b = str(i.getDatiAppuntamento.get('Data e Ora Inizio',None))
                aa = time.strptime(a, '%Y-%m-%d %H:%M:%S')
                aaa = datetime.datetime.fromtimestamp(time.mktime(aa))
                bb = time.strptime(b, '%Y-%m-%d %H:%M:%S')
                bbb = datetime.datetime.fromtimestamp(time.mktime(bb))
                if (aaa - bbb).days < 365:
                    nAppuntamenti += 1

            self.numeroAppuntamenti=nAppuntamenti

    #def mostraGrafico(self): #non lo so

    def salvaSuFile (self):
        stats = {
            "mediaUdienzeAmminstrative" : self.mediaUdienzeAmministrative,
            "mediaUdienzeCivili" : self.mediaUdienzeCivili,
            "mediaUdienzeMinorili" : self.mediaUdienzeMinorili,
            "mediaUdienzeMensile" : self.mediaUdienzeMensile,
            "mediaUdienzePenali" : self.mediaUdienzePenali,
            "numeroAppuntamenti" : self.numeroAppuntamenti,
        }
        with open('Dati\Statistiche.pickle', 'wb') as f:
            pickle.dump(stats, f, pickle.HIGHEST_PROTOCOL)

    def mostraStatistiche(self): #modificare
        self.calcolaStatistiche()
        if os.path.isfile('Dati\Statistiche.pickle'):
            with open('Dati\Statistiche.pickle', 'rb') as f:
                stats = dict(pickle.load(f))
        return stats