
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox

from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaAggiungiCliente(QWidget):

    cliente = Cliente()

    def __init__(self,parent = None):
        super(VistaAggiungiCliente, self).__init__(parent)

        tool = Tools()
        self.gestore = GestoreSistema()
        self.setWindowTitle('Modifica cliente')
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
        list = []
        print(item.text() == "")
        print(f"sh{item.text()}it")
        while (item.text() != "" and i < 8):
            x = str(item.text())
            print("88888")
            list[i] = x
            print("88888")
            i+=1
            item = self.layout.itemAtPosition(i+1, 1).widget()

        if len(list) < 8:
            self.error("Devi riempire tutti gli spazi per potrìer creare un nuovo cliente")
            return

        x = list[3]
        y = x[2] != "/" and x[5] != '/'
        z = x.split("/")
        y1 = z[0].isdigit() and z[1].isdigit() and z[2].isdigit()
        if y:
            self.error("Erore formato data di nascita, il formato è DD/MM/YYYY")
            return

        if not y1:
            self.error("Erore formato data di nascita devi inserire dei numeri e non delle lettere")
            return

        '''x = list[5]
        if not len(str(x)) == 10 and str(x).isdigit():
            self.error("Il numero di telefono deve essere di 10 numeri")
            return'''

        x = list[6]
        if not len(str(x)) == 10 and str(x).isdigit():
            self.error("Il numero di telefono deve essere di 10 numeri")
            return

        corsiAgg = []
        appuntamenti = []
        parcelle = []
        udienze = []

        Cliente.creaCliente(list[2], list[1],corsiAgg,list[3], list[4],list[5], list[6],list[7], appuntamenti, parcelle,
                            list[0], udienze)

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