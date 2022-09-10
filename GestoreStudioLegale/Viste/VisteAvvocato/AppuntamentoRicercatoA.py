from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout, QScrollArea, \
    QListWidget, QScrollBar, QListWidgetItem, QLabel, QMainWindow, QLineEdit

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAvvocato.VistaEliminaAppuntamentoA import VistaEliminaAppuntamentoA
from GestoreStudioLegale.Servizi.Appuntamento import *
import pickle
import os


class AppuntamentoRicercatoA(QMainWindow):
    appuntamentiList = []
    app = Appuntamento()

    def __init__(self, parent=None):
        super(AppuntamentoRicercatoA, self).__init__(parent)
        # super()._init_()
        self.initUI()

    def initUI(self):
        tool = Tools()
        self.cWidget = QWidget()  # contiene tutto
        self.outerLayout = QVBoxLayout()
        #self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box

        self.grid = QGridLayout()

        self.outerLayout.addWidget(tool.rewindButton(self.rewind), 1)
        self.outerLayout.addWidget(self.scroll, 9)
        self.cWidget.setLayout(self.outerLayout)
        self.getDatiAp()

        #self.supWidget = QWidget()

        # button_layout2.addWidget(self.createButton("Modifica", self.aggiornaAppuntamento))
        # button_layout2.addWidget(self.createButton("Rimuovi", self.rimuoviAppuntamento))
        #self.supWidget.setLayout(self.button_layout2)

        # self.vbox.addWidget(tool.rewindButton(self.rewind))
        self.widget.setLayout(self.grid)

        # Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.cWidget)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Appuntamenti')
        self.show()

    '''def createButton(self, nome, on_click):
        button = QPushButton(nome)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setFont(QFont('Arial', 10))
        button.clicked.connect(on_click)
        #button.setSizePolicy(150, 50)
        return button'''

    def aggiungiAppuntamento(self):
        pass

    def aggiornaAppuntamento(self):
        pass

    def rimuoviAppuntamento(self, id):
        self.subWindow = VistaEliminaAppuntamentoA()
        self.subWindow.setData(id)
        self.subWindow.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.RicercaAppuntamentoA import RicercaAppuntamentoA
        self.vistaAvvocatoR = RicercaAppuntamentoA()
        self.vistaAvvocatoR.show()

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
            print("ciao")
            label.setText(
                'Appuntamento: ' + '\n' + 'TIPO PROCEDIMENTO: ' + f"{appuntamento.getDatiAppuntamento()['Tipo Procedimento']}" + '\n' + 'ID: ' + f"{appuntamento.getDatiAppuntamento()['ID']}" + '\n' + 'DATA E ORA INIZIO: ' + f"{appuntamento.getDatiAppuntamento()['Data e Ora Inizio']}" + '\n' + 'DATA E ORA FINE' + f"{appuntamento.getDatiAppuntamento()['Data e Ora Fine']}")
            label.setGeometry(QRect(0, 0, 350, 20))
            label.setFont(QFont('Arial', 10))
            label.setStyleSheet("border: 1px solid black;")
            print("ciao2")
            self.grid.addWidget(label,i,1,1,2)
            i += 1
            self.grid.addWidget(tool.createButton("Modifica", self.aggiornaAppuntamento), i, 1)
            self.grid.addWidget(
                tool.createButton("Elimina", lambda: self.rimuoviAppuntamento(self.getDatiAp()['ID'])), i, 2)
            i += 1

            # print("ciao56")
            # if appuntamento.Avvocato.codiceFiscale == str(tool.leggi()).rsplit()[0]:
            # if 'jhsdkcdks' == str(tool.leggi(n=0)).rsplit()[0]:
            # if 'jhsdkcdks' == str(tool.leggi(n=0)).rsplit()[0]:

            # if 'djskorfl' == str(tool.leggi(n=0)).rsplit()[0]:
            # print(appuntamento)
            # print("fatto")
            # return appuntamento.getDatiAppuntamento()

            print("ciao56")
            if appuntamento.Avvocato.codiceFiscale == str(tool.leggi()).rsplit()[0]:
            #if 'jhsdkcdks' == str(tool.leggi(n=0)).rsplit()[0]:
            # if 'jhsdkcdks' == str(tool.leggi(n=0)).rsplit()[0]:
            #if 'djskorfl' == str(tool.leggi(n=0)).rsplit()[0]:
                print(appuntamento)
                print("fatto")
                return appuntamento.getDatiAppuntamento()

    def setData(self,appuntamento):
        self.appuntamento = appuntamento