import os
import re

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QSizePolicy

import pickle
from GestoreStudioLegale.Servizi import Cliente

class Tools():

    appuntamenti = []
    avvocati = []
    clienti = []
    corsiAggiornamento = []
    corsiDict = []
    parcelle = []
    udienze = []

    def __init__(self):
        pass

    def check(self,email):
        regex = '^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, email) and email.endswith("@gmail.com")):
            print("Valid Email")
            return True
        else:
            print("Invalid Email")
            return False

    def createButton(self, nome, on_click,dim=10,method2 = 0):
        button = QPushButton(nome)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setFont(QFont('Arial', dim))
        #button.setBaseSize(baseS,heightS)
        #button.setMaximumSize(maxBase,maxHeight)
        button.clicked.connect(on_click)
        if(method2 != 0):
            button.clicked.connect(method2)
        return button

    def IdGenerator(self, stringa): #ID posto a 0000 nel file
        if stringa == 'A':
            stringa1 = int(self.leggi('lastID').rsplit()[0]) + 1
            stringa = stringa+str(stringa1)
            self.salva(str(stringa1), 'lastID')
            return stringa
        elif stringa == 'C':
            stringa1 = int(self.leggi('lastID').rsplit()[0]) + 1
            stringa = stringa + str(stringa1)
            self.salva(str(stringa1), 'lastID')
            return stringa
        elif stringa == 'AP':
            stringa1 = int(self.leggi('lastID').rsplit()[0]) + 1
            stringa = stringa + str(stringa1)
            self.salva(str(stringa1), 'lastID')
            return stringa
        elif stringa == 'UD':
            stringa1 = int(self.leggi('lastID').rsplit()[0]) + 1
            stringa = stringa + str(stringa1)
            self.salva(str(stringa1), 'lastID')
            return stringa
        elif stringa == 'PA':
            stringa1 = int(self.leggi('lastID').rsplit()[0]) + 1
            stringa = stringa + str(stringa1)
            self.salva(str(stringa1), 'lastID')
            return stringa
        elif stringa == 'CO':
            stringa1 = int(self.leggi('lastID').rsplit()[0]) + 1
            stringa = stringa + str(stringa1)
            self.salva(str(stringa1), 'lastID')
            return stringa

    def leggi(self,file = 'Credenziali',n = 20):
        if os.path.isfile(f'GestoreStudioLegale/Dati/{file}.pickle'):
            with open(f'GestoreStudioLegale/Dati/{file}.pickle', 'r') as f:
                if n == 0 :
                    return f.read()
                stringa1 = f.read(n)
                return str(stringa1)

    def loadAppuntamenti(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
            with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'rb') as f:
                self.appuntamenti = list(pickle.load(f))
                return self.appuntamenti

    def loadAvvocati(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                self.avvocati = list(pickle.load(f))
                return self.avvocati

    def loadClienti(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                self.clienti = list(pickle.load(f))
                return self.clienti

    def loadCorsiAggiornamento(self):
        if os.path.isfile('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle'):
            with open('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle', 'rb') as f:
                self.corsiAggiornamento = list(pickle.load(f))
                return self.corsiAggiornamento

    def loadParcelle(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
            with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                self.parcelle = list(pickle.load(f))
                return self.parcelle

    def loadUdienze(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Udienze.pickle'):
            with open('GestoreStudioLegale/Dati/Udienze.pickle', 'rb') as f:
                self.udienze = list(pickle.load(f))
                return self.udienze

    def rewindButton(self, rewind):
        button = QPushButton("Indietro")
        button.setFont(QFont('Arial', 10))
        button.clicked.connect(rewind)
        button.setSizePolicy(150, 50)
        return button

    def salva(self, stringa,file='Credenziali'):
        if os.path.isfile(f'GestoreStudioLegale/Dati/{file}.pickle'):
            with open(f'GestoreStudioLegale/Dati/{file}.pickle', 'w') as f:
                f.write(stringa)
                f.write('\n')

    def salvaAppend(self, stringa,file='Credenziali'):
        if os.path.isfile(f'GestoreStudioLegale/Dati/{file}.pickle'):
            with open(f'GestoreStudioLegale/Dati/{file}.pickle', 'a') as f:
                f.write(stringa)
                f.write('\n')