from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QMessageBox

from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaEliminaAppuntamentoA(QWidget):

    id = ''
    tool = Tools()

    def __init__(self,parent = None):
        super(VistaEliminaAppuntamentoA, self).__init__(parent)

        gLayout = QGridLayout()
        gLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        textLabel = QLabel()
        textLabel.setText("Sei sicuro?")
        textLabel.setGeometry(QRect(100, 120, 350, 40))
        textLabel.setFont(QFont('Arial', 12))
        gLayout.addWidget(textLabel, 1,1,1,2)
        button1 = self.tool.createButton("No", self.rewind)
        button1.setMaximumSize(500,200)
        gLayout.addWidget(button1, 2, 1)
        gLayout.addWidget(self.tool.createButton("Sì",lambda checked: self.eliminaAppuntamento(self.id)), 2, 0)
        self.setLayout(gLayout)
        self.resize(300, 100)
        self.setWindowTitle("Gestore Studio Legale")

    def eliminaAppuntamento(self,id):
        from GestoreStudioLegale.Viste.VisteAvvocato.VisteAvvocatoAppuntamento.VistaHomeAppuntamentiA import VistaHomeAppuntamentiA
        app = Appuntamento()
        app.rimuoviAppuntamento(id)
        tool = Tools()
        self.avocatiList = tool.loadAvvocati()
        for avvocato in self.avocatiList:
            if avvocato.codiceFiscale == tool.leggi().rsplit()[0]:
                for app in avvocato.appuntamentiAvvocato:
                    if app.ID == id:
                        avvocato.appuntamentiAvvocato.remove(app)
                avvocato.aggiornaAvvocato()
        self.vistaVisualizzaAppuntamento = VistaHomeAppuntamentiA()
        msg = QMessageBox()
        msg.setWindowTitle('Appuntamento eliminato')
        msg.setText('Appuntamento eliminato con successo')
        msg.exec()
        self.vistaVisualizzaAppuntamento.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VisteAvvocatoAppuntamento.VistaHomeAppuntamentiA import VistaHomeAppuntamentiA
        self.vistaHome = VistaHomeAppuntamentiA()
        self.vistaHome.show()
        self.close()

    def setData(self,id):
        self.id = id