from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox
from datetime import datetime, timedelta, time
from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
from GestoreStudioLegale.Servizi.Parcella import Parcella
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaAggiornaParcella(QWidget):

    parcella = Parcella()

    def __init__(self,parent = None):
        super(VistaAggiornaParcella, self).__init__(parent)

        tool = Tools()
        self.gestore = GestoreSistema()
        self.setWindowTitle('Modifica parcella')
        self.resize(500, 120)
        self.layout = QGridLayout()
        self.layout.addWidget(tool.rewindButton(self.rewind), 0, 0)

        self.createLine('intestatario',1,'o')
        self.createLine('importo', 2, 'o')

        self.buttonLogin = QPushButton('conferma')
        self.layout.addWidget(self.buttonLogin, 3, 0, 1, 2)
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

        intestatario = self.breve('intestatario', self.parcella.getDatiParcellaCliente()['intestatario'], 1, 'o')
        importo = self.breve('importo', self.parcella.getDatiParcellaCliente()["importo"], 2, 'o')
        print("yolo")

        complete = intestatario and importo

        if complete is not False:
            Parcella.rimuoviParcella(self.parcella.getDatiParcellaCliente()["ID"])
            self.parcella.intestatario = intestatario
            self.parcella.importo = importo
        else:
            return

        print(self.parcella)


        item = self.layout.itemAtPosition(1, 1).widget()
        print(item.text())
        parcella = Parcella()

        '''parcella.creaParcella(self.avvocato.getDatiAvvocato()["Codice fiscale"],self.avvocato.getDatiAvvocato()["Cognome"],
                              self.avvocato.getDatiAvvocato()["Nome"],corsiAgg,
                            self.avvocato.getDatiAvvocato()["Data nascita"],self.avvocato.getDatiAvvocato()["Email"],
                            self.avvocato.getDatiAvvocato()["Id"],self.avvocato.getDatiAvvocato()["Numero telefono"],
                            self.avvocato.getDatiAvvocato()["Password"],udienza,clienti,licenza,appuntamenti)'''

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