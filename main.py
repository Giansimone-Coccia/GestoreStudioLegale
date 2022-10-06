#from PyQt5.uic.properties import QtWidgets
#from GestoreStudioLegale.Viste.LoginCliente import Ui_Form
import sys
from os import name

from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
from PyQt5.QtWidgets import QApplication

from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento
from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Servizi.Parcella import Parcella
from GestoreStudioLegale.Servizi.Udienza import Udienza
#from GestoreStudioLegale.Sistema.GestoreEmail import GestoreEmail
from GestoreStudioLegale.Gestione.Statistiche import Statistiche
from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
from GestoreStudioLegale.Gestione.Backup import Backup
from GestoreStudioLegale.Sistema.CorsoAggiornamento import CorsoAggiornamento
from GestoreStudioLegale.Sistema.GestoreEmail import GestoreEmail
from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VistaHome import VistaHome


cliente1 = Cliente()
cliente2 = Cliente()
cliente3 = Cliente()
cliente4 = Cliente()
cliente5 = Cliente()
cliente6 = Cliente()
cliente7 = Cliente()
avvocato1 = Avvocato()
avvocato2 = Avvocato()
udienza1 = Udienza()
udienza2 = Udienza()
udienza3 = Udienza()
udienza4 = Udienza()
udienza5 = Udienza()
udienza6 = Udienza()
udienza7 = Udienza()
appuntamento1 = Appuntamento()
appuntamento2 = Appuntamento()
appuntamento3 = Appuntamento()
appuntamento4 = Appuntamento()
appuntamentiL = [appuntamento1, appuntamento2]
appuntamentiL2 = [appuntamento4, appuntamento3]
parcella1 = Parcella()
parcella2 = Parcella()
parcella3 = Parcella()
corso1 = CorsoAggiornamento()
email = GestoreEmail()

corsi = ['economia politica']
appuntamentiAvvocato = ['martedì', 'mercoledì']
licenze = []
a = ['bo']
b = ['non so']
listaClienti = [cliente1, cliente2, cliente3]
nuovaListaClienti = []
corsoAggiornamentiLista = ['matematica', 'analisi 2']
parcelleL = [parcella1, parcella2]
parcelleL1 = [parcella3]
udienzeC = [udienza1, udienza2]
udienzeA = [udienza3,udienza4]
udienzeGen = [udienza1, udienza2, udienza3, udienza4]

cliente1.creaCliente('cc', 'djfsffjc', corsi, '25/09/2000', 'mail@gwwwmail.com', 'C123ew4', 45254534, 'p', appuntamentiL, parcelleL, 'alesseio', udienza1)
cliente2.creaCliente('dfskfjfsb', 'djfsjc', corsi, '25/09/2000', 'mail@gmail.com', 'C1254', 45254534, 'pswrd', appuntamentiL2, parcelleL1, 'alessio', udienza3)
cliente3.creaCliente('abcdefgd', 'ertyuio', corsi, '24/9/2011', 'mail234@gmail.com', 'C9923', 56666536, 'pswrd1', appuntamento2, parcella3, 'angelo', udienza2)
#cliente1.creaCliente('cc', 'djfsjc', corsi, '25/9/2000', 'mail@gmail.com', 'C1234', 45254534, 'p', appuntamento1, parcella1, 'alessio', udienza1)
#cliente2.creaCliente('dfskfjfsb', 'djfsjc', corsi, '25/9/2000', 'mail@gmail.com', 'C1254', 45254534, 'pswrd', appuntamento1, parcella1, 'alessio', udienza1)
#cliente1.creaCliente('cc', 'djfsffjc', corsi, '25/9/2000', 'mail@gwwwmail.com', 'C123ew4', 45254534, 'p', appuntamento1, parcella1, 'alesseio', udienza1)
#cliente2.creaCliente('dfskfjfsb', 'djfsjc', corsi, '25/9/2000', 'mail@gmail.com', 'C1254', 45254534, 'pswrd', appuntamento1, parcella1, 'alessio', udienza1)
#cliente1.creaCliente('cc', 'djfsjc', corsi, '25/9/2000', 'mail@gmail.com', 'C1234', 45254534, 'p', appuntamento1, parcella1, 'alessio', udienza1)
#cliente2.creaCliente('dfskfjfsb', 'djfsjc', corsi, '25/9/2000', 'mail@gmail.com', 'C1254', 45254534, 'pswrd', appuntamento1, parcella1, 'alessio', udienza1)
#cliente1.creaCliente('cc', 'djfsffjc', corsi, '25/9/2000', 'mail@gwwwmail.com', 'C123ew4', 45254534, 'p', appuntamento1, parcella1, 'alesseio', udienza1)
#cliente2.creaCliente('dfskfjfsb', 'djfsjc', corsi, '25/9/2000', 'mail@gmail.com', 'C1254', 45254534, 'pswrd', appuntamento1, parcella1, 'alessio', udienza1)
#cliente1.creaCliente('cc', 'djfsjc', corsi, '25/9/2000', 'mail@gmail.com', 'C1234', 45254534, 'p', appuntamento1, parcella1, 'alessio', udienza1)
#cliente2.creaCliente('dfskfjfsb', 'djfsjc', corsi, '25/9/2000', 'mail@gmail.com', 'C1254', 45254534, 'pswrd', appuntamento1, parcella1, 'alessio', udienza1)

#cliente1.getDatiCliente()  #FUNZIONA FACENDO PRIMA AGGIUNGICLIENTE COSI' FA PRIMA CREAUTILIZZATORE
#print(cliente1.dataNascita)
#cliente2.getDatiCliente()
#cliente3.getDatiCliente()
#cliente1.ricercaUtilizzatoreEmail('albero@gmail.com') #FUNZIONA
#cliente1.ricercaUtilizzatoreEmail('mail@gmail.com') #FUNZIONA
#cliente1.ricercaUtilizzatoreId('1234')  #FUNZIONA
#cliente1.ricercaUtilizzatoreId('C1234') #FUNZIONA
#cliente1.ricercaUtilizzatoreNomeCognome("luca", "ndkndk")  #FUNZIONA
#cliente1.ricercaUtilizzatoreNomeCognome("alessio", "djfsjc")  #FUNZIONA
#cliente1.rimuoviCliente("5678")  #FUNZIONA
#cliente1.rimuoviCliente("C1234")  #FUNZIONA
#cliente1.visualizzaCliente("dandndisnkaj")  #FUNZIONA
#cliente1.visualizzaCliente("C1234")  #FUNZIONA
#cliente1.aggiornaCliente('almail@gmil.com')

#avvocato1.creaAvvocato('jhsdkcdks', 'dilio', 'alberto', corsoAggiornamentiLista, '2/4/1995', 'albe@outlook.com', 'A4783', 4738203754, 'passAvv', udienzeGen, listaClienti, licenze, appuntamentiAvvocato) #FUNZONA
#avvocato2.creaAvvocato('abcdefg', 'marozzi', 'luca', corsoAggiornamentiLista, '23/12/1995', 'albe4382@outlook.com', 'B4783', 1233754, 'passAvv2', udienzeGen, listaClienti, licenze, appuntamentiAvvocato)
#avvocato1.getDatiAvvocato() #FUNZIONA INISIME A CREAAVVOCATO
#avvocato1.ricercaUtilizzatoreId('A4783') #FUNZIONA
#avvocato1.ricercaUtilizzatoreId('id non valido') #FUNZIONA
#avvocato1.ricercaUtilizzatoreEmail('albe@outlook.com') #FUNZIONA
#avvocato1.ricercaUtilizzatoreEmail('emailAcaso') #FUNZIONA
#avvocato1.ricercaUtilizzatoreNomeCognome('alberto', 'dilio') #FUNZIONA
#avvocato1.ricercaUtilizzatoreNomeCognome('alberto', 'sbagliato') #FUNZIONA
#avvocato1.rimuoviAvvocato('A4783') #FUNZIONA
#avvocato1.rimuoviAvvocato('errato') #FUNZIONA
#avvocato1.visualizzaAvvocato('A4783') #FUNZIONA
#avvocato1.aggiornaAvvocato(nuovaListaClienti, 3620988123)
#print(avvocato2.getDatiAvvocato()['clienti'])

parcella1.creaParcella(cliente1, 'PP456', 123456789, 1235, 'alessio') #FUNZIONA
parcella2.creaParcella(cliente1, 'PP123', 583928493, 2000, 'francesca')
#parcella3.creaParcella(cliente2, 'PP678', 432455653, 3444, 'marco')
#print(cliente1.getDatiCliente()['parcelle'])
#print('si')
#parcella1.getDatiParcellaCliente() #FUNZIONA UTILIZZANDOLO INSIEME A creaParcella
#parcella1.ricercaParcellaCliente(cliente1) #FUNZIONA
#parcella1.ricercaParcellaIntestatario('giorgio') #FUNZIONA
#parcella1.ricercaParcellaIntestatario('nomeAcaso') #FUNZIONA
#parcella1.ricercaParcellaIdentificativo(123456789)
#parcella1.ricercaParcellaIdentificativo(48729852)
#parcella1.rimuoviParcella('PP456') #FUNZIONA
#parcella1.rimuoviParcella('PP0000') #FUNZIONA
#parcella1.getDatiParcellaCliente() #FUNZIONA
#parcella2.getDatiParcellaCliente()
#parcella3.getDatiParcellaCliente()
udienza1.creaUdienza(avvocato1, 'Ascoli Piceno', cliente1, '10/08/2022,12:00','10/08/2022,13:00','U2345','civile') #FUNZIONA
#udienza1.creaUdienza(avvocato1, 'Ascoli Piceno', cliente1, '10/08/2022,12:00','10/08/2022,13:00','U2345','civile') #FUNZIONA
udienza2.creaUdienza(avvocato2, 'Roma', cliente2, '21/2/2022,15:00','21/12/2021,19:00','U7765','penale') #FUNZIONA
#udienza1.getDatiUdienza() #FUNZIONA

#cliente1 = udienza1.getDatiUdienza()['Cliente']
print(udienza1.getDatiUdienza()['Cliente'].getDatiCliente())
print(cliente1.getDatiCliente())
print('ciao')
#udienza2.getDatiUdienza() #FUNZIONA
#listaUdienze = udienza1.ricercaUdienzaCliente(cliente1) #DA RICONTROLLARE DOPO AVER SISTEMATO LA CLASSE CLIENTE
#print(listaUdienze)
#udienzaTr= udienza1.ricercaUdienzaDataInizio('21/12/2021,15:00') #FUNZIONA
#print(udienzaTr)
#udienzaT=udienza1.ricercaUdienzaID('U2345') #FUNZIONA
#print(udienzaT)
#udienzaTro= udienza1.ricercaUdienzaTipo('penale') #FUNZIONA
#print(udienzaTro)
#print(udienza1)
#udienzaT.getDatiUdienza() #FUNZIONA
#udienzaTr.getDatiUdienza() #FUNZIONA
#udienza1.rimuoviUdienza('U2345') #FUNZIONA
#udienza1.rimuoviUdienza('U2765') #FUNZIONA

udienza3.creaUdienza(avvocato2, 'Bari', cliente2, '9/08/2022,12:00','10/08/2022,13:00','U299345','amministrativa')
udienza4.creaUdienza(avvocato1, 'Roma', cliente4, '22/2/2022,15:00','23/12/2022,19:00','U276865','penale')
#udienza5.creaUdienza(avvocato1, 'Ascoli Piceno', cliente5, '11/08/2022,12:00','12/08/2022,13:00','U26345','civile')
#udienza6.creaUdienza(avvocato1, 'Roma', cliente6, '20/2/2022,15:00','21/12/2022,19:00','U27965','penale')
#udienza7.creaUdienza(avvocato1, 'Roma', cliente7, '20/2/2022,15:00','21/12/2022,19:00','U25965','amministrativa')
#udienza5.creaUdienza(avvocato1, 'Ascoli Piceno', cliente5, '11/08/2022,12:00','12/08/2022,13:00','U26345','civile')
#udienza6.creaUdienza(avvocato1, 'Roma', cliente6, '20/2/2022,15:00','21/12/2022,19:00','U27965','penale')
#udienza7.creaUdienza(avvocato1, 'Roma', cliente7, '20/2/2022,15:00','21/12/2022,19:00','U25965','amministrativa')
#udienza3.creaUdienza(avvocato1, 'Ascoli Piceno', cliente3, '9/08/2022,12:00','10/08/2022,13:00','U299345','civile')
#udienza4.creaUdienza(avvocato1, 'Roma', cliente4, '22/2/2022,15:00','23/12/2022,19:00','U276865','penale')
#udienza5.creaUdienza(avvocato1, 'Ascoli Piceno', cliente5, '11/08/2022,12:00','12/08/2022,13:00','U26345','civile')
#udienza6.creaUdienza(avvocato1, 'Roma', cliente6, '20/2/2022,15:00','21/12/2022,19:00','U27965','penale')
#udienza7.creaUdienza(avvocato1, 'Roma', cliente7, '20/2/2022,15:00','21/12/2022,19:00','U25965','amministrativa')
#udienza5.creaUdienza(avvocato1, 'Ascoli Piceno', cliente5, '11/08/2022,12:00','12/08/2022,13:00','U26345','civile')
#udienza6.creaUdienza(avvocato1, 'Roma', cliente6, '20/2/2022,15:00','21/12/2022,19:00','U27965','penale')
#udienza7.creaUdienza(avvocato1, 'Roma', cliente7, '20/2/2022,15:00','21/12/2022,19:00','U25965','amministrativa')

#stats = Statistiche()
#stats.calcolaStatistiche()
#stats.salvaSuFile()
#print(stats.leggiFile())
#stats.mostraGrafico() #FUNZIONA
#print(stats.mostraStatistiche("udienze penali"))

#gestore = GestoreSistema()
#gestore.loginCliente('pswrd','dfskfjfsb') #FUNZIONA
#gestore.loginCliente('pswrdErrata','dfskfjfsb') #FUNZIONA
#gestore.loginAvvocato('passAvv', 'jhsdkcdks') #FUNZIONA MA STAMPA OGGETTI
#gestore.loginAvvocato('passAvv', 'CFErrato') #FUNZIONA MA STAMPA OGGETTI
#gestore.loginAdmin('password', 'admin') #FUNZIONA
#gestore.loginAdmin('passwordErrata', 'admin') #FUNZIONA
#gestore.loginAdmin('password', 'Sbagliato') #FUNZIONA
#gestore.modificaCredenzialiAdmin('nuova', 'newUs') #FUNZIONA
#gestore.modificaCredenzialiAdmin('nuova') #FUNZIONA
#gestore.rimuoviAvvocato(avvocato1) #FUNZIONA
#gestore.rimuoviCliente(cliente1) #FUNZIONA
#gestore1.invioEmail() #NON ACORA TESTATO

#corso1.creaCorso('matematica',3,'CR123','21/08/2022,15:00','21/08/2022,21:00','formazione') #FUNZIONA
#corso1.getDatiCorso()
#corso1.ricercaCorsoCodice('CR123') #FUNZIONA
#corso1.ricercaCorsoNome('matematica') #FUNZIONA
#corso1.ricercaCorsoTipo('formazione') #FUNZIONA
#corso1.rimuoviCorso('CR123') #FUNZIONA

#backup = Backup()
#backup.eseguiBackup()
#cliente8=backup.getDatiBakcup()['clienti'][0]
#print(cliente8)
appuntamento1.creaAppuntamento(cliente1, avvocato1, '9/08/2022,12:00','10/08/2022,13:00', 'A3245', 'civile') #FUNZIONA
appuntamento2.creaAppuntamento(cliente1, avvocato2,  '23/11/2022,12:00','10/08/2022,15:00', 'B7845', 'civile')
appuntamento3.creaAppuntamento(cliente2, avvocato1,  '30/09/2022,14:26','30/09/2022,16:00', 'A76fry5', 'civile')
appuntamento4.creaAppuntamento(cliente2, avvocato1,  '30/09/2022,14:21','30/09/2022,16:00', 'A5825667', 'civile')
#print(appuntamentiL)
#print(appuntamento1.getDatiAppuntamento())
#email.invioEmail()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    vista_home = VistaHome()
    vista_home.show()
    sys.exit(app.exec())