from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QScrollArea, QMainWindow
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools

class VistaVisualizzaClienti(QMainWindow):

    clientiList = []

    def __init__(self, parent=None):
        super(VistaVisualizzaClienti, self).__init__(parent)
        tool = Tools()
        self.grifLayout = QGridLayout()
        self.scroll = QScrollArea()
        self.widget = QWidget()
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
        self.setCentralWidget(self.scroll)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(700, 600)
        self.setWindowTitle("Clienti")

    def loadDateC(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                self.clientiList = list(pickle.load(f))

    def getDatiC(self):
        self.loadDateC()
        i=0
        print("222")
        for cliente in self.clientiList:
            textLabel = QLabel()
            textLabel.setText(
                'Cliente: ' + '\n' + 'NOME: ' + f"{cliente.getDatiCliente()['Nome']}" + '\n' + 'COGNOME: ' + f"{cliente.getDatiCliente()['Cognome']}" + '\n' + 'ID: ' + f"{cliente.getDatiCliente()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{cliente.getDatiCliente()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{cliente.getDatiCliente()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{cliente.getDatiCliente()['Numero telefono']}")
            textLabel.setGeometry(QRect(0, 0, 350, 20))
            textLabel.setFont(QFont('Arial', 10))
            textLabel.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(textLabel,i,1)
            i+=1


    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeAdmin import VistaHomeAdmin
        self.vistaHome = VistaHomeAdmin()
        self.vistaHome.show()
        self.close()