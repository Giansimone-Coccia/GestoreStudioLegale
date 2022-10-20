from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout


from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaAvvocati import VistaVisualizzaAvvocati


class VistaAvvocatoRicercato(QWidget):

    avvocato = Avvocato()
    tool = Tools()

    def __init__(self, parent=None):
        super(VistaAvvocatoRicercato, self).__init__(parent)

        self.vistaVis = VistaVisualizzaAvvocati()

        self.setWindowTitle('Ricerca avvocato')
        self.resize(500, 120)
        self.grifLayout = QGridLayout()
        self.grifLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 1)


    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaRicercaAvvocato import VistaRicercaAvvocato
        self.vistaHome = VistaRicercaAvvocato()
        self.vistaHome.show()
        self.close()

    def setData(self,avvocato):
        self.avvocato = avvocato
        textLabel = QLabel()
        textLabel.setText(
            'Avvocato: ' + '\n' + 'NOME: ' + f"{self.avvocato.getDatiAvvocato()['Nome']}" + '\n' + 'COGNOME: ' + f"{self.avvocato.getDatiAvvocato()['Cognome']}" + '\n' + 'DATA DI NASCITA: ' + f"{self.avvocato.getDatiAvvocato()['Data nascita']}" + '\n' + 'ID: ' + f"{self.avvocato.getDatiAvvocato()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{self.avvocato.getDatiAvvocato()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{self.avvocato.getDatiAvvocato()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{self.avvocato.getDatiAvvocato()['Numero telefono']}" + '\n' + 'PASSWORD: ' + f"{self.avvocato.getDatiAvvocato()['Password']}")
        textLabel.setGeometry(QRect(0, 0, 350, 20))
        textLabel.setFont(QFont('Arial', 10))
        textLabel.setStyleSheet("border: 1px solid black;")
        self.grifLayout.addWidget(textLabel, 1, 1, 1, 2)
        self.grifLayout.addWidget(
            self.tool.createButton("Aggiorna", lambda checked, a=self.avvocato: self.vistaVis.aggiornaAvvocato(a),method2=self.close), 2, 1)
        self.grifLayout.addWidget(
            self.tool.createButton("Elimina",
                              lambda checked, b=self.avvocato.getDatiAvvocato()['Id']: self.vistaVis.eliminaAvvocato(b),method2=self.close),
            2, 2)
        self.setLayout(self.grifLayout)