import datetime
import os
import pickle

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox, QComboBox, \
    QCalendarWidget
#from datetime import datetime, timedelta, time
from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
from GestoreStudioLegale.Servizi.Parcella import Parcella
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeParcelle import VistaHomeParcelle


class VistaAggiornaParcella(QWidget):

    cliente = Cliente()
    tool = Tools()
    parcella = Parcella()
    parcelleList = tool.loadParcelle()

    def __init__(self,parent = None):
        super(VistaAggiornaParcella, self).__init__(parent)
        tool = Tools()
        self.gestore = GestoreSistema()
        self.setWindowTitle('Modifica Parcella')
        self.resize(500, 120)
        self.layout = QGridLayout()
        self.layout.addWidget(tool.rewindButton(self.rewind), 0, 0)

        self.createLine('intestatario', 1, 'o')
        self.createLine('importo', 2, 'o')

        self.confirmButton = QPushButton()
        self.confirmButton = self.tool.createButton('Conferma Parcella', self.confermaParcella)

        self.layout.addWidget(self.confirmButton, 3, 0, 1, 2)
        self.setLayout(self.layout)

    def createLine(self, name, n, l):
        self.labelName = QLabel(f'<font size="4"> {name} </font>')
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText(f'Inserisci nuov{l} {name.lower()}')
        self.layout.addWidget(self.labelName, n, 0)
        self.layout.addWidget(self.lineEdit, n, 1)

    def rewind(self):
        self.vistaHome = VistaHomeParcelle()
        self.vistaHome.show()
        self.close()

    def confermaParcella(self):
        i=0
        item = self.layout.itemAtPosition(i + 1, 1).widget()
        for parcella in self.parcelleList:
            if parcella.ID == self.parcella.ID:
               importoAggiornato = self.layout.itemAtPosition(2, 1).widget().text()
               intestatarioAggiornato = self.layout.itemAtPosition(1, 1).widget().text()
               #print(item.text())
               print(importoAggiornato)
               print(intestatarioAggiornato)
               #parcella.aggiornaParcella(parcella.Cliente, parcella.identificativo, importoAggiornato, intestatarioAggiornato )
               parcella.intestatario = intestatarioAggiornato
               parcella.importo = importoAggiornato
               #print(self.layout.itemAtPosition(2, 1).widget().text())
            if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
                    with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'wb') as f1:
                        pickle.dump(self.parcelleList, f1, pickle.HIGHEST_PROTOCOL)
                    self.conferma()

    def conferma(self):
        msg = QMessageBox()
        msg.setWindowTitle("Parcella confermata")
        msg.setText("La sua parcella è stata modificata con successo")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        self.vistaPrima = VistaHomeParcelle()
        self.vistaPrima.show()
        self.close()

    def problema(self):
        msg = QMessageBox()
        msg.setWindowTitle("ERRORE")
        msg.setText("Non è possibile modificarla con questi dati, riprovi")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        self.vistaPrec = VistaHomeParcelle()
        self.vistaPrima.show()
        self.close()