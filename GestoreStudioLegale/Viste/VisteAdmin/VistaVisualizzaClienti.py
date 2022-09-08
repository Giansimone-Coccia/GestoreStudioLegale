from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QScrollArea, QMainWindow, QGroupBox, QPushButton, \
    QSizePolicy
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAdmin.VistaEliminaCliente import VistaEliminaCliente
from GestoreStudioLegale.Servizi.Cliente import *

class VistaVisualizzaClienti(QMainWindow):

    clientiList = []

    def __init__(self, parent=None):
        super(VistaVisualizzaClienti, self).__init__(parent)
        tool = Tools()
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.grifLayout = QGridLayout()
        self.grifLayout.addWidget(tool.createButton("Aggiungi Cliente", self.aggiungiCliente), 0, 1,1,2)
        self.grifLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        textLabel = QLabel()
        textLabel.setText("Di seguito la lista dei clienti")
        textLabel.setGeometry(QRect(0, 0, 200, 150))
        textLabel.setFont(QFont('Arial', 10))
        self.getDatiC()
        self.widget.setLayout(self.grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(700, 600)
        self.setCentralWidget(self.scroll)
        self.setWindowTitle("Clienti")

    def loadDateC(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                self.clientiList = list(pickle.load(f))

    def getDatiC(self):
        self.loadDateC()
        tool=Tools()
        i=2
        print("222")
        for cliente in self.clientiList:
            #widget =QWidget()
            #layout=QGridLayout()
            textLabel = QLabel()
            textLabel.setText('Cliente: ' + '\n' + 'NOME: ' + f"{cliente.getDatiCliente()['Nome']}" + '\n' + 'COGNOME: ' + f"{cliente.getDatiCliente()['Cognome']}" + '\n' + 'ID: ' + f"{cliente.getDatiCliente()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{cliente.getDatiCliente()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{cliente.getDatiCliente()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{cliente.getDatiCliente()['Numero telefono']}")
            textLabel.setGeometry(QRect(0, 0, 350, 20))
            textLabel.setFont(QFont('Arial', 10))
            textLabel.setStyleSheet("border: 1px solid black;")
            #layout.addWidget(textLabel,0,1)
            #layout.setRowStretch(0,2)
            #widget.setLayout(layout)
            self.grifLayout.addWidget(textLabel,i,1,1,2)
            i+=1
            '''
            button = QPushButton("Elimina")
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.setFont(QFont('Arial', 10))
            button.setCheckable(True)
            button.toggle()'''
            self.grifLayout.addWidget(tool.createButton("Aggiorna",self.aggiornaCliente),i,1)
            self.grifLayout.addWidget(tool.createButton("Elimina",lambda: self.eliminaCliente(cliente.getDatiCliente()['Id'],cliente)),i, 2)
            '''
            button.clicked.connect(self.eliminaCliente(cliente.getDatiCliente()['Id']))
            self.grifLayout.addWidget(button,i, 2)'''
            i+=1

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeAdmin import VistaHomeAdmin
        self.vistaHome = VistaHomeAdmin()
        self.vistaHome.show()
        self.close()

    def aggiungiCliente(self):
        pass

    def eliminaCliente(self,id,cliente):
        self.subWindow =VistaEliminaCliente()
        self.subWindow.setData(id,cliente)
        self.subWindow.show()
        self.close()


    def aggiornaCliente(self):
        pass