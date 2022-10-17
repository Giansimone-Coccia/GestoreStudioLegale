from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QMessageBox

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaEliminaCorsoAgg(QWidget):

    id = ''
    tool = Tools()
    avvocatiList = tool.loadAvvocati()

    def __init__(self, parent = None):
        super(VistaEliminaCorsoAgg, self).__init__(parent)

        tool = Tools()
        gLayout = QGridLayout()
        gLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        textLabel = QLabel()
        textLabel.setText("Sei sicuro?")
        textLabel.setGeometry(QRect(100, 120, 350, 40))
        textLabel.setFont(QFont('Arial', 12))
        gLayout.addWidget(textLabel, 1,1,1,2)
        button1 = tool.createButton("No", self.rewind)
        button1.setMaximumSize(500,200)
        gLayout.addWidget(button1, 2, 1)
        gLayout.addWidget(tool.createButton("Sì",lambda checked: self.eliminaCorso(self.id)), 2, 0)
        self.setLayout(gLayout)
        self.resize(300, 100)
        self.setWindowTitle("Eliminazione corso aggiornamento")

    def eliminaCorso(self, id):
        from GestoreStudioLegale.Sistema.CorsoAggiornamento import CorsoAggiornamento
        corso1 = CorsoAggiornamento()
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeCorsoAgg import VistaHomeCorsoAgg
        corso1.rimuoviCorso(id)
        for avvocato in self.avvocatiList:
            if avvocato.corsoAggiornamento.ID == id:
                avvocato.corsoAggiornamento = None
                avvocato.aggiornaAvvocato()
        self.vistaHomeCo = VistaHomeCorsoAgg()
        msg = QMessageBox()
        msg.setWindowTitle('Corso eliminato')
        msg.setText('Corso eliminato con successo')
        msg.exec()
        self.vistaHomeCo.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeCorsoAgg import VistaHomeCorsoAgg
        self.vistaHome2 = VistaHomeCorsoAgg()
        self.vistaHome2.show()
        self.close()

    def setData(self,id):
        self.id = id