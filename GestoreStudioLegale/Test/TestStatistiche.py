from unittest import TestCase

from GestoreStudioLegale.Gestione.Statistiche import Statistiche


class TestStatistiche(TestCase):
    def setUp(self):
        self.stats = Statistiche()
        self.stats.numeroAppuntamenti = 15
        self.stats.mediaUdienzeMensili = 6
        self.stats.mediaUdienzeCivili = 2
        self.stats.mediaUdienzePenali = 12
        self.stats.mediaUdienzeAmministrative = 5
        self.stats.mediaUdienzeMinorili = 3


    def testCalcoloStatistiche(self):
        self.assertIsNotNone(self.stats)
        self.assertEqual(self.stats.mediaUdienzeMensili, 6)
        self.assertEqual(self.stats.mediaUdienzeAmministrative, 5)
        self.assertEqual(self.stats.mediaUdienzeCivili, 2)
        self.assertEqual(self.stats.numeroAppuntamenti, 15)
        self.assertEqual(self.stats.mediaUdienzeMinorili, 3)
        self.assertEqual(self.stats.mediaUdienzePenali, 12)
