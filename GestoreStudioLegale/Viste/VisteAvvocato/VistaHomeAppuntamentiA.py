from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout, QScrollArea, \
    QListWidget, QScrollBar, QListWidgetItem, QLabel, QMainWindow

from GestoreStudioLegale.Utilities.Utilities import Tools
import pickle
import os


class VistaHomeAppuntamentiA(QMainWindow):

    appuntamentiList = []
    def __init__(self):
        #super(VistaHomeAppuntamentiA, self).__init__(parent)
        super().__init__()
        self.initUI()

    def initUI(self):
        tool = Tools()
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        for i in range(1, self.getNum()):
            label = QLabel()
            print("ciao")
            label.setText('Appuntamento: '+'\n'+ 'TIPO PROCEDIMENTO: '+f"{self.getDatiAp()['Tipo Procedimento']}"+'ID: '+f"{self.getDatiAp()['ID']}"+'\n'+'DATA E ORA INIZIO: '+f"{self.getDatiAp()['Data e Ora Inizio']}"+'\n'+'DATA E ORA FINE'+f"{self.getDatiAp()['Data e Ora Fine']}")
            print("ciao2")
            self.vbox.addWidget(label)

        #self.vbox.addWidget(tool.rewindButton(self.rewind), 0, 0)
        self.widget.setLayout(self.vbox)

        # Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Scroll Area Demonstration')
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
        print("ciao4")
        for appuntamento in self.appuntamentiList:
            print("ciao7")
            if str(appuntamento) == str(tool.leggi()).rsplit()[0]:
                print("ciao5")
                return appuntamento.getDatiAppuntamento()

    def getNum(self):
        n = 0
        self.loadDateAp()
        for appuntamento in self.appuntamentiList:
            n+=1
        return n
