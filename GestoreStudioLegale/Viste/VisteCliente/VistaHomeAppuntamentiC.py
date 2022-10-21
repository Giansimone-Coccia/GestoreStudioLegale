from PyQt5.QtWidgets import QWidget, QGridLayout, QMessageBox

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteCliente.VistaPrenotaAppuntamentiC import VistaPrenotaAppuntamentiC
from GestoreStudioLegale.Viste.VisteCliente.VistaVisualizzaAppuntamento import VistaVisualizzaAppuntamento


class VistaHomeAppuntamentiC (QWidget):

    tool = Tools()

    def __init__(self, parent=None):
        super(VistaHomeAppuntamentiC, self).__init__(parent)
        gLayout = QGridLayout()
        gLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        gLayout.addWidget(self.tool.createButton("Prenota Appuntamento", self.reachPrenotaAppuntamento), 1, 0)
        gLayout.addWidget(self.tool.createButton("Visualizza Appuntamento", self.reachVisualizzaAppuntamento), 2, 0)
        self.setLayout(gLayout)
        self.resize(500, 400)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()

    def reachPrenotaAppuntamento(self):
        self.avvocatiList=self.tool.loadAvvocati()
        self.clientiList=self.tool.loadClienti()
        i = 0
        for cliente in self.clientiList:
            if cliente.codiceFiscale == self.tool.leggi().rsplit()[0]:
                for avvocato in self.avvocatiList:
                    self.avvClientiList = avvocato.clienti
                    for avvCliente in self.avvClientiList:
                        if avvCliente.codiceFiscale == cliente.codiceFiscale:
                            i = 1

        if i ==0 :
            msg = QMessageBox()
            msg.setWindowTitle('Nessun avvocato associato')
            msg.setText('Nessun avvocato è stato asscociato a lei')
            msg.exec()
            return

        self.vistaPrenotazione = VistaPrenotaAppuntamentiC()
        self.vistaPrenotazione.show()
        self.close()

    def reachVisualizzaAppuntamento(self):
        self.vistaAppuntamento = VistaVisualizzaAppuntamento()
        self.vistaAppuntamento.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteCliente.VistaHomeCliente import VistaHomeCliente
        self.vistaHome = VistaHomeCliente()
        self.vistaHome.show()
        self.close()


