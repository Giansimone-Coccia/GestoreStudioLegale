from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox

from GestoreStudioLegale.Servizi.Avvocato import Avvocato

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaEliminaAvvocato(QWidget):

    id = ''

    def __init__(self,parent = None):
        super(VistaEliminaAvvocato, self).__init__(parent)

        tool = Tools()
        gLayout = QGridLayout()
        gLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        textLabel = QLabel()
        textLabel.setText(f"Sei sicuro?")
        textLabel.setGeometry(QRect(100, 120, 350, 40))
        textLabel.setFont(QFont('Arial', 12))
        gLayout.addWidget(textLabel, 1,0)
        button1 = tool.createButton("No", self.rewind)
        button2 = tool.createButton("Sì",lambda: self.eliminaAvvocato(self.id))
        button1.setFont(QFont('Arial', 24))
        button2.setFont(QFont('Arial', 24))
        button1.setBaseSize(int(160), int(90))
        button2.setBaseSize(int(160), int(90))
        button1.setMaximumSize(160 * 2, 90 * 2)
        button2.setMaximumSize(160 * 2, 90 * 2)
        gLayout.addWidget(button1, 2, 1)
        gLayout.addWidget(button2, 2, 0)
        self.setLayout(gLayout)
        self.resize(160*4, 300)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()

    def eliminaAvvocato(self,id):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaAvvocati import VistaVisualizzaAvvocati
        Avvocato.rimuoviAvvocato(id)
        self.vistaVisualizzaAvvocato = VistaVisualizzaAvvocati()
        msg = QMessageBox()
        msg.setWindowTitle('Avvocato eliminato')
        msg.setText('Avvocato eliminato con successo')
        msg.exec()
        self.vistaVisualizzaAvvocato.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaAvvocati import VistaVisualizzaAvvocati
        self.vistaHome = VistaVisualizzaAvvocati()
        self.vistaHome.show()
        self.close()

    def setData(self,id):
        self.id = id