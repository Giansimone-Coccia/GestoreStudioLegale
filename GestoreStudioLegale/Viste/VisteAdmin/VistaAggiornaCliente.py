from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox
from datetime import datetime, timedelta, time
from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaAggiornaCliente(QWidget):

    cliente = Cliente()

    def _init_(self,parent = None):
        super(VistaAggiornaCliente, self)._init_(parent)

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
        print(self.cliente.getDatiCliente()["Data nascita"])
        cliente = Cliente()

        appuntamenti = self.cliente.appuntamentoCliente
        parcelle = self.cliente.parcelle
        udienze =self.cliente.udienza
        corsiAgg = self.cliente.corsoAggiornamento

        nome = self.breve('nome',self.cliente.getDatiCliente()["Nome"],1,'o')

        cognome = self.breve('cognome',self.cliente.getDatiCliente()["Cognome"],2,'o')

        cd = self.breve('codice fiscale',self.cliente.getDatiCliente()["Codice fiscale"],3,'o')

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



        email = self.breve('email',self.cliente.getDatiCliente()["Email"],5,'a')

        item = self.layout.itemAtPosition(6, 1).widget()
        id = str(item.text())
        if str(self.cliente.getDatiCliente()["Id"]) == item.text():
            self.error("Hai inseirto lo stesso Id")
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
            self.error("Hai inseirto lo stesso numero di telefono")
            return
        elif str(self.cliente.getDatiCliente()["Numero telefono"])!= item.text() and item.text() != "":
            if len(str(item.text())) == 10 and str(item.text()).isdigit() :
                self.string += f"numero di telefono, "
            else:
                self.error("Hai sbagliato il formato del numero di telefono, devi inserire 10 numeri")
                return


        password = self.breve('password',self.cliente.getDatiCliente()["Password"],8,'a')

        print("yolo")

        #Cliente.rimuoviCliente(self.cliente.getDatiCliente()["Id"])

        '''if nome is not False: self.cliente.nome = nome
        else: return
        if cognome is not False:self.cliente.cognome = cognome
        else: return
        if cd is not False:self.cliente.codiceFiscale = cd
        else: return
        if date is not None: self.cliente.dataNascita = date

        if email is not False:self.cliente.email = email
        else: return
        if id != "":self.cliente.id = id

        if number != "": self.cliente.numeroTelefono=number

        if password is not False:self.cliente.password = password
        else:return'''

        complete = nome and cognome and cd and email and password

        if complete is not False:
            Cliente.rimuoviCliente(self.cliente.getDatiCliente()["Id"])
            self.cliente.nome = nome
            self.cliente.cognome = cognome
            self.cliente.codiceFiscale = cd
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

        print(self.cliente)


        self.string = self.string[:-2]
        print(self.cliente.nome)
        print(self.string)
        print(self.cliente.getDatiCliente())

        item = self.layout.itemAtPosition(1, 1).widget()
        print(item.text())

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