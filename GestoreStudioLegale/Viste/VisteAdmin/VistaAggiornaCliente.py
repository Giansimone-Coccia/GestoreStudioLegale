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
        self.layout.setRowMinimumHeight(3, 75)
        self.buttonLogin.clicked.connect(lambda: self.invio())
        self.setLayout(self.layout)

    def createLine(self,name,n,l):
        self.labelName = QLabel(f'<font size="4"> {name} </font>')
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText(f'Inserisci nuov{l} {name.lower()}')
        self.layout.addWidget(self.labelName, n, 0)
        self.layout.addWidget(self.lineEdit, n, 1)

    def invio(self):

        self.string = ""

        '''
        appuntamenti = []
        parcelle = []
        udienza = []
        corsiAgg = []

        appuntamenti = self.cliente.getDatiCliente["appuntamentoCliente"]
        parcelle = self.cliente.getDatiCliente['parcelle']
        udienze =self.cliente.getDatiCliente['Udienze']
        corsiAgg = self.cliente.getDatiCliente['Corso aggiornamento']'''

        GestoreSistema.rimuoviCliente(self.cliente.Id)

        if self.breve('nome',self.cliente.getDatiCliente()["Nome"],1,'o'):
            return
        if self.breve('cognome',self.cliente.getDatiCliente()["Cognome"],2,'o'):
            return
        if self.breve('codice fiscale',self.cliente.getDatiCliente()["Codice fiscale"],3,'o'):
            return
        if self.breve('data di nascita',self.cliente.getDatiCliente()["Data nascita"],4,'o'):
            return
        if self.breve('email',self.cliente.getDatiCliente()["Email"],5,'a'):
            return
        if self.breve('id',self.cliente.getDatiCliente()["Id"],6,'o'):
            return
        if self.breve('numero di telefono',self.cliente.getDatiCliente()["Numero telefono"],7,'o'):
            return
        if self.breve('password',self.cliente.getDatiCliente()["Password"],8,'a'):
            return

        self.string = self.string[:-2]
        print(self.string)
        print(self.cliente.getDatiCliente())

        #GestoreSistema.salvaCliente(self.cliente)

        '''Cliente.creaCliente(self.cliente.getDatiCliente()["Codice fiscale"],self.cliente.getDatiCliente()["Cognome"],corsiAgg,
                            self.cliente.getDatiCliente()["Data nascita"],self.cliente.getDatiCliente()["Email"],
                            self.cliente.getDatiCliente()["Id"],self.cliente.getDatiCliente()["Numero telefono"],
                            self.cliente.getDatiCliente()["Password"],appuntamenti,parcelle,
                            self.cliente.getDatiCliente()["Nome"],udienze)'''

        self.msg = QMessageBox()
        self.msg.setWindowTitle('Modifica avvenuta con successo')
        self.msg.setText(f"Hai modificato: {self.string}")
        self.msg.exec()
        self.rewind()


    def breve(self, nome, obj, n, l):
        item = self.layout.itemAtPosition(n, 1).widget()
        if obj == item.text():
            self.error(f"Hai inseirto l{l} stess{l} {nome}")
            return True
        elif obj != item.text() and item.text()!="":
            obj = item.text()
            self.string += f"{nome}, "
            return False



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