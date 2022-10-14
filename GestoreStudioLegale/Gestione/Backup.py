import pickle
import os.path
import datetime
import os

from PyQt5.QtWidgets import QMessageBox


class Backup():

    def _init_(self):
        self.data = datetime.datetime(year=1970, month=1, day=1)
        self.frequenza = 24

    def eseguiBackup(self): # da vedere
        file_path = 'GestoreStudioLegale/Dati/Backup.pickle'
        with open(file_path, 'r+') as f:
            f.truncate(0)
            f.seek(0)
        self.salvaDatiAppuntamento()
        self.salvaDatiParcella()
        self.salvaDatiCorsoAggiornamento()
        self.salvaDatiUtilizzatore()

    def modificaData(self, nuovaData): #ricorda su enterprise
        self.data=nuovaData

    def modificaFrequenza(self, nuovaFrequenza):  #ricorda su enterprise
        self.frequenza=nuovaFrequenza

    def salvaDatiAppuntamento(self):

        backup = {}
        if os.path.isfile('GestoreStudioLegale/Dati/Backup.pickle'):
            with open('GestoreStudioLegale/Dati/Backup.pickle', 'rb') as f:
                try:
                    backup = dict(pickle.load(f))
                except EOFError as er:
                    print("Errore5")

        appuntamenti = []
        if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
            with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'rb') as f:
                try:
                    appuntamenti = pickle.load(f)
                    backup['appuntamenti'] = appuntamenti
                except EOFError as er:
                    print("Errore1")
        with open('GestoreStudioLegale/Dati/Backup.pickle', 'wb') as f:
            pickle.dump(backup, f, pickle.HIGHEST_PROTOCOL)

    def salvaDatiParcella(self):
        backup = {}
        if os.path.isfile('GestoreStudioLegale/Dati/Backup.pickle'):
            with open('GestoreStudioLegale/Dati/Backup.pickle', 'rb') as f:
                try:
                    backup = dict(pickle.load(f))
                except EOFError as er:
                    print("Errore5")

        parcelle = []
        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
            with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                try:
                    parcelle = pickle.load(f)
                    backup['parcelle'] = parcelle
                except EOFError as er:
                    print("Errore2")
        with open('GestoreStudioLegale/Dati/Backup.pickle', 'wb') as f:
            pickle.dump(backup, f, pickle.HIGHEST_PROTOCOL)

    def salvaDatiUtilizzatore(self):
        backup = {}
        if os.path.isfile('GestoreStudioLegale/Dati/Backup.pickle'):
            with open('GestoreStudioLegale/Dati/Backup.pickle', 'rb') as f:
                try:
                    backup = dict(pickle.load(f))
                except EOFError as er:
                    print("Errore5")

        avvocati = []
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                try:
                    avvocati = pickle.load(f)
                    backup['avvocati'] = avvocati
                except EOFError as er:
                    print("Errore3")

        clienti=[]
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                try:
                    clienti = pickle.load(f)
                    backup['clienti'] = clienti
                except EOFError as er:
                    print("Errore4")

        with open('GestoreStudioLegale/Dati/Backup.pickle', 'wb') as f:
            pickle.dump(backup, f, pickle.HIGHEST_PROTOCOL)

    def salvaDatiCorsoAggiornamento(self):
        backup = {}
        if os.path.isfile('GestoreStudioLegale/Dati/Backup.pickle'):
            with open('GestoreStudioLegale/Dati/Backup.pickle', 'rb') as f:
                try:
                    backup = dict(pickle.load(f))
                except EOFError as er:
                    print("Errore5")

        corsiAggiornamento = []
        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
            with open('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle', 'rb') as f:
                try:
                    corsiAggiornamento = pickle.load(f)
                    backup['corsi aggiornamento'] = corsiAggiornamento
                except EOFError as er:
                    print("Errore5")
        with open('GestoreStudioLegale/Dati/Backup.pickle', 'wb') as f:
            pickle.dump(backup, f, pickle.HIGHEST_PROTOCOL)

    def getDatiBakcup(self):
        backup = {}
        if os.path.isfile('GestoreStudioLegale/Dati/Backup.pickle'):
            with open('GestoreStudioLegale/Dati/Backup.pickle', 'rb') as f:
                try:
                    backup = dict(pickle.load(f))
                except EOFError as er:
                    print("Errore5")
        return backup

    def problema(self):
        msg = QMessageBox()
        msg.setWindowTitle("Problema")
        msg.setText("Problema con il backup")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()