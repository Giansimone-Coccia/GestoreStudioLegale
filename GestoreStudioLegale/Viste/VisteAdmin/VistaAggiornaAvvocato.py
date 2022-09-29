from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox
from datetime import datetime, timedelta, time
from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaAggiornaAvvocato(QWidget):

    avvocato = Avvocato()

    def _init_(self,parent = None):
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
        print(self.avvocato.getDatiAvvocato()["Data nascita"])

        appuntamenti = self.avvocato.appuntamentiAvvocato
        clienti = self.avvocato.clienti
        licenza =self.avvocato.licenza
        corsiAgg = self.avvocato.corsoAggiornamento
        udienza= self.avvocato.udienza

        nome = self.breve('nome', self.avvocato.getDatiAvvocato()["Nome"], 1, 'o')

        cognome = self.breve('cognome', self.avvocato.getDatiAvvocato()["Cognome"], 2, 'o')

        cd = self.breve('codice fiscale', self.avvocato.getDatiAvvocato()["Codice fiscale"], 3, 'o')

        item = self.layout.itemAtPosition(4, 1).widget()
        date = None
        if self.avvocato.getDatiAvvocato()["Data nascita"] == item.text():
            self.error(f"Hai inseirto la stessa data di nascita")
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

        email = self.breve('email', self.avvocato.getDatiAvvocato()["Email"], 5, 'a')

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

        print("yolo")



        '''if nome is not False:self.avvocato.nome = nome
        else:return
        if cognome is not False:self.avvocato.cognome = cognome
        else:return
        if cd is not False:self.avvocato.codiceFiscale = cd
        else:return
        if date is not None: self.avvocato.dataNascita = date

        if email is not False:self.avvocato.email = email
        else:return
        if id != "": self.avvocato.id = id

        if number != "": self.avvocato.numeroTelefono = number

        if password is not False:self.avvocato.password = password
        else:return'''

        complete = nome and cognome and cd and email and password

        if complete is not False:
            Avvocato.rimuoviAvvocato(self.avvocato.getDatiAvvocato()["Id"])
            self.avvocato.nome = nome
            self.avvocato.cognome = cognome
            self.avvocato.codiceFiscale = cd
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

        print(self.avvocato)

        self.string = self.string[:-2]
        print(self.avvocato.nome)
        print(self.string)
        print(self.avvocato.getDatiAvvocato())

        item = self.layout.itemAtPosition(1, 1).widget()
        print(item.text())
        avvocato = Avvocato()

        avvocato.creaAvvocato(self.avvocato.getDatiAvvocato()["Codice fiscale"],self.avvocato.getDatiAvvocato()["Cognome"],
                              self.avvocato.getDatiAvvocato()["Nome"],corsiAgg,
                            self.avvocato.getDatiAvvocato()["Data nascita"],self.avvocato.getDatiAvvocato()["Email"],
                            self.avvocato.getDatiAvvocato()["Id"],self.avvocato.getDatiAvvocato()["Numero telefono"],
                            self.avvocato.getDatiAvvocato()["Password"],udienza,clienti,licenza,appuntamenti)

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