from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox

from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaAggiornaAvvocato(QWidget):

    avvocato = Avvocato()

    def __init__(self,parent = None):
        super(VistaAggiornaAvvocato, self).__init__(parent)

        tool = Tools()
        self.gestore = GestoreSistema()
        self.setWindowTitle('Modifica avvocato')
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
        print(self.avvocato.getDatiAvvocato()["Data nascita"])

        appuntamenti = self.avvocato.appuntamentoCliente
        parcelle = self.avvocato.parcelle
        udienze =self.avvocato.udienza
        corsiAgg = self.avvocato.corsoAggiornamento

        Avvocato.rimuoviAvvocato(self.avvocato.getDatiAvvocato()["Id"])

        x = self.breve('nome',self.avvocato.getDatiAvvocato()["Nome"],1,'o')
        if x is not False: self.avvocato.nome = x
        else: return

        x = self.breve('cognome',self.avvocato.getDatiAvvocato()["Cognome"],2,'o')
        if x is not False: self.avvocato.cognome = x
        else: return

        x = self.breve('codice fiscale',self.avvocato.getDatiAvvocato()["Codice fiscale"],3,'o')
        if x is not False:self.avvocato.codiceFiscale = x
        else: return

        '''x = self.breve('data di nascita',self.cliente.getDatiCliente()["Data nascita"],4,'o')
        if x is not False: self.cliente.dataNascita = x
        else: return'''
        item = self.layout.itemAtPosition(4, 1).widget()
        if self.avvocato.getDatiAvvocato()["Data nascita"] == item.text():
            self.error(f"Hai inseirto la stessa data di nascita")
            return
        elif str(self.avvocato.getDatiAvvocato()["Data nascita"])!= item.text() and item.text() != "":
            x = str(item.text())
            y = x[2] != "/" and x[5] != '/'
            z = x.split("/")
            y1 = z[0].isdigit() and z[1].isdigit() and z[2].isdigit()
            print("22222")
            if y:
                self.error("Erore formato data di nascita, il formato è DD/MM/YYYY")
                return
            elif y1:
                self.string += f"data di nascita, "
                self.avvocato.dataNascita= x
            else:
                self.error("Erore formato data di nascita devi inserire dei numeri e non delle lettere")
                return


        x = self.breve('email',self.avvocato.getDatiAvvocato()["Email"],5,'a')
        if x is not False: self.avvocato.email = x
        else: return

        x = self.breve('id',self.avvocato.getDatiAvvocato()["Id"],6,'o')
        if x is not False: self.avvocato.Id = x
        else: return

        item = self.layout.itemAtPosition(7, 1).widget()
        x = str(item.text())
        if str(self.avvocato.getDatiAvvocato()["Numero telefono"]) == item.text():
            self.error("Hai inseirto lo stesso numero di telefono")
            return
        elif str(self.avvocato.getDatiAvvocato()["Numero telefono"])!= item.text() and item.text() != "":
            if len(str(item.text())) == 10 and str(item.text()).isdigit() :
                self.string += f"numero di telefono, "
                self.avvocato.numeroTelefono = x
            else:
                self.error("Hai sbagliato il formato del numero di telefono, devi inserire 10 numeri")
                return


        x = self.breve('password',self.avvocato.getDatiAvvocato()["Password"],8,'a')
        if x is not False: self.avvocato.password = x
        else: return

        self.string = self.string[:-2]
        print(self.avvocato.nome)
        print(self.string)
        print(self.avvocato.getDatiAvvocato())

        item = self.layout.itemAtPosition(1, 1).widget()
        print(item.text())
        avvocato =Avvocato()

        avvocato.creaAvvocato(self.avvocato.getDatiAvvocato()["Codice fiscale"],self.avvocato.getDatiAvvocato()["Cognome"],corsiAgg,
                            self.avvocato.getDatiAvvocato()["Data nascita"],self.avvocato.getDatiAvvocato()["Email"],
                            self.avvocato.getDatiAvvocato()["Id"],self.avvocato.getDatiAvvocato()["Numero telefono"],
                            self.avvocato.getDatiAvvocato()["Password"],appuntamenti,parcelle,
                            self.avvocato.getDatiAvvocato()["Nome"],udienze)

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
        from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaAvvocati import VistaVisualizzaAvvocati
        self.vistaVisualizza = VistaVisualizzaAvvocati()
        self.vistaVisualizza.show()
        self.close()

    def setData(self, avvocato):
        self.avvocato = avvocato

    def error(self, name):
        self.msg = QMessageBox()
        self.msg.setWindowTitle('ERRORE')
        self.msg.setText(name)
        self.msg.exec()