import os
import pickle

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox
from datetime import datetime, timedelta, time
from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaCreaCliente(QWidget):

    cliente = Cliente()

    def __init__(self,parent = None):
        super(VistaCreaCliente, self).__init__(parent)

        tool = Tools()
        self.gestore = GestoreSistema()
        self.setWindowTitle('Aggiungi cliente')
        self.resize(500, 120)
        self.layout = QGridLayout()
        self.layout.addWidget(tool.rewindButton(self.rewind), 0, 0)

        self.createLine('Nome',1)
        self.createLine('Cognome', 2)
        self.createLine('Codice fiscale', 3)
        self.createLine('Data nascita', 4)
        self.createLine('Email', 5)
        self.createLine('Id', 6)
        self.createLine('Numero di telefono', 7)
        self.createLine('Password', 8)

        self.buttonLogin = QPushButton('conferma')
        self.layout.addWidget(self.buttonLogin, 9, 0, 1, 2)
        self.buttonLogin.clicked.connect(self.invio)
        self.setLayout(self.layout)

    def createLine(self,name,n):
        self.labelName = QLabel(f'<font size="4"> {name} </font>')
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText(f'Inserisci {name.lower()}')
        self.layout.addWidget(self.labelName, n, 0)
        self.layout.addWidget(self.lineEdit, n, 1)

    def error(self, name):
        self.msg = QMessageBox()
        self.msg.setWindowTitle('ERRORE')
        self.msg.setText(name)
        self.msg.exec()

    def invio(self):
        i = 0
        item = self.layout.itemAtPosition(i+1, 1).widget()
        cliente = Cliente()

        while i < 8:
            if item.text() == "":
                self.error("Devi riempire tutti gli spazi per poter creare un nuovo cliente")
                return
            i+=1
            item = self.layout.itemAtPosition(i+1, 1).widget()

        item = self.layout.itemAtPosition(4, 1).widget()
        x = item.text()
        date = None
        if (len(x) > 6):
            y = x[2] != "/" and x[5] != '/'
            print("yup")
            if y:
                self.error("Erore formato data di nascita, il formato è DD/MM/YYYY")
                return
            else:
                try:
                    print("shit")
                    date = datetime.strptime(item.text(), "%d/%m/%Y")
                    print(date)
                    if date > datetime.now():
                        self.error("Data non valida inserita, la data che hai inserito è futura")
                        return
                except ValueError:
                    self.error("Data non valida inserita")
                    return
        else:
            self.error("Erore formato data di nascita, il formato è DD/MM/YYYY")
            return

        z = x.split("/")
        y1 = z[0].isdigit() and z[1].isdigit() and z[2].isdigit()

        if not y1:
            self.error("Erore formato data di nascita devi inserire dei numeri e non delle lettere")
            return

        item = self.layout.itemAtPosition(6, 1).widget()
        if cliente.ricercaUtilizzatoreId(item.text()) is not None:
            self.error("Esiste già un cliente con questo id")
            return

        item = self.layout.itemAtPosition(7, 1).widget()
        x = item.text()
        print(str(x).isdigit())
        if not (len(str(x)) == 10 and str(x).isdigit()):
            self.error("Il numero di telefono deve essere di 10 numeri")
            return

        corsiAgg = []
        appuntamenti = []
        parcelle = []
        udienze = []
        tool =Tools()

        cliente.creaCliente(self.layout.itemAtPosition(3, 1).widget().text(), self.layout.itemAtPosition(2, 1).widget().text(),
                            corsiAgg,date.strftime("%d/%m/%Y"), self.layout.itemAtPosition(5, 1).widget().text(),
                            self.layout.itemAtPosition(6, 1).widget().text(), self.layout.itemAtPosition(7, 1).widget().text(),
                            self.layout.itemAtPosition(8, 1).widget().text(), appuntamenti, parcelle,
                            self.layout.itemAtPosition(1, 1).widget().text(), udienze)

        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                self.avvocatiList = list(pickle.load(f))
        for avvocato in self.avvocatiList:
            if avvocato.codiceFiscale == tool.leggi().rsplit()[0]:
                avvocato.clienti.append(cliente.ricercaUtilizzatoreId(self.layout.itemAtPosition(6, 1).widget().text()))
                avvocato.aggiornaAvvocato()
                msg = QMessageBox()
                msg.setWindowTitle('Cliente aggiunto')
                msg.setText('Cliente aggiunto e creato con successo')
                msg.exec()
                self.close()
                self.rewind()




    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaAggiungiCliente import VistaAggiungiCliente
        self.vistaAg = VistaAggiungiCliente()
        self.vistaAg.show()
        self.close()