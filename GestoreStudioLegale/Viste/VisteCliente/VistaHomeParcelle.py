from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QMainWindow, QScrollArea

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaHomeParcelle(QMainWindow):

    clientiList = []
    parcelleList = []
    tool = Tools()

    def __init__(self, parent=None):
        super(VistaHomeParcelle, self).__init__(parent)
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        textLabel1 = QLabel()
        textLabel2 = QLabel()
        textLabel1.setText("Di seguito la lista delle parcelle con le informazioni relative al cliente")
        textLabel1.setGeometry(QRect(0, 0, 200, 150))
        textLabel1.setFont(QFont('Arial', 10))
        textLabel2.setText('Cliente: '+'\n'+ 'NOME: '+f"{self.getDatiC()['Nome']}"+ '\n'+'COGNOME: '+f"{self.getDatiC()['Cognome']}"+'\n'+'ID: '+f"{self.getDatiC()['Id']}"+'\n'+'CODICE FISCALE: '+f"{self.getDatiC()['Codice fiscale']}"+'\n'+'EMAIL: '+f"{self.getDatiC()['Email']}"+'\n'+'NUMERO TELEFONO: '+f"{self.getDatiC()['Numero telefono']}")
        textLabel2.setGeometry(QRect(0, 0, 350, 10))
        textLabel2.setFont(QFont('Times', 10))
        textLabel2.setStyleSheet("border: 1px solid black;")
        self.gridLayout.addWidget(textLabel2, 1, 1)
        self.gridLayout.addWidget(textLabel1, 2, 1)
        self.getDatiP()
        self.widget.setLayout(self.gridLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(800, 600)
        self.setWindowTitle("Parcelle")
        self.show()

    def getDatiC(self):
        self.clientiList = self.tool.loadClienti()
        tool = Tools()
        for cliente in self.clientiList:
            if cliente.codiceFiscale == str(tool.leggi()).rsplit()[0]:
                    return cliente.getDatiCliente()

    def getDatiP(self):
        self.parcelleList = self.tool.loadParcelle()
        tool = Tools()
        parc = []
        i = 3
        for parcella in self.parcelleList:
            if parcella.Cliente.codiceFiscale == str(tool.leggi()).rsplit()[0]:
                parc.append(parcella)
        for p in parc:
            label = QLabel()
            label.setText(
                'Parcella: '+'\n'+ 'INTESTATARIO: '+f"{p.getDatiParcellaCliente()['intestatario']}"+ '\n'+'IMPORTO: '+f"{p.getDatiParcellaCliente()['importo']}"+'€'+'\n'+'ID: '+f"{p.getDatiParcellaCliente()['ID']}"+'\n'+'IDENTIFICATIVO: '+f"{p.getDatiParcellaCliente()['identificativo']}")
            label.setGeometry(QRect(0, 0, 350, 20))
            label.setFont(QFont('Arial', 10))
            label.setStyleSheet("border: 1px solid black;")
            self.gridLayout.addWidget(label, i, 1, 1, 2)
            i += 1

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteCliente.VistaHomeCliente import VistaHomeCliente
        self.vistaHome = VistaHomeCliente()
        self.vistaHome.show()
        self.close()
