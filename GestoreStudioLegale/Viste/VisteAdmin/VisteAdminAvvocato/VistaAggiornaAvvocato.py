from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from datetime import datetime
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
        #print(self.avvocato.getDatiAvvocato()["Data nascita"])
        tool = Tools()

        nome = self.layout.itemAtPosition(1, 1).widget().text()
        cognome = self.layout.itemAtPosition(2, 1).widget().text()
        appuntamenti = self.avvocato.appuntamentiAvvocato
        clienti = self.avvocato.clienti
        #licenza =self.avvocato.licenza
        corsiAgg = self.avvocato.corsoAggiornamento
        #udienza= self.avvocato.udienza

        if str(self.avvocato.getDatiAvvocato()["Nome"]) == nome:
            self.error("Hai inserito lo stesso Nome")
            return
        if str(self.avvocato.getDatiAvvocato()["Cognome"]) == cognome:
            self.error("Hai inserito lo stesso Cognome")
            return

        if nome != "" or cognome != "":
            if self.avvocato.ricercaUtilizzatoreNomeCognome(nome, cognome):
                self.error("Esiste già un cliente con questo nome e cognome")
                return
            else:
                if nome != "":
                    self.string += f"nome, "
                if cognome != "":
                    self.string += f"cognome, "

        cd = self.layout.itemAtPosition(3, 1).widget().text()

        if str(self.avvocato.getDatiAvvocato()["Codice fiscale"]) == cd:
            self.error("Hai inseirto lo stesso Codice fiscale")
            return
        elif str(self.avvocato.getDatiAvvocato()["Codice fiscale"]) != cd and cd != "":
            if self.avvocato.ricercaUtilizzatoreCC(cd) is None:
                self.string += f"codice fiscale, "
            else:
                self.error("Hai inserito l'id di un cliente già esistente")
                return

        item = self.layout.itemAtPosition(4, 1).widget()
        date = None

        if self.avvocato.getDatiAvvocato()["Data nascita"] == item.text():
            self.error(f"Hai inserito la stessa data di nascita")
            return
        elif str(self.avvocato.getDatiAvvocato()["Data nascita"]) != item.text() and item.text() != "":
            data = str(item.text())
            z = data.split("/")
            y1 = z[0].isdigit() and z[1].isdigit() and z[2].isdigit()
            if (len(data) > 6):
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

        if str(self.avvocato.getDatiAvvocato()["Email"]) == email:
            self.error("Hai inseirto la stessa email")
            return
        elif str(self.avvocato.getDatiAvvocato()["Email"]) != email and email != "":
            if tool.check(email):
                self.string += f"email, "
            else:
                self.error(
                    "Erore formato email, questa non può contenere caratteri speciali e deve  concludere con \"@gmail.com\"")
                return

        item = self.layout.itemAtPosition(6, 1).widget()
        id = str(item.text())

        if str(self.avvocato.getDatiAvvocato()["Id"]) == item.text():
            self.error("Hai inseirto lo stesso Id")
            return
        elif str(self.avvocato.getDatiAvvocato()["Id"]) != item.text() and item.text() != "":
            if self.avvocato.ricercaUtilizzatoreId(item.text()) is None:
                self.string += f"id, "
            else:
                self.error("Hai inserito l'id di un cliente già esistente")
                return

        item = self.layout.itemAtPosition(7, 1).widget()
        number = str(item.text())

        if str(self.avvocato.getDatiAvvocato()["Numero telefono"]) == item.text():
            self.error("Hai inseirto lo stesso numero di telefono")
            return
        elif str(self.avvocato.getDatiAvvocato()["Numero telefono"]) != item.text() and item.text() != "":
            if len(str(item.text())) == 10 and str(item.text()).isdigit():
                self.string += f"numero di telefono, "
            else:
                self.error("Hai sbagliato il formato del numero di telefono, devi inserire 10 numeri")
                return

        password = self.breve('password', self.avvocato.getDatiAvvocato()["Password"], 8, 'a')

        complete = password

        if complete is not False:
            if nome != "":
                self.avvocato.nome = nome

            if cognome != "":
                self.avvocato.cognome = cognome

            if cd != "":
                self.avvocato.codiceFiscale = cd

            if email != "":
                self.avvocato.email = email

            self.avvocato.password = password

            if date is not None:
                self.avvocato.dataNascita = date.strftime("%d/%m/%Y")

            if id != "":
                self.avvocato.id = id

            if number != "":
                self.avvocato.numeroTelefono = number
        else:
            return

        self.string = self.string[:-2]

        i=0
        vString = self.string.rsplit(",")
        #print(vString)
        if len(vString)>1:
            self.string = ""
            while i < len(vString):
                if i!=(len(vString)-1):
                    self.string += f"{vString[i]},"
                if i==(len(vString)-1):
                    self.string = self.string[:-1]
                    self.string += f" e{vString[i]}"
                i+=1

        self.avvocato.aggiornaAvvocato()

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
        from GestoreStudioLegale.Viste.VisteAdmin.VisteAdminAvvocato.VistaVisualizzaAvvocati import VistaVisualizzaAvvocati
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