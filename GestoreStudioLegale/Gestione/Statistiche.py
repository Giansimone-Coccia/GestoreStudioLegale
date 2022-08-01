import pickle
import os.path

class Statistiche:

    def __init__(self):
        self.mediaUdienzeAmministrative = 0
        self.mediaUdienzeCivili = 0
        self.mediaUdienzeMinorili = 0
        self.mediaUdienzeMensile = 0
        self.mediaUdienzePenali = 0
        self.numeroAppuntamenti = 0

    def calcolaStatistiche(self):
        self.salvaSuFile()

    def mostraGrafico(self):

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


    def mostraStatistiche(self):
        self.calcolaStatistiche()
        if os.path.isfile('Dati\Statistiche.pickle'):
            with open('Dati\Statistiche.pickle', 'rb') as f:
                stats = dict(pickle.load(f))
                for key, value in stats.items():
                    print(key, value)