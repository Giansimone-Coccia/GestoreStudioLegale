from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QMessageBox

from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaEliminaCliente(QWidget):

    id = ''
    tool = Tools()

    def __init__(self,parent = None):
        super(VistaEliminaCliente, self).__init__(parent)


        gLayout = QGridLayout()
        gLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        textLabel = QLabel()
        textLabel.setText(f"Sei sicuro?")
        textLabel.setGeometry(QRect(100, 120, 350, 40))
        textLabel.setFont(QFont('Arial', 12))
        gLayout.addWidget(textLabel, 1,0)
        button1 = self.tool.createButton("No", self.rewind)
        button2 = self.tool.createButton("Sì",lambda: self.eliminaCliente(self.id))
        button1.setFont(QFont('Arial', 24))
        button2.setFont(QFont('Arial', 24))
        button1.setMaximumSize(160 * 2, 90 * 2)
        button2.setMaximumSize(160 * 2, 90 * 2)
        gLayout.addWidget(button1, 2, 1)
        gLayout.addWidget(button2, 2, 0)
        self.setLayout(gLayout)
        self.resize(300, 100)
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

    def setData(self,id):
        self.id = id