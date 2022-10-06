from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout, QScrollArea, \
    QListWidget, QScrollBar, QListWidgetItem, QLabel, QMainWindow, QLineEdit

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAvvocato.RicercaAppuntamentoA import RicercaAppuntamentoA
from GestoreStudioLegale.Viste.VisteAvvocato.VistaEliminaAppuntamentoA import VistaEliminaAppuntamentoA
from GestoreStudioLegale.Servizi.Appuntamento import *
import pickle
import os

from GestoreStudioLegale.Viste.VisteAvvocato.VisteInserisciAppuntamentoA import VisteInserisciAppuntamentoA


class VistaHomeAppuntamentiA(QMainWindow):
    appuntamentiList = []

    def __init__(self, parent=None):
        super(VistaHomeAppuntamentiA, self).__init__(parent)
        self.initUI()

    def initUI(self):
        tool = Tools()
        self.cWidget = QWidget()  # contiene tutto
        self.outerLayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box

        self.grid = QGridLayout()

        self.outerLayout.addWidget(tool.rewindButton(self.rewind), 1)
        self.outerLayout.addLayout(self.button_layout, 1)
        self.outerLayout.addWidget(self.scroll, 8)
        self.button_layout.addWidget(tool.createButton("Inserisci", self.aggiungiAppuntamento))
        self.button_layout.addWidget(tool.createButton("Cerca", self.cercaAppuntamento))
        self.cWidget.setLayout(self.outerLayout)
        self.getDatiAp()

        self.widget.setLayout(self.grid)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.cWidget)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Appuntamenti')
        self.show()

    def aggiungiAppuntamento(self):
        self.vistaAggiuntaA = VisteInserisciAppuntamentoA()
        self.vistaAggiuntaA.show()
        self.close()

    def cercaAppuntamento(self):
        self.vistaAvvocatoR = RicercaAppuntamentoA()
        self.vistaAvvocatoR.show()
        self.close()

    def aggiornaAppuntamento(self, appuntamento):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaAggiornaAppuntamentoA import VistaAggiornaAppuntamentoA
        self.vistaAggiorna = VistaAggiornaAppuntamentoA()
        self.vistaAggiorna.appuntamento = appuntamento
        self.vistaAggiorna.show()
        self.close()

    def rimuoviAppuntamento(self, id):
        self.subWindow = VistaEliminaAppuntamentoA()
        self.subWindow.setData(id)
        self.subWindow.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAvvocato import VistaHomeAvvocato
        self.vistaHome = VistaHomeAvvocato()
        self.vistaHome.show()
        self.close()

    def loadDateAp(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
            with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'rb') as f:
                self.appuntamentiList = list(pickle.load(f))

    def getDatiAp(self):
        self.loadDateAp()
        tool = Tools()
        i = 0
        for appuntamento in self.appuntamentiList:
            label = QLabel()
            label.setText(
                'Appuntamento: ' + '\n' + 'TIPO PROCEDIMENTO: ' + f"{appuntamento.getDatiAppuntamento()['Tipo Procedimento']}" + '\n' + 'ID: ' + f"{appuntamento.getDatiAppuntamento()['ID']}" + '\n' + 'DATA E ORA INIZIO: ' + f"{appuntamento.getDatiAppuntamento()['Data e Ora Inizio']}" + '\n' + 'DATA E ORA FINE: ' + f"{appuntamento.getDatiAppuntamento()['Data e Ora Fine']}")
            label.setGeometry(QRect(0, 0, 350, 20))
            label.setFont(QFont('Arial', 10))
            label.setStyleSheet("border: 1px solid black;")
            print("ciao2")
            self.grid.addWidget(label,i,1,1,2)
            i += 1
            self.grid.addWidget(tool.createButton("Modifica", lambda checked,  a = appuntamento: self.aggiornaAppuntamento(a)), i, 1)
            print("yugdbskjavsu")
            self.grid.addWidget(
                tool.createButton("Elimina", lambda checked, a = appuntamento.getDatiAppuntamento()['ID']: self.rimuoviAppuntamento(a)), i, 2)
            i += 1

    def getNum(self):
        n = 0
        self.loadDateAp()
        for appuntamento in self.appuntamentiList:
            n += 1
        return n
