from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox
from PyQt5 import QtCore as qtc

from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaEliminaCliente(QWidget):

    id = ''
    cliente = Cliente()

    def __init__(self,parent = None):
        super(VistaEliminaCliente, self).__init__(parent)

        tool = Tools()
        gLayout = QGridLayout()
        gLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        textLabel = QLabel()
        textLabel.setText(f"Sei sicuro di voler eliminare:{self.cliente.getDatiCliente()['Nome']}?")
        textLabel.setGeometry(QRect(100, 120, 350, 40))
        textLabel.setFont(QFont('Arial', 12))
        gLayout.addWidget(textLabel, 1,1,1,2)
        button1 = tool.createButton("No", self.rewind)
        button1.setMaximumSize(500,200)
        gLayout.addWidget(button1, 2, 1)
        gLayout.addWidget(tool.createButton("Sì",lambda: self.eliminaCliente(self.id)), 2, 0)
        self.setLayout(gLayout)
        self.resize(500, 300)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()

    def eliminaCliente(self,id):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaClienti import VistaVisualizzaClienti
        Cliente.rimuoviCliente(id)
        self.vistaVisualizzaCliente = VistaVisualizzaClienti()
        msg = QMessageBox()
        msg.setWindowTitle('Cliente eliminato')
        msg.setText('Il cliente è stato eliminato con successo')
        msg.exec()
        self.vistaVisualizzaCliente.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaClienti import VistaVisualizzaClienti
        self.vistaHome = VistaVisualizzaClienti()
        self.vistaHome.show()
        self.close()

    def setData(self,id,cliente):
        self.id = id
        self.cliente = cliente