from unittest import TestCase

from GestoreStudioLegale.Servizi.Avvocato import Avvocato

class TestAvvocato(TestCase):
    def setUp(self):
        self.avvocatoVuoto = Avvocato()
        self.avvocatoVuoto.creaAvvocato('', '', '', [], '', '', '', 0, '', [], [])
        self.avvocatoOk = Avvocato()
        self.avvocatoOk.creaAvvocato('CF', 'Verdi', 'Angelo', ['Economia politica','Rischi e pericoli'], '', 'av@gmail.com', '', 0, '', [], [])

    def testOggettoVuoto(self):
        self.assertIsNotNone(self.avvocatoOk)
        self.assertIsNotNone(self.avvocatoVuoto)
        self.assertEqual(self.avvocatoVuoto.getDatiAvvocato()['Nome'], '')
        self.assertEqual(self.avvocatoVuoto.getDatiAvvocato()['Codice fiscale'], '')
        self.assertEqual(len(self.avvocatoVuoto.getDatiAvvocato()['Corso aggiornamento']), 0)
        self.assertEqual(len(self.avvocatoOk.getDatiAvvocato()['Corso aggiornamento']), 2)
        self.assertEqual(self.avvocatoOk.getDatiAvvocato()['Cognome'], 'Verdi')