from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QScrollArea, QMainWindow, QHBoxLayout
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAdmin.VistaAggiornaAvvocato import VistaAggiornaAvvocato
from GestoreStudioLegale.Viste.VisteAdmin.VistaAggiungiAvvocato import VistaAggiungiAvvocato
from GestoreStudioLegale.Viste.VisteAdmin.VistaEliminaAvvocato import VistaEliminaAvvocato
from GestoreStudioLegale.Viste.VisteAdmin.VistaRicercaAvvocato import VistaRicercaAvvocato


class VistaVisualizzaAvvocati(QMainWindow):

    avvocatiList = []
    tool = Tools()

    def __init__(self, parent=None):
        super(VistaVisualizzaAvvocati, self).__init__(parent)


        self.cWidget = QWidget()
        self.outerLayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()
        self.widget = QWidget()

        self.grifLayout = QGridLayout()

        self.outerLayout.addWidget(self.tool.rewindButton(self.rewind), 1)
        self.outerLayout.addLayout(self.button_layout, 1)
        self.outerLayout.addWidget(self.scroll, 8)
        self.button_layout.addWidget(self.tool.createButton("Inserisci", self.aggiungiAvvocato))
        self.button_layout.addWidget(self.tool.createButton("Cerca", self.cercaAvvocato))
        self.cWidget.setLayout(self.outerLayout)

        self.getDatiA()
        self.widget.setLayout(self.grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.cWidget)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(800, 600)
        self.setWindowTitle("Avvocati")

    def getDatiA(self):
        self.avvocatiList = self.tool.loadAvvocati()
        i=2
        for avvocato in self.avvocatiList:
            textLabel = QLabel()
            textLabel.setText(
                'Avvocato: ' + '\n' + 'NOME: ' + f"{avvocato.getDatiAvvocato()['Nome']}" + '\n' + 'COGNOME: ' + f"{avvocato.getDatiAvvocato()['Cognome']}" + '\n'+ 'DATA DI NASCITA: ' + f"{avvocato.getDatiAvvocato()['Data nascita']}" + '\n' + 'ID: ' + f"{avvocato.getDatiAvvocato()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{avvocato.getDatiAvvocato()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{avvocato.getDatiAvvocato()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{avvocato.getDatiAvvocato()['Numero telefono']}"+ '\n' + 'PASSWORD: ' + f"{avvocato.getDatiAvvocato()['Password']}")
            textLabel.setGeometry(QRect(0, 0, 350, 20))
            textLabel.setFont(QFont('Arial', 10))
            textLabel.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(textLabel,i,1,1,2)
            i+=1
            self.grifLayout.addWidget(self.tool.createButton("Aggiorna",lambda checked, a=avvocato: self.aggiornaAvvocato(a)),i,1)
            self.grifLayout.addWidget(self.tool.createButton("Elimina",lambda checked, b=avvocato.getDatiAvvocato()['Id']: self.eliminaAvvocato(b)),i, 2)
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

    def cercaAvvocato(self):
        self.subWindow = VistaRicercaAvvocato()
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