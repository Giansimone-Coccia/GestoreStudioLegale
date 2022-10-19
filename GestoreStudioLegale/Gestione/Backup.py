import pickle
import os.path
import datetime
import os

from PyQt5.QtWidgets import QMessageBox


class Backup():

    backup = {}

    def __init__(self):
        self.data = datetime.datetime(year=1970, month=1, day=1)
        self.frequenza = 24

    def eseguiBackup(self):
        file_path = 'GestoreStudioLegale/Dati/Backup.pickle'
        with open(file_path, 'w+') as f:
            f.write('')
        self.salvaDatiAppuntamento()
        self.salvaDatiParcella()
        self.salvaDatiCorsoAggiornamento()
        self.salvaDatiUtilizzatore()

    def modificaData(self, nuovaData):
        self.data=nuovaData

    def modificaFrequenza(self, nuovaFrequenza):
        self.frequenza=nuovaFrequenza

    def salvaDatiAppuntamento(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
            with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'rb') as f:
                try:
                    appuntamenti = pickle.load(f)
                    self.backup['appuntamenti'] = appuntamenti
                except EOFError as er:
                    self.problema()
            with open('GestoreStudioLegale/Dati/Backup.pickle', 'wb') as f:
                pickle.dump(self.backup, f, pickle.HIGHEST_PROTOCOL)

    def salvaDatiUdienza(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Udienze.pickle'):
            with open('GestoreStudioLegale/Dati/Udienze.pickle', 'rb') as f:
                try:
                    udienze = pickle.load(f)
                    self.backup['udienze'] = udienze
                except EOFError as er:
                    self.problema()
            with open('GestoreStudioLegale/Dati/Backup.pickle', 'wb') as f:
                pickle.dump(self.backup, f, pickle.HIGHEST_PROTOCOL)


    def salvaDatiParcella(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
            with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                try:
                    parcelle = pickle.load(f)
                    self.backup['parcelle'] = parcelle
                except EOFError as er:
                    self.problema()
            with open('GestoreStudioLegale/Dati/Backup.pickle', 'wb') as f:
                pickle.dump(self.backup, f, pickle.HIGHEST_PROTOCOL)

    def salvaDatiUtilizzatore(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                try:
                    avvocati = pickle.load(f)
                    self.backup['avvocati'] = avvocati
                except EOFError as er:
                    self.problema()

        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                try:
                    clienti = pickle.load(f)
                    self.backup['clienti'] = clienti
                except EOFError as er:
                    self.problema()

        with open('GestoreStudioLegale/Dati/Backup.pickle', 'wb') as f:
            pickle.dump(self.backup, f, pickle.HIGHEST_PROTOCOL)

    def salvaDatiCorsoAggiornamento(self):
        if os.path.isfile('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle'):
            with open('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle', 'rb') as f:
                try:
                    corsiAggiornamento = pickle.load(f)
                    self.backup['corsi aggiornamento'] = corsiAggiornamento
                except EOFError as er:
                    self.problema()
        with open('GestoreStudioLegale/Dati/Backup.pickle', 'wb') as f:
            pickle.dump(self.backup, f, pickle.HIGHEST_PROTOCOL)

    def getDatiBakcup(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Backup.pickle'):
            with open('GestoreStudioLegale/Dati/Backup.pickle', 'rb') as f:
                try:
                    self.backup = dict(pickle.load(f))
                    print(self.backup)
                except EOFError as er:
                    self.problema()
        return self.backup

    def problema(self):
        msg = QMessageBox()
        msg.setWindowTitle("Problema")
        msg.setText("Problema con il backup")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()