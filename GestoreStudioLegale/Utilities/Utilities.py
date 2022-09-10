import os

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QSizePolicy

import pickle
from GestoreStudioLegale.Servizi import Cliente

class Tools():

    clienti = []
    avvocati = []
    appuntamenti = []
    parcelle = []
    udienze = []

    def __init__(self):
        pass

    def leggi(self,file = 'Credenziali',n = 20):
        if os.path.isfile(f'GestoreStudioLegale/Dati/{file}.pickle'):
            with open(f'GestoreStudioLegale/Dati/{file}.pickle', 'r') as f:
                if n == 0 :
                    return f.read()
                stringa1 = f.read(n)
                #stringa1 = f.readline()
                #stringa2 = f.readline()
                #self.salvaAppend(stringa2)
                return str(stringa1)

    def salva(self, stringa,file='Credenziali'):
        if os.path.isfile(f'GestoreStudioLegale/Dati/{file}.pickle'):
            with open(f'GestoreStudioLegale/Dati/{file}.pickle', 'w') as f:
                f.write(stringa)
                f.write('\n')

    def salvaAppend(self, stringa,file='Credenziali'): #per richiamarlo anche poi con la password
        if os.path.isfile(f'GestoreStudioLegale/Dati/{file}.pickle'):
            with open(f'GestoreStudioLegale/Dati/{file}.pickle', 'a') as f:
                f.write(stringa)
                f.write('\n')

    def rewindButton(self, rewind):
        button1 = QPushButton("Indietro")
        button1.setFont(QFont('Arial', 10))
        button1.clicked.connect(rewind)
        button1.setSizePolicy(150, 50)
        return button1

    def createButton(self, nome, on_click):
        button = QPushButton(nome)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setFont(QFont('Arial', 10))
        button.clicked.connect(on_click)
        return button

    def loadClienti(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                self.clienti = list(pickle.load(f))
                return self.clienti

    def loadAvvocati(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                self.avvocati = list(pickle.load(f))
                return self.avvocati

    def loadUdienze(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Udienze.pickle'):
            with open('GestoreStudioLegale/Dati/Udienze.pickle', 'rb') as f:
                self.udienze = list(pickle.load(f))
                return self.udienze

    def loadParcelle(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
            with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                self.parcelle = list(pickle.load(f))
                return self.parcelle

    def loadAppuntamenti(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
            with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'rb') as f:
                self.appuntamenti = list(pickle.load(f))
                return self.appuntamenti