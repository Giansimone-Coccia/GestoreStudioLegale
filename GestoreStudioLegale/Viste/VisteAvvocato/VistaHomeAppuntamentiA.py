from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout, QScrollArea, \
    QListWidget, QScrollBar, QListWidgetItem, QLabel, QMainWindow, QLineEdit

from GestoreStudioLegale.Utilities.Utilities import Tools
import pickle
import os


class VistaHomeAppuntamentiA(QMainWindow):
    appuntamentiList = []

    def __init__(self, parent=None):
        super(VistaHomeAppuntamentiA, self).__init__(parent)
        # super()._init_()
        self.initUI()

    def initUI(self):
        tool = Tools()
        self.cWidget = QWidget() #contiene tutto
        self.outerLayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.outerLayout.addWidget(tool.rewindButton(self.rewind),1)
        self.outerLayout.addLayout(self.button_layout,2)
        self.outerLayout.addWidget(self.scroll,7)
        self.button_layout.addWidget(self.createButton("Inserisci", self.aggiungiAppuntamento))
        self.button_layout.addWidget(self.createButton("Cerca", self.cercaAppuntamento))
        self.cWidget.setLayout(self.outerLayout)
        supWidget = QWidget()
        button_layout2 = QHBoxLayout()
        button_layout2.addWidget(self.createButton("Modifica", self.aggiornaAppuntamento))
        button_layout2.addWidget(self.createButton("Rimuovi", self.rimuoviAppuntamento))

        for i in range(1, self.getNum()):
            supWidget.setLayout(button_layout2)
            label = QLabel()
            print("ciao")
            label.setText(
                'Appuntamento: ' + '\n' + 'TIPO PROCEDIMENTO: ' + f"{self.getDatiAp()['Tipo Procedimento']}" + '\n' + 'ID: ' + f"{self.getDatiAp()['ID']}" + '\n' + 'DATA E ORA INIZIO: ' + f"{self.getDatiAp()['Data e Ora Inizio']}" + '\n' + 'DATA E ORA FINE' + f"{self.getDatiAp()['Data e Ora Fine']}")
            label.setFont(QFont('Arial', 10))
            print("ciao2")
            self.vbox.addWidget(label,9)
            self.vbox.addWidget(supWidget,1)


        # self.vbox.addWidget(tool.rewindButton(self.rewind))
        self.widget.setLayout(self.vbox)

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

    def cercaAppuntamento(self):
        pass

    def aggiornaAppuntamento(self):
        pass

    def rimuoviAppuntamento(self):
        pass

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
        for appuntamento in self.appuntamentiList:
            print("ciao56")
            if appuntamento.Avvocato.codiceFiscale == str(tool.leggi()).rsplit()[0]:
            # if 'jhsdkcdks' == str(tool.leggi(n=0)).rsplit()[0]:
            #if 'djskorfl' == str(tool.leggi(n=0)).rsplit()[0]:
                print(appuntamento)
                print("fatto")
                return appuntamento.getDatiAppuntamento()

    def getNum(self):
        n = 0
        self.loadDateAp()
        for appuntamento in self.appuntamentiList:
            n += 1
        return n

    def createButton(self, nome, on_click):
        button = QPushButton(nome)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setFont(QFont('Arial', 10))
        button.clicked.connect(on_click)
        return button