from PyQt5.QtWidgets import (QDialog,
                             QDialogButtonBox, QFormLayout, QGroupBox,
                             QLineEdit,
                             QVBoxLayout, QMessageBox)

from GestoreStudioLegale.Servizi.Cliente import Cliente

from GestoreStudioLegale.Utilities.Utilities import Tools


class RicercaUdienze(QDialog):
    NumButtons = 4
    NumGridRows = 3

    def __init__(self):
        super(RicercaUdienze, self).__init__()

        self.tool = Tools()
        self.udienzeList = self.tool.loadUdienze()


        self.textIn = QLineEdit()

        self.layout = QFormLayout()

        self.createFormGroupBox()


        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.indexScelta)
        buttonBox.rejected.connect(self.rewind)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)

        self.setLayout(mainLayout)

        self.setWindowTitle("Ricerca")
        self.resize(400, 120)

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Cerca un udienza")

        self.layout.insertRow(1, "Codice fiscale (cliente):", self.textIn)

        self.formGroupBox.setLayout(self.layout)

        self.formGroupBox.setLayout(self.layout)

    def indexScelta(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.UdienzaRicercata import UdienzaRicercata

        self.code = self.textIn.text()

        cliente = Cliente()

        self.risultatoRicerca = cliente.ricercaUtilizzatoreCC(self.code)

        if self.risultatoRicerca is None:
            msg = QMessageBox()
            msg.setWindowTitle('Cliente non trovato')
            msg.setText('Non esiste alcun cliente con questo codice fiscale. Riprova')
            msg.exec()
            return

        udienze = []

        for udienza in self.udienzeList:
            if udienza.Cliente.codiceFiscale == self.risultatoRicerca.codiceFiscale:
                udienze.append(udienza)

        self.subWindow = UdienzaRicercata(udienze)
        self.subWindow.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeUdienze import VistaHomeUdienze
        self.vistaHome = VistaHomeUdienze()
        self.vistaHome.show()
        self.close()