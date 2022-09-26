from unittest import TestCase

from GestoreStudioLegale.Servizi.Cliente import Cliente

class TestCliente(TestCase):
    def setUp(self):
        self.clienteVuoto = Cliente()
        self.clienteVuoto.creaCliente('', '', [], '', '', '', 0, '', [], [], '', [])
        self.clienteOk = Cliente()
        self.clienteOk.creaCliente('CF', 'Alberto', ['Economia politica','Rischi e pericoli'], '', '', '', 0, '', [], [], '', [])

    def testOggettoVuoto(self):
        self.assertEqual(self.clienteVuoto.getDatiCliente()['Nome'], '')
        self.assertEqual(len(self.clienteVuoto.getDatiCliente()['Corso aggiornamento']), 0)
        self.assertEqual(len(self.clienteOk.getDatiCliente()['Corso aggiornamento']), 2)