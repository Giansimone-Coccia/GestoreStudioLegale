import os
import re

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
    corsiAggiornamento = []

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

    def createButton(self, nome, on_click,dim=10,method2 = 0):#,baseS=int(160),heightS=int(90),maxBase=int(160*1.5),maxHeight=int(90*2)):
        button = QPushButton(nome)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setFont(QFont('Arial', dim))
        #button.setBaseSize(baseS,heightS)
        #button.setMaximumSize(maxBase,maxHeight)
        button.clicked.connect(on_click)
        if(method2 != 0):
            button.clicked.connect(method2)
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

    def loadCorsiAggiornamento(self):
        if os.path.isfile('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle'):
            with open('GestoreStudioLegale/Dati/CorsiAggiornamento.pickle', 'rb') as f:
                self.corsiAggiornamento = list(pickle.load(f))
                return self.corsiAggiornamento

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

    def check(self,email):
        regex = '^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, email) and email.endswith("@gmail.com")):
            print("Valid Email")
            return True
        else:
            print("Invalid Email")
            return False