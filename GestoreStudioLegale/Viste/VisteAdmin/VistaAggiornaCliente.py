from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from datetime import datetime
from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
from GestoreStudioLegale.Servizi.Cliente import Cliente
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
        tool = Tools()
        cliente = Cliente()

        nome = self.layout.itemAtPosition(1, 1).widget().text()
        cognome = self.layout.itemAtPosition(2, 1).widget().text()
        appuntamenti = self.cliente.appuntamentoCliente
        parcelle = self.cliente.parcelle
        corsiAgg = self.cliente.corsoAggiornamento

        if str(self.cliente.getDatiCliente()["Nome"]) == nome:
            self.error("Hai inseirto lo stesso Nome")
            return
        if str(self.cliente.getDatiCliente()["Cognome"]) == cognome:
            self.error("Hai inseirto lo stesso Cognome")
            return

        if nome !="" or cognome != "":
            if self.cliente.ricercaUtilizzatoreNomeCognome(nome,cognome):
                self.error("Esiste già un cliente con questo nome e cognome")
                return
            else:
                if nome !="":
                    self.string += f"nome, "
                if cognome !="":
                    self.string += f"cognome, "

        cd = self.layout.itemAtPosition(3, 1).widget().text()

        if str(self.cliente.getDatiCliente()["Codice fiscale"]) == cd:
            self.error("Hai inseirto lo stesso Codice fiscale")
            return
        elif str(self.cliente.getDatiCliente()["Codice fiscale"]) != cd and cd != "":
            if cliente.ricercaUtilizzatoreCC(cd) is None:
                self.string += f"codice fiscale, "
            else:
                self.error("Hai inserito l'id di un cliente già esistente")
                return

        item = self.layout.itemAtPosition(4, 1).widget()
        date = None

        if self.cliente.getDatiCliente()["Data nascita"] == item.text():
            self.error(f"Hai inseirto la stessa data di nascita")
            return
        elif str(self.cliente.getDatiCliente()["Data nascita"])!= item.text() and item.text() != "":
            data = str(item.text())
            z = data.split("/")
            y1 = z[0].isdigit() and z[1].isdigit() and z[2].isdigit()
            if(len(data)>6):
                y = data[2] != "/" and data[5] != '/'
                if y:
                    self.error("Erore formato data di nascita, il formato è DD/MM/YYYY")
                    return
                elif y1:
                    try:
                        date = datetime.strptime(data, "%d/%m/%Y")
                        if date > datetime.now():
                            self.error("Data non valida inserita, la data che hai inserito è futura")
                            return
                        self.string += f"data di nascita, "
                    except ValueError:
                        self.error("Data non valida inserita")
                        return

                else:
                    self.error("Erore formato data di nascita devi inserire dei numeri e non delle lettere")
                    return
            else:
                self.error("Erore formato data di nascita, il formato è DD/MM/YYYY")
                return

        email = self.layout.itemAtPosition(5, 1).widget().text()

        if str(self.cliente.getDatiCliente()["Email"]) == email:
            self.error("Hai inserito la stessa email")
            return
        elif str(self.cliente.getDatiCliente()["Email"]) != email and email != "":
            if tool.check(email):
                self.string += f"email, "
            else:
                self.error(
                    "Erore formato email, questa non può contenere caratteri speciali e deve  concludere con \"@gmail.com\"")
                return


        item = self.layout.itemAtPosition(6, 1).widget()
        id = str(item.text())

        if str(self.cliente.getDatiCliente()["Id"]) == item.text():
            self.error("Hai inserito lo stesso Id")
            return
        elif str(self.cliente.getDatiCliente()["Id"]) != item.text() and item.text() != "":
            if cliente.ricercaUtilizzatoreId(item.text()) is None:
                self.string += f"id, "
            else:
                self.error("Hai inserito l'id di un cliente già esistente")
                return

        item = self.layout.itemAtPosition(7, 1).widget()
        number = str(item.text())
        if str(self.cliente.getDatiCliente()["Numero telefono"]) == item.text():
            self.error("Hai inserito lo stesso numero di telefono")
            return
        elif str(self.cliente.getDatiCliente()["Numero telefono"])!= item.text() and item.text() != "":
            if len(str(item.text())) == 10 and str(item.text()).isdigit() :
                self.string += f"numero di telefono, "
            else:
                self.error("Hai sbagliato il formato del numero di telefono, devi inserire 10 numeri")
                return


        password = self.breve('password',self.cliente.getDatiCliente()["Password"],8,'a')


        complete = password

        if complete is not False:

            if nome != "":
                self.cliente.nome = nome

            if cognome != "":
                self.cliente.cognome = cognome

            if cd != "":
                self.cliente.codiceFiscale = cd

            if email != "":
                self.cliente.email = email

            self.cliente.password = password

            if date is not None:
                self.cliente.dataNascita = date.strftime("%d/%m/%Y")
            if id != "":
                self.cliente.id = id
            if number != "":
                self.cliente.numeroTelefono = number
        else:
            return

        self.string = self.string[:-2]

        i=0
        vString = self.string.rsplit(",")
        if len(vString)>1:
            self.string = ""
            while i < len(vString):
                if i!=(len(vString)-1):
                    self.string += f"{vString[i]},"
                if i==(len(vString)-1):
                    self.string = self.string[:-1]
                    self.string += f" e{vString[i]}"
                i+=1

        self.cliente.aggiornaCliente()

        item = self.layout.itemAtPosition(1, 1).widget()

        cliente.creaCliente(self.cliente.getDatiCliente()["Codice fiscale"],self.cliente.getDatiCliente()["Cognome"],corsiAgg,
                            self.cliente.getDatiCliente()["Data nascita"],self.cliente.getDatiCliente()["Email"],
                            self.cliente.getDatiCliente()["Id"],self.cliente.getDatiCliente()["Numero telefono"],
                            self.cliente.getDatiCliente()["Password"],appuntamenti,parcelle,
                            self.cliente.getDatiCliente()["Nome"])

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