from PyQt5.QtWidgets import (QDialog,
                             QDialogButtonBox, QFormLayout, QGroupBox,
                             QLabel, QLineEdit,
                             QVBoxLayout, QMessageBox)

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Sistema.CorsoAggiornamento import CorsoAggiornamento


class VistaRicercaCorsoAgg(QDialog):
    NumGridRows = 3
    NumButtons = 4


    def __init__(self):
        super(VistaRicercaCorsoAgg, self).__init__()

        self.tool = Tools()
        self.corsiList = self.tool.loadCorsiAggiornamento()


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
        self.formGroupBox = QGroupBox("Cerca un corso d'aggiornamento")

        self.layout.insertRow(1, "ID", self.textIn)

        self.formGroupBox.setLayout(self.layout)

        self.formGroupBox.setLayout(self.layout)

    def indexScelta(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaCorsoAggRicercato import VistaCorsoAggRicercato

        self.code = self.textIn.text()

        corsoAgg = CorsoAggiornamento()

        risultatoRicerca = corsoAgg.ricercaCorsoCodice(self.code)
        #print(risultatoRicerca.nome)

        if risultatoRicerca is None:
            msg = QMessageBox()
            msg.setWindowTitle('Corso non trovato')
            msg.setText('Non esiste alcun corso di aggiornamento con questo ID. Riprova')
            msg.exec()
            return

        corsiAgg = []

        for corso in self.corsiList:
            if corso.ID == risultatoRicerca.ID:
                corsiAgg.append(corso)


        self.subWindow = VistaCorsoAggRicercato(corsiAgg)
        self.subWindow.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeCorsoAgg import VistaHomeCorsoAgg
        self.vistaHome = VistaHomeCorsoAgg()
        self.vistaHome.show()
        self.close()