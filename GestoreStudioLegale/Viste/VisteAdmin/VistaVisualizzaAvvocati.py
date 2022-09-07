from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QScrollArea, QMainWindow, QGroupBox
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools

class VistaVisualizzaAvvocati(QMainWindow):

    avvocatiList = []

    def __init__(self, parent=None):
        super(VistaVisualizzaAvvocati, self).__init__(parent)
        tool = Tools()
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.grifLayout = QGridLayout()
        self.grifLayout.addWidget(tool.createButton("Aggiungi", self.rewind), 0, 1,1,2)
        self.grifLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        textLabel = QLabel()
        textLabel.setText("Di seguito la lista degli avvocati")
        textLabel.setGeometry(QRect(0, 0, 200, 150))
        textLabel.setFont(QFont('Arial', 10))
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
        print("222")
        for avvocato in self.avvocatiList:
            #widget =QWidget()
            #layout=QGridLayout()
            textLabel = QLabel()
            textLabel.setText(
                'Avvocato: ' + '\n' + 'NOME: ' + f"{avvocato.getDatiAvvocato()['Nome']}" + '\n' + 'COGNOME: ' + f"{avvocato.getDatiAvvocato()['Cognome']}" + '\n' + 'ID: ' + f"{avvocato.getDatiAvvocato()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{avvocato.getDatiAvvocato()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{avvocato.getDatiAvvocato()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{avvocato.getDatiAvvocato()['Numero telefono']}")
            textLabel.setGeometry(QRect(0, 0, 350, 20))
            textLabel.setFont(QFont('Arial', 10))
            textLabel.setStyleSheet("border: 1px solid black;")
            #layout.addWidget(textLabel,0,1)
            #layout.setRowStretch(0,2)
            #widget.setLayout(layout)
            self.grifLayout.addWidget(textLabel,i,1,1,2)
            i+=1
            self.grifLayout.addWidget(tool.createButton("Aggiorna",self.rewind),i,1)
            self.grifLayout.addWidget(tool.createButton("Elimina", self.rewind),i, 2)
            i+=1

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeAdmin import VistaHomeAdmin
        self.vistaHome = VistaHomeAdmin()
        self.vistaHome.show()
        self.close()
