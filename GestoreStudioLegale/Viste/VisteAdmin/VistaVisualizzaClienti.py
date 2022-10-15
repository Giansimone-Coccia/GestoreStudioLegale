from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QScrollArea, QMainWindow, QHBoxLayout
import os

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAdmin.VistaAggiornaCliente import VistaAggiornaCliente
from GestoreStudioLegale.Viste.VisteAdmin.VistaAggiungiCliente import VistaAggiungiCliente
from GestoreStudioLegale.Viste.VisteAdmin.VistaEliminaCliente import VistaEliminaCliente
from GestoreStudioLegale.Servizi.Cliente import *
from GestoreStudioLegale.Viste.VisteAdmin.VistaRicercaCliente import VistaRicercaCliente


class VistaVisualizzaClienti(QMainWindow):

    clientiList = []

    def __init__(self, parent=None):
        super(VistaVisualizzaClienti, self).__init__(parent)
        tool = Tools()

        self.cWidget = QWidget()
        self.outerLayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()
        self.widget = QWidget()

        self.grifLayout = QGridLayout()

        self.outerLayout.addWidget(tool.rewindButton(self.rewind), 1)
        self.outerLayout.addLayout(self.button_layout, 1)
        self.outerLayout.addWidget(self.scroll, 8)
        self.button_layout.addWidget(tool.createButton("Inserisci",self.aggiungiCliente))
        self.button_layout.addWidget(tool.createButton("Cerca", self.cercaCliente))
        self.cWidget.setLayout(self.outerLayout)

        self.getDatiC()
        self.widget.setLayout(self.grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.cWidget)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(800, 600)
        self.setWindowTitle("Clienti")

    def loadDateC(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                self.clientiList = list(pickle.load(f))

    def getDatiC(self):
        self.loadDateC()
        tool=Tools()
        i=1
        for cliente in self.clientiList:
            textLabel = QLabel()
            textLabel.setText('Cliente: ' + '\n' + 'NOME: ' + f"{cliente.getDatiCliente()['Nome']}" + '\n' + 'COGNOME: ' + f"{cliente.getDatiCliente()['Cognome']}"+ '\n'+ 'DATA DI NASCITA: ' + f"{cliente.getDatiCliente()['Data nascita']}" + '\n' + 'ID: ' + f"{cliente.getDatiCliente()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{cliente.getDatiCliente()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{cliente.getDatiCliente()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{cliente.getDatiCliente()['Numero telefono']}"+ '\n' + 'PASSWORD: ' + f"{cliente.getDatiCliente()['Password']}")
            textLabel.setGeometry(QRect(0, 0, 350, 20))
            textLabel.setFont(QFont('Arial', 10))
            textLabel.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(textLabel,i,1,1,2)
            i+=1

            self.grifLayout.addWidget(tool.createButton("Aggiorna", lambda checked, a=cliente: self.aggiornaCliente(a)),i,1)
            self.grifLayout.addWidget(tool.createButton("Elimina", lambda checked, b=cliente.getDatiCliente()['Id']: self.eliminaCliente(b)),i,2)
            i+=1

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeAdmin import VistaHomeAdmin
        self.vistaHome = VistaHomeAdmin()
        self.vistaHome.show()
        self.close()

    def aggiungiCliente(self):
        self.subWindow = VistaAggiungiCliente()
        self.subWindow.show()
        self.close()

    def eliminaCliente(self,id):
        self.subWindow = VistaEliminaCliente()
        self.subWindow.setData(id)
        self.subWindow.show()
        self.close()

    def cercaCliente(self):
        self.subWindow = VistaRicercaCliente()
        self.subWindow.show()
        self.close()

    def aggiornaCliente(self,cliente):
        self.subWindow = VistaAggiornaCliente()
        self.subWindow.setData(cliente)
        self.subWindow.show()
        self.close()
