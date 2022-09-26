
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox
from datetime import datetime, timedelta, time
from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaAggiungiAvvocato(QWidget):

    cliente = Cliente()

    def __init__(self,parent = None):
        super(VistaAggiungiAvvocato, self).__init__(parent)

        tool = Tools()
        self.gestore = GestoreSistema()
        self.setWindowTitle('Modifica avvocato')
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
        avvocato = Avvocato()

        while i < 8:
            if item.text() == "":
                self.error("Devi riempire tutti gli spazi per poter creare un nuovo cliente")
                return
            i+=1
            item = self.layout.itemAtPosition(i+1, 1).widget()

        item = self.layout.itemAtPosition(4, 1).widget()
        x = item.text()
        date = None
        if(len(x)>5):
            y = x[2] != "/" and x[5] != '/'
            if y:
                self.error("Erore formato data di nascita, il formato è DD/MM/YYYY")
                return
            else:
                try:
                    date = datetime.datetime.strptime(item.text(), "%d/%m/%Y")
                    if date > datetime.now():
                        self.error("Data non valida inserita, la dat che hai inserito è futura")
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
        if avvocato.ricercaUtilizzatoreId(item.text()) is not None:
            self.error("Esiste già un cliente con questo id")
            return

        item = self.layout.itemAtPosition(7, 1).widget()
        x = item.text()
        print(str(x).isdigit())
        if not (len(str(x)) == 10 and str(x).isdigit()):
            self.error("Il numero di telefono deve essere di 10 numeri")
            return

        corsiAgg = []
        udienza = []
        clienti = []
        licenza = []
        appuntamento = []

        avvocato.creaAvvocato(self.layout.itemAtPosition(3, 1).widget().text(), self.layout.itemAtPosition(2, 1).widget().text(),
                              self.layout.itemAtPosition(1, 1).widget().text(),corsiAgg,date.strftime("%d/%m/%Y"), self.layout.itemAtPosition(5, 1).widget().text(),
                            self.layout.itemAtPosition(6, 1).widget().text(), self.layout.itemAtPosition(7, 1).widget().text(),
                            self.layout.itemAtPosition(8, 1).widget().text(), udienza, clienti,
                             licenza,appuntamento)

        self.msg = QMessageBox()
        self.msg.setWindowTitle('Creazione avvenuta con successo')
        self.msg.setText("Hai creato con successo un nuovo cliente")
        self.msg.exec()
        self.rewind()



    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaClienti import VistaVisualizzaClienti
        self.vistaVisualizza = VistaVisualizzaClienti()
        self.vistaVisualizza.show()
        self.close()