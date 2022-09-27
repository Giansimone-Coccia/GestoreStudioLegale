from unittest import TestCase

from GestoreStudioLegale.Servizi.Cliente import Cliente

class TestCliente(TestCase):
    def setUp(self):
        self.clienteVuoto = Cliente()
        self.clienteVuoto.creaCliente('', '', [], '', '', '', 0, '', [], [], '', [])
        self.clienteOk = Cliente()
        self.clienteOk.creaCliente('CF', 'Alberto', [], '', '', '', 0, '', [], [], '', ['udienza1', 'udienza2'])

    def testOggettoVuoto(self):
        self.assertEqual(self.clienteVuoto.getDatiCliente()['Nome'], '')
        self.assertEqual(len(self.clienteVuoto.getDatiCliente()['Udienza']), 0)
        self.assertEqual(len(self.clienteOk.getDatiCliente()['Udienza']), 2)