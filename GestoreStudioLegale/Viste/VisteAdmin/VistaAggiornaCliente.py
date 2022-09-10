from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox
from PyQt5 import QtCore as qtc

from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Servizi.Udienza import Udienza
from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento
from GestoreStudioLegale.Servizi.Parcella import Parcella
from GestoreStudioLegale.Sistema.CorsoAggiornamento import CorsoAggiornamento
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaAggiornaCliente(QWidget):

    cliente = Cliente()

    def __init__(self,parent = None):
        super(VistaAggiornaCliente, self).__init__(parent)

        tool = Tools()
        self.gestore = GestoreSistema()
        self.setWindowTitle('Modifica cliente')
        self.resize(500, 120)
        self.layout = QGridLayout()
        self.layout.addWidget(tool.rewindButton(self.rewind), 0, 0)

        self.createLine('Nome',1,'o')
        self.createLine('Cognome', 2, 'o')
        self.createLine('Codice fiscale', 3, 'o')
        self.createLine('Data nascita', 4, 'a')
        self.createLine('Email', 5, 'a')
        self.createLine('Id', 6, 'o')
        self.createLine('Numero di telefono', 7, 'o')
        self.createLine('Password', 8, 'a')

        self.buttonLogin = QPushButton('conferma')
        self.layout.addWidget(self.buttonLogin, 9, 0, 1, 2)
        #self.layout.setRowMinimumHeight(3, 75)
        self.buttonLogin.clicked.connect(self.invio)
        self.setLayout(self.layout)

    def createLine(self,name,n,l):
        self.labelName = QLabel(f'<font size="4"> {name} </font>')
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText(f'Inserisci nuov{l} {name.lower()}')
        self.layout.addWidget(self.labelName, n, 0)
        self.layout.addWidget(self.lineEdit, n, 1)

    def invio(self):

        self.string = ""
        print(self.cliente.getDatiCliente()["Data nascita"])

        appuntamenti = self.cliente.appuntamentoCliente
        parcelle = self.cliente.parcelle
        udienze =self.cliente.udienza
        corsiAgg = self.cliente.corsoAggiornamento

        Cliente.rimuoviCliente(self.cliente.getDatiCliente()["Id"])

        x = self.breve('nome',self.cliente.getDatiCliente()["Nome"],1,'o')
        if x is not False: self.cliente.nome = x
        else: return

        x = self.breve('cognome',self.cliente.getDatiCliente()["Cognome"],2,'o')
        if x is not False: self.cliente.cognome = x
        else: return

        x = self.breve('codice fiscale',self.cliente.getDatiCliente()["Codice fiscale"],3,'o')
        if x is not False:self.cliente.codiceFiscale = x
        else: return

        '''x = self.breve('data di nascita',self.cliente.getDatiCliente()["Data nascita"],4,'o')
        if x is not False: self.cliente.dataNascita = x
        else: return'''
        item = self.layout.itemAtPosition(4, 1).widget()
        if self.cliente.getDatiCliente()["Data nascita"] == item.text():
            self.error(f"Hai inseirto la stessa data di nascita")
            return
        elif self.cliente.getDatiCliente()["Data nascita"]!= item.text() and item.text() != "":
            x = item.text()
            y = x[2] != "/" and x[5] != '/'
            if y:
                self.msg = QMessageBox()
                self.msg.setWindowTitle('ERRORE')
                self.msg.setText("Eroore formato data di nascita, il formato è DD/MM/YYYY")
                self.msg.exec()
                return
            else:
                self.string += f"data di nascita, "
                self.cliente.dataNascita= x


        x = self.breve('email',self.cliente.getDatiCliente()["Email"],5,'a')
        if x is not False: self.cliente.email = x
        else: return

        x = self.breve('id',self.cliente.getDatiCliente()["Id"],6,'o')
        if x is not False: self.cliente.id = x
        else: return

        x = self.breve('numero di telefono',self.cliente.getDatiCliente()["Numero telefono"],7,'o')
        if x is not False: self.cliente.numeroTelefono = x
        else: return

        x = self.breve('password',self.cliente.getDatiCliente()["Password"],8,'a')
        if x is not False: self.cliente.password = x
        else: return

        self.string = self.string[:-2]
        print(self.cliente.nome)
        print(self.string)
        print(self.cliente.getDatiCliente())

        item = self.layout.itemAtPosition(1, 1).widget()
        print(item.text())
        cliente =Cliente()

        cliente.creaCliente(self.cliente.getDatiCliente()["Codice fiscale"],self.cliente.getDatiCliente()["Cognome"],corsiAgg,
                            self.cliente.getDatiCliente()["Data nascita"],self.cliente.getDatiCliente()["Email"],
                            self.cliente.getDatiCliente()["Id"],self.cliente.getDatiCliente()["Numero telefono"],
                            self.cliente.getDatiCliente()["Password"],appuntamenti,parcelle,
                            self.cliente.getDatiCliente()["Nome"],udienze)

        self.msg = QMessageBox()
        self.msg.setWindowTitle('Modifica avvenuta con successo')
        self.msg.setText(f"Hai modificato: {self.string}")
        self.msg.exec()
        self.rewind()


    def breve(self, nome, obj, n, l):
        item = self.layout.itemAtPosition(n, 1).widget()
        if obj == item.text():
            self.error(f"Hai inseirto l{l} stess{l} {nome}")
            return False
        elif obj != item.text() and item.text()!="":
            self.string += f"{nome}, "
            return item.text()
        if item.text() == "":
            return obj



    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaClienti import VistaVisualizzaClienti
        self.vistaVisualizza = VistaVisualizzaClienti()
        self.vistaVisualizza.show()
        self.close()

    def setData(self, cliente):
        self.cliente = cliente

    def error(self, name):
        self.msg = QMessageBox()
        self.msg.setWindowTitle('ERRORE')
        self.msg.setText(name)
        self.msg.exec()