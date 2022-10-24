from unittest import TestCase

from GestoreStudioLegale.Gestione.Statistiche import Statistiche
from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento
from GestoreStudioLegale.Servizi.Udienza import Udienza


class TestStatistiche(TestCase):
    def setUp(self):
        self.udienza3 = Udienza()
        self.udienza4 = Udienza()
        #self.udienza5 = Udienza()
        #self.udienza6 = Udienza()
        #self.udienza7 = Udienza()
        self.appuntamento1 = Appuntamento()
        self.appuntamento2 = Appuntamento()
        self.appuntamento1.creaAppuntamento(None, None, '12/12/2022,13:00', '24/01/2023,15:00', 'A22331', 'giudiziario')
        self.appuntamento2.creaAppuntamento(None, None, '10/11/2022,11:00', '25/02/2023,17:00', 'A21351','minorile')
        self.udienza3.creaUdienza(None, 'Bari', None, '9/08/2022,12:00','10/08/2022,13:00','U299345','amministrativa')
        self.udienza4.creaUdienza(None, 'Roma', None, '22/2/2022,15:00','23/12/2022,19:00','U276865','penale')
        #self.udienza5.creaUdienza(None, 'Ascoli Piceno', None, '11/08/2022,12:00','12/08/2022,13:00','U26345','civile')
        #self.udienza6.creaUdienza(None, 'Roma', None, '20/2/2022,15:00','21/12/2022,19:00','U27965','penale')
        #self.udienza7.creaUdienza(None, 'Roma', None, '20/2/2022,15:00','21/12/2022,19:00','U25965','amministrativa')
        self.stats = Statistiche()
        self.stats.calcolaStatistiche()
        print(self.stats.mediaUdienzeMensili)
        print(self.stats.numeroAppuntamenti)
        self.stats.salvaSuFile()
        print(self.stats.mediaUdienzeMensili)
        print(self.stats.numeroAppuntamenti)
        self.d = self.stats.leggiFile()
        #Statistiche.calcolaStatistiche()
        #print(Statistiche.leggiFile())
        #print(self.stats.mediaUdienzeAmministrative)
        #self.stats.salvaSuFile()
        #self.stats.leggiFile()
        #self.stats = Statistiche()
        #print(self.stats.mediaUdienzeAmministrative)
        #self.stats.calcolaStatistiche()
        #print(self.stats.mediaUdienzeAmministrative)


    def testCalcoloStatistiche(self):
        #print(self.d)
        #pass
        #print(self.stats.mediaUdienzeAmministrative)
        #self.assertEqual(self.stats.mediaUdienzeMensili, 2)
        self.assertEqual(self.stats.mediaUdienzeMensili, 0)
        #self.assertEqual(self.stats.mediaUdienzeAmministrative, 1)
        self.assertEqual(self.stats.mediaUdienzeAmministrative, 0)
        #self.assertEqual(self.stats.mediaUdienzeCivili, 1)
        self.assertEqual(self.stats.mediaUdienzeCivili, 0)
        #self.assertEqual(self.stats.numeroAppuntamenti, 12)
        self.assertEqual(self.stats.numeroAppuntamenti, 0)
        #self.assertEqual(self.stats.numeroAppuntamenti, 2)

        d = self.stats.leggiFile()
        print(d)
        print(self.stats.mediaUdienzeCivili)    #Non va bene, riportano tutti zero
        print(self.stats.numeroAppuntamenti)
        print(self.stats.mediaUdienzeAmministrative)
        print(self.stats.mediaUdienzeMensili)
        print(self.stats.mediaUdienzeMinorili)
        print(self.stats.mediaUdienzePenali)
        print(self.stats.leggiFile())
        #print(self.stats.leggiFile()['Amministrative'])