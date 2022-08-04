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

corsi = []
appuntamentiAvvocato = []
licenze = []
a = []
b = []
listaClienti = [cliente1]

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
cliente1.aggiornaCliente('almail@gmil.com')
