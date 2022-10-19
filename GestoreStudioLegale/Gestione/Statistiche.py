import pickle
import os.path
from datetime import datetime, timedelta, time

from PyQt5.QtWidgets import QMessageBox


class Statistiche:

    def __init__(self):
        self.mediaUdienzeAmministrative = 0
        self.mediaUdienzeCivili = 0
        self.mediaUdienzeMensili = 0
        self.mediaUdienzeMinorili = 0
        self.mediaUdienzePenali = 0
        self.numeroAppuntamenti = 0

    def calcolaStatistiche(self):

        nUdienzeAmminsitrative=0
        nUdienzeCivili=0
        nUdienzeMinorili=0
        nUdienzePenali=0
        nUdienze=0
        nAppuntamenti=0

        udienze = []
        if os.path.isfile('GestoreStudioLegale/Dati/Udienze.pickle'):
            with open('GestoreStudioLegale/Dati/Udienze.pickle', 'rb') as f:
                try:
                    udienze = pickle.load(f)
                except EOFError as er:
                    self.problema()

            for udienza in udienze:
                if udienza.tipoTribunale == 'amministrativa':
                    date = datetime.now() - timedelta(days=365)
                    if udienza.dataOraInizio > date:
                        nUdienzeAmminsitrative += 1
            for udienza in udienze:
                if udienza.tipoTribunale == 'civile':
                    date = datetime.now() - timedelta(days=365)
                    if udienza.dataOraInizio > date:
                        nUdienzeCivili += 1
            for udienza in udienze:
                if udienza.tipoTribunale == 'penale':
                    date = datetime.now() - timedelta(days=365)
                    if udienza.dataOraInizio > date:
                        nUdienzePenali += 1
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
                    self.problema()

            for appuntamento in appuntamenti:
                date = datetime.now() - timedelta(days = 365)
                if appuntamento.dataOraInizio > date:
                    nAppuntamenti += 1

            self.numeroAppuntamenti = nAppuntamenti/12


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
                d = pickle.load(f)
                return d

    def mostraStatistiche(self):
        self.calcolaStatistiche()
        self.salvaSuFile()

        stats={}
        if os.path.isfile('GestoreStudioLegale/Dati/Statistiche.pickle'):
            with open('GestoreStudioLegale/Dati/Statistiche.pickle', 'rb') as f:
                try:
                    stats = dict(pickle.load(f))
                except EOFError as er:
                    self.problema()
        return stats

    def problema(self):
        msg = QMessageBox()
        msg.setWindowTitle("Problema")
        msg.setText("Problema con lettura/scrittua file")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

