from PyQt5.QtWidgets import QWidget, QGridLayout
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaAggiungiCliente(QWidget):

    tool = Tools()

    def __init__(self,parent = None):
        super(VistaAggiungiCliente, self).__init__(parent)

        gLayout = QGridLayout()
        gLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        gLayout.addWidget(self.tool.createButton("Aggiungi cliente esistente", self.reachAggiungiClienteEsistente), 1, 0)
        gLayout.addWidget(self.tool.createButton("Crea nuovo cliente", self.reachCreaCliente), 2, 0)
        self.setLayout(gLayout)
        self.resize(500, 400)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()


    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAvvocato import VistaHomeAvvocato
        self.vistaH = VistaHomeAvvocato()
        self.vistaH.show()
        self.close()

    def reachCreaCliente(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VisteAvvocatoCliente.VistaCreaCliente import VistaCreaCliente
        self.vistaH = VistaCreaCliente()
        self.vistaH.show()
        self.close()

    def reachAggiungiClienteEsistente(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VisteAvvocatoCliente.VistaAggiungiClienteEsistente import VistaAggiungiClienteEsistente
        self.vistaH = VistaAggiungiClienteEsistente()
        self.vistaH.show()
        self.close()