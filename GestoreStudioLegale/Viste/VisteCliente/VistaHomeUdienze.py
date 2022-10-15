from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QScrollArea, QMainWindow

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaHomeUdienze(QMainWindow):

    udienzeList = []
    clientiList = []
    tool = Tools()

    def __init__(self, parent=None):
        super(VistaHomeUdienze, self).__init__(parent)
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        textLabel1 = QLabel()
        textLabel2 = QLabel()
        textLabel1.setText("Di seguito la lista delle udienze con le informazioni relative al cliente")
        textLabel1.setGeometry(QRect(0, 0, 200, 150))
        textLabel1.setFont(QFont('Arial', 10))
        textLabel2.setText(
            'Cliente: ' + '\n' + 'NOME: ' + f"{self.getDatiC()['Nome']}" + '\n' + 'COGNOME: ' + f"{self.getDatiC()['Cognome']}" + '\n' + 'ID: ' + f"{self.getDatiC()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{self.getDatiC()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{self.getDatiC()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{self.getDatiC()['Numero telefono']}")
        textLabel2.setGeometry(QRect(0, 0, 350, 10))
        textLabel2.setFont(QFont('Arial', 10))
        textLabel2.setStyleSheet("border: 1px solid black;")
        self.gridLayout.addWidget(textLabel2, 1, 1)
        self.gridLayout.addWidget(textLabel1, 2, 1)
        self.getDatiU()
        self.widget.setLayout(self.gridLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)
        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Udienze')
        self.resize(800, 600)
        self.show()

    def getDatiU(self):
        tool = Tools()
        self.udienzeList = self.tool.loadUdienze()
        udienzeL = []
        i=3
        for udienza in self.udienzeList:
           if udienza.Cliente.codiceFiscale == str(self.tool.leggi()).rsplit()[0]:
              udienzeL.append(udienza)

        for u in udienzeL:
            label = QLabel()
            dataIn = u.getDatiUdienza()['Data e Ora Inizio'].strftime("%m/%d/%Y, %H:%M:%S")
            dataFin = u.getDatiUdienza()['Data e Ora Fine'].strftime("%m/%d/%Y, %H:%M:%S")
            label.setText(
                'Udienza: ' + '\n' + 'CITTA TRIBUNALE: ' + f"{u.getDatiUdienza()['Città Tribunale']}" + '\n' + 'TIPO TRIBUNALE: ' + f"{u.getDatiUdienza()['Tipo Tribunale']}" + '\n' + 'ID: ' + f"{u.getDatiUdienza()['ID']}" + '\n' + 'DATA ORA INIZIO: ' + f"{dataIn}" + '\n' + 'DATA ORA FINE: ' + f"{dataFin}")
            label.setGeometry(QRect(0, 0, 350, 20))
            label.setFont(QFont('Arial', 10))
            label.setStyleSheet("border: 1px solid black;")
            self.gridLayout.addWidget(label, i, 1, 1, 2)
            i += 1

    def aggiornaUdienza(self):
        pass

    def rimuoviUdienza(self):
        pass

    def getDatiC(self):
        self.clientiList = self.tool.loadClienti()
        for cliente in self.clientiList:
            if cliente.codiceFiscale == str(self.tool.leggi(n=0)).rsplit()[0]:
                return cliente.getDatiCliente()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteCliente.VistaHomeCliente import VistaHomeCliente
        self.vistaHome1 = VistaHomeCliente()
        self.vistaHome1.show()
        self.close()