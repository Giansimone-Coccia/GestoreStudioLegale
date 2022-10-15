from unittest import TestCase

from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Sistema.CorsoAggiornamento import CorsoAggiornamento


class TestCliente(TestCase):
    def setUp(self):
        corso1 = CorsoAggiornamento()
        corso2 = CorsoAggiornamento()
        self.clienteVuoto = Cliente()
        self.clienteVuoto.creaCliente('', '', [], '', '', '', 0, '', [], [], '')
        self.clienteOk = Cliente()
        self.clienteOk.creaCliente('CF', 'Rossi', [corso1, corso2], '', 'mr@gmail.com', '', 3334445556, '', [], [], 'Mario')

    def testOggettoVuoto(self):
        self.assertEqual(self.clienteVuoto.getDatiCliente()['Nome'], '')
        self.assertEqual(len(self.clienteVuoto.getDatiCliente()['Corso aggiornamento']), 0)
        self.assertEqual(len(self.clienteOk.getDatiCliente()['Corso aggiornamento']), 2)
        self.assertEqual(self.clienteOk.getDatiCliente()['Codice fiscale'], 'CF')
        self.assertEqual(self.clienteOk.getDatiCliente()['Email'], 'mr@gmail.com')