from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QScrollArea, QMainWindow, QGroupBox
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAdmin.VistaAggiornaAvvocato import VistaAggiornaAvvocato
from GestoreStudioLegale.Viste.VisteAdmin.VistaAggiungiAvvocato import VistaAggiungiAvvocato
from GestoreStudioLegale.Viste.VisteAdmin.VistaEliminaAvvocato import VistaEliminaAvvocato


class VistaVisualizzaAvvocati(QMainWindow):

    avvocatiList = []

    def __init__(self, parent=None):
        super(VistaVisualizzaAvvocati, self).__init__(parent)
        tool = Tools()

        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.grifLayout = QGridLayout()

        self.grifLayout.addWidget(tool.createButton("Aggiungi", self.aggiungiAvvocato,baseS=160*3,maxBase=160*4), 0, 1,1,2)
        self.grifLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)

        self.getDatiA()
        self.widget.setLayout(self.grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(700, 600)
        self.setCentralWidget(self.scroll)
        self.setWindowTitle("Avvocati")

    def loadDateA(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                self.avvocatiList = list(pickle.load(f))

    def getDatiA(self):
        self.loadDateA()
        tool=Tools()
        i=2
        for avvocato in self.avvocatiList:
            textLabel = QLabel()
            textLabel.setText(
                'Avvocato: ' + '\n' + 'NOME: ' + f"{avvocato.getDatiAvvocato()['Nome']}" + '\n' + 'COGNOME: ' + f"{avvocato.getDatiAvvocato()['Cognome']}" + '\n'+ 'DATA DI NASCITA: ' + f"{avvocato.getDatiAvvocato()['Data nascita']}" + '\n' + 'ID: ' + f"{avvocato.getDatiAvvocato()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{avvocato.getDatiAvvocato()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{avvocato.getDatiAvvocato()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{avvocato.getDatiAvvocato()['Numero telefono']}")
            textLabel.setGeometry(QRect(0, 0, 350, 20))
            textLabel.setFont(QFont('Arial', 10))
            textLabel.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(textLabel,i,1,1,2)
            i+=1
            self.grifLayout.addWidget(tool.createButton("Aggiorna",lambda checked, a=avvocato: self.aggiornaAvvocato(a)),i,1)
            self.grifLayout.addWidget(tool.createButton("Elimina",lambda checked, b=avvocato.getDatiAvvocato()['Id']: self.eliminaAvvocato(b)),i, 2)
            i+=1

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeAdmin import VistaHomeAdmin
        self.vistaHome = VistaHomeAdmin()
        self.vistaHome.show()
        self.close()

    def aggiungiAvvocato(self):
        self.subWindow = VistaAggiungiAvvocato()
        self.subWindow.show()
        self.close()

    def eliminaAvvocato(self,id):
        self.subWindow = VistaEliminaAvvocato()
        self.subWindow.setData(id)
        self.subWindow.show()
        self.close()

    def aggiornaAvvocato(self,avvocato):
        self.subWindow = VistaAggiornaAvvocato()
        self.subWindow.setData(avvocato)
        self.subWindow.show()
        self.close()