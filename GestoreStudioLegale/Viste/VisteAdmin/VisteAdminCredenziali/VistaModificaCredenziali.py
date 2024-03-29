from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel


from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAdmin.VisteAdminCredenziali.VistaModificaPassword import VistaModificaPassword
from GestoreStudioLegale.Viste.VisteAdmin.VisteAdminCredenziali.VistaModificaUsername import VistaModificaUsername


class VistaModificaCredenziali(QWidget):

    tool = Tools()

    def __init__(self,parent = None):
        super(VistaModificaCredenziali, self).__init__(parent)

        gLayout = QGridLayout()
        gLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        textLabel = QLabel()
        textLabel.setText(f"Scegli quale credenziale modificare:")
        textLabel.setGeometry(QRect(100, 120, 350, 40))
        textLabel.setFont(QFont('Arial', 12))
        gLayout.addWidget(textLabel, 1,0)
        button1 = self.tool.createButton("Modifica Password", self.reachModificaPassword)
        button2 = self.tool.createButton("Modifica Username", self.reachModificaUsername)
        button1.setFont(QFont('Arial', 15))
        button2.setFont(QFont('Arial', 15))
        button1.setBaseSize(int(160),int(90))
        button2.setBaseSize(int(160),int(90))
        button1.setMaximumSize(160*2, 90*2)
        button2.setMaximumSize(160*2, 90*2)
        gLayout.addWidget(button1, 2, 1)
        gLayout.addWidget(button2, 2, 0)
        self.setLayout(gLayout)
        self.resize(160*4, 300)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()

    def reachModificaPassword(self):
        self.vistaModPassword = VistaModificaPassword()
        self.vistaModPassword.show()
        self.close()

    def reachModificaUsername(self):
        self.vistaModUsername = VistaModificaUsername()
        self.vistaModUsername.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeAdmin import VistaHomeAdmin
        self.vistaHome = VistaHomeAdmin()
        self.vistaHome.show()
        self.close()