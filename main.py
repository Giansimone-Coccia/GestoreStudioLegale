from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento
from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Servizi.Parcella import Parcella
from GestoreStudioLegale.Servizi.Udienza import Udienza

cliente1 = Cliente()
avvocato1 = Avvocato()
udienza1 = Udienza()
appuntamento1 = Appuntamento()
parcella1 = Parcella()

corsi = ['economia politica']
appuntamentiAvvocato = ['martedì', 'mercoledì']
licenze = []
a = ['bo']
b = ['non so']
listaClienti = [cliente1]
nuovaListaClienti = []
corsoAggiornamentiLista = ['matematica', 'analisi 2']

#cliente1.aggiungiCliente('dfskfjfsb', 'djfsjc', corsi, '25/9/2000', 'mail@gmail.com', 'C1234', 45254534, 'pswrd', appuntamento1, parcella1, 'alessio', udienza1)
#cliente1.getDatiCliente()  #FUNZIONA FACENDO PRIMA AGGIUNGICLIENTE COSI' FA PRIMA CREAUTILIZZATORE
#print(cliente1.dataNascita)
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

#avvocato1.creaAvvocato('jhsdkcdks', 'dilio', 'alberto', corsoAggiornamentiLista, '2/4/1995', 'albe@outlook.com', 'A4783', 4738203754, 'passAvv', udienza1, listaClienti, licenze, appuntamentiAvvocato) #FUNZONA
#avvocato1.getDatiAvvocato() #FUNZIONA
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

#parcella1.creaParcella(cliente1, 'PP456', 123456789, 1235, 'giorgio') #FUNZIONA
#parcella1.getDatiParcellaCliente() #FUNZIONA UTILIZZANDOLO INSIEME A creaParcella
parcella1.ricercaParcellaCliente(cliente1) #FUNZIONA
#parcella1.ricercaParcellaIntestatario('giorgio') #FUNZIONA
#parcella1.ricercaParcellaIntestatario('nomeAcaso') #FUNZIONA
#parcella1.ricercaParcellaIdentificativo(123456789)
#parcella1.ricercaParcellaIdentificativo(48729852)
#parcella1.rimuoviParcella('PP456') #FUNZIONA
#parcella1.rimuoviParcella('PP0000') #FUNZIONA
#parcella1.visualizzaParcella('PP456') #FUNZIONA


