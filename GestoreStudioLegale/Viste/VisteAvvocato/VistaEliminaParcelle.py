from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QMessageBox

from GestoreStudioLegale.Servizi.Parcella import Parcella
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaEliminaParcelle(QWidget):

    id = ''

    def __init__(self, parent = None):
        super(VistaEliminaParcelle, self).__init__(parent)

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
        gLayout.addWidget(tool.createButton("Sì",lambda checked: self.eliminaParcella(self.id)), 2, 0)
        self.setLayout(gLayout)
        self.resize(300, 100)
        self.setWindowTitle("Eliminazione parcella")

    def eliminaParcella(self, id):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeParcelle import VistaHomeParcelle
        Parcella.rimuoviParcella(id)
        self.vistaHomeParcelle = VistaHomeParcelle()
        msg = QMessageBox()
        msg.setWindowTitle('Appuntamento eliminato')
        msg.setText('Appuntamento eliminato con successo')
        msg.exec()
        self.vistaHomeParcelle.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeParcelle import VistaHomeParcelle
        self.vistaHome = VistaHomeParcelle()
        self.vistaHome.show()
        self.close()

    def setData(self,id):
        self.id = id