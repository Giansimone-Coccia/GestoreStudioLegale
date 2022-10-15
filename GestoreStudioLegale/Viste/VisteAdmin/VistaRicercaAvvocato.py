from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, \
    QLineEdit, QPushButton, QMessageBox


from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Utilities.Utilities import Tools



class VistaRicercaAvvocato(QWidget):

    def __init__(self, parent=None):
        super(VistaRicercaAvvocato, self).__init__(parent)

        tool = Tools()
        self.setWindowTitle('Ricerca avvocato')
        self.resize(500, 120)
        layout = QGridLayout()
        layout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        textLabel = QLabel()
        textLabel.setText(f"Inserisci l'id dell'avvocato da ricercare:")
        textLabel.setGeometry(QRect(100, 120, 350, 40))
        textLabel.setFont(QFont('Arial', 10))
        layout.addWidget(textLabel, 1, 0,1,3)
        self.labelIdAvv = QLabel('<font size="4"> Id avvocato </font>')
        self.lineEditIdAvv = QLineEdit()
        self.lineEditIdAvv.setPlaceholderText("Inserisci l'id dell'avvoacto")
        layout.addWidget(self.labelIdAvv, 2, 0)
        layout.addWidget(self.lineEditIdAvv, 2, 1)
        self.buttonLogin = QPushButton('Conferma')
        layout.addWidget(self.buttonLogin, 3, 0, 1, 3)
        layout.setRowMinimumHeight(2, 75)
        self.buttonLogin.clicked.connect(self.ricercaAvvocato)
        self.setLayout(layout)

    def ricercaAvvocato(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaAvvocatoRicercato import VistaAvvocatoRicercato
        avvocato = Avvocato()

        #print(self.lineEditIdAvv)

        #print(avvocato.ricercaUtilizzatoreId(self.lineEditIdAvv.text()))

        if avvocato.ricercaUtilizzatoreId(self.lineEditIdAvv.text()) is None:
            msg = QMessageBox()
            msg.setWindowTitle('Avvocato non trovato')
            msg.setText('Non esiste alcun avvocato con questo id')
            msg.exec()
            return
        else:
            self.subWindow = VistaAvvocatoRicercato()
            avv= avvocato.ricercaUtilizzatoreId(self.lineEditIdAvv.text())
            #print(avv.getDatiAvvocato())
            self.subWindow.setData(avv)
            self.subWindow.show()
            self.close()


    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaAvvocati import VistaVisualizzaAvvocati
        self.vistaHome = VistaVisualizzaAvvocati()
        self.vistaHome.show()
        self.close()