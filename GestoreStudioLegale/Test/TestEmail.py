from unittest import TestCase

from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento
from GestoreStudioLegale.Sistema.GestoreEmail import GestoreEmail

class TestStatistiche(TestCase):
    def setUp(self):
        self.gestoreE = GestoreEmail()
        self.appuntamento = Appuntamento()

    def testException(self):
        self.gestoreE.invioEmail()
        if self.appuntamento == None:
            self.assertRaises(Exception, self.gestoreE.invioEmail())