from unittest import TestCase

from GestoreStudioLegale.Gestione.Statistiche import Statistiche
from GestoreStudioLegale.Servizi.Udienza import Udienza


class TestStatistiche(TestCase):
    def setUp(self):
        '''self.udienza3 = Udienza()
        self.udienza4 = Udienza()
        self.udienza5 = Udienza()
        self.udienza6 = Udienza()
        self.udienza7 = Udienza()
        self.udienza3.creaUdienza(None, 'Bari', None, '9/08/2022,12:00','10/08/2022,13:00','U299345','amministrativa')
        self.udienza4.creaUdienza(None, 'Roma', None, '22/2/2022,15:00','23/12/2022,19:00','U276865','penale')
        self.udienza5.creaUdienza(None, 'Ascoli Piceno', None, '11/08/2022,12:00','12/08/2022,13:00','U26345','civile')
        self.udienza6.creaUdienza(None, 'Roma', None, '20/2/2022,15:00','21/12/2022,19:00','U27965','penale')
        self.udienza7.creaUdienza(None, 'Roma', None, '20/2/2022,15:00','21/12/2022,19:00','U25965','amministrativa')
        self.stats = Statistiche()
        self.stats.calcolaStatistiche()
        self.stats.salvaSuFile()
        self.d = self.stats.leggiFile()'''
        #Statistiche.calcolaStatistiche()
        #print(Statistiche.leggiFile())
        #print(self.stats.mediaUdienzeAmministrative)
        #self.stats.salvaSuFile()
        #self.stats.leggiFile()
        self.stats = Statistiche()
        print(self.stats.mediaUdienzeAmministrative)
        self.stats.calcolaStatistiche()
        print(self.stats.mediaUdienzeAmministrative)


    def testCalcoloStatistiche(self):
        #print(self.d)
        pass
        #print(self.stats.mediaUdienzeAmministrative)
        ''''#self.assertEqual(self.stats.mediaUdienzeMensili, 2)
        self.assertEqual(self.stats.mediaUdienzeMensili, 0)
        #self.assertEqual(self.stats.mediaUdienzeAmministrative, 1)
        self.assertEqual(self.stats.mediaUdienzeAmministrative, 0)
        #self.assertEqual(self.stats.mediaUdienzeCivili, 1)
        self.assertEqual(self.stats.mediaUdienzeCivili, 0)
        #self.assertEqual(self.stats.numeroAppuntamenti, 12)
        self.assertEqual(self.stats.numeroAppuntamenti, 0)
        d = self.stats.leggiFile()
        print(d)
        print(self.stats.mediaUdienzeCivili)
        print(self.stats.numeroAppuntamenti)
        print(self.stats.mediaUdienzeAmministrative)
        print(self.stats.mediaUdienzeMensili)
        print(self.stats.mediaUdienzeMinorili)
        print(self.stats.mediaUdienzePenali)
        print(self.stats.leggiFile())
        #print(self.stats.leggiFile()['Amministrative'])'''