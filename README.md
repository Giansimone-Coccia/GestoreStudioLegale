# GestoreStudioLegale
Progetto d'esame basato sullo sviluppo di un software gestionale per uno studio legale per l'esame di Ingegneria del software A.A 2021/2022

![](https://github.com/Giansimone-Coccia/GestoreStudioLegale/blob/main/logo.png)   

## 1.1 REGOLE PER IL CORRETTO UTILIZZO
### Avvio del software
Scaricare l'intero progetto sul proprio pc ed aprirlo con un IDE (PyCharm).
Se non lo avete già fatto, mandando in esecuzione il programma, l'IDE vi chiederà di installare alcuni pacchetti/librerie esterne. E' possibile farlo utilizzando il comando **pip install**
  - pip install PyQt5

### Primo accesso
Il primo inserimento dei clienti o degli avvocati avviene tramite l'amministratore che, per convenzione ha delle credenziali di default che possono essere successivamente modificate. Queste sono:

  - **username:** user
  - **password:** password

## 1.2 STRUTTURA DEL SOFTWARE
Le informazioni raccolte hanno evidenziato i possibili utenti di un software per uno studio legale: gli avvocati, i clienti e l’amministratore dello studio. Per rispettare questa esigenza il nostro software si suddivide principalmente in tre sezioni una per ogni utente. Altra caratteristica che risultava importante era avere la possibilità di visualizzare e gestire agilmente le informazioni relative alle parcelle, alle udienze, agli appuntamenti e ai corsi di aggiornamento. 
I vari utenti hanno delle aree riservate, per accedervi:
avvocati e clienti hanno come username il proprio codice fiscale e una password assegnatagli al momento della creazione del profilo
l’amministratore ha un username e una password di default che può sostituire una volta fatto l’accesso alla propria sezione.

### 1.2.1 SEZIONE RISERVATA AGLI AVVOCATI
Gli avvocati accedendo al software, nella loro area riservata, potranno svolgere tutte le attività legate alla gestione degli appuntamenti, delle parcelle, delle udienze, dei clienti e dei corsi di aggiornamento. 
L’avvocato può creare un cliente per aggiungerlo alla propria lista di clienti, inserendo nome, cognome, codice fiscale, data di nascita, email, Id, numero di telefono e password oppure può aggiungere alla sua lista di clienti un cliente che già è salvato nei file del sistema inserendo l’Id.
Per quanto riguarda gli appuntamenti, l’avvocato può creare un appuntamento inserendo il cliente a cui si rivolge, la data, l’orario di inizio e il tipo di procedimento; una volta creati gli appuntamenti sarà possibile visualizzarli e anche ricercarli tramite l’ID (viene inserito automaticamente dal sistema). Nel caso in cui ci sia una modifica di giorno o di ora, a causa di impegni o dell’avvocato o del cliente, è possibile modificare la data e l’ora. Se l’appuntamento dovesse essere annullato, l’avvocato può anche eliminarlo dalla sua lista di appuntamenti. 
Per quanto riguarda le parcelle, l’avvocato può inserire una parcella per un cliente specificando l’intestatario, l’importo, il cliente e l’identificativo; una volta creata, sarà anche possibile modificare i campi dell’importo e dell’intestatario. Sarà consentito anche eliminare una parcella e ricercare tutte le parcelle relative ad un cliente tramite il “codice fiscale”. 
Per quanto riguarda le udienze, l’avvocato ha la possibilità di inserire un’udienza compilando i campi relativi alla data, all’ora, al tipo di procedimento, al cliente e alla città del tribunale. Una volta inserita l’udienza, verrà visualizzata insieme a tutte quelle già precedentemente inserite. L’avvocato dispone della possibilità di modificare i campi di data e ora ma anche di eliminare un’udienza e di ricercare e visualizzare tutte le udienze relative ad un suo specifico cliente. Tutte le azioni di creazione di parcelle, udienze e appuntamenti possono essere rivolte solo ai propri clienti.  
Oltre queste attività, l’avvocato ha anche la possibilità di scegliere un corso di aggiornamento da aggiungere alla sua lista in modo tale da visualizzare la durata del corso e il numero di crediti che offre.  

### 1.2.2 SEZIONE RISERVATA  AI CLIENTI
Accedendo alla propria area un cliente può visualizzare tutte le informazioni relative agli appuntamenti effettuati o da effettuare, le parcelle e le udienze, così da sapere sia quali saranno i prossimi impegni sia visualizzare uno storico.
Il cliente inoltre ha la possibilità di prenotare un appuntamento selezionando data, ora, il tipo di procedimento e l’avvocato a cui vuole rivolgersi. L’appuntamento verrà confermato sempre tranne nel caso in cui ci siano sovrapposizioni di orario con altri appuntamenti dell’avvocato.

### 1.2.3 SEZIONE RISERVATA  ALL’AMMINISTRATORE
La sezione riservata all’amministratore permette di eseguire operazioni sui profili degli avvocati e dei clienti:
creare un profilo inserendo nome, cognome, codice fiscale, data di nascita, email, Id, numero di telefono e password 
modificare tutti i campi
eliminare un profilo 
ricercare, tramite ID, un singolo profilo tra la lista di tutti gli avvocati/clienti presenti
L’amministratore può, inoltre, visualizzare le statistiche relative al numero medio di appuntamenti mensili e di udienze (le statistiche delle udienze sono calcolate anche in base alla tipologia di udienza). 
Per quanto riguarda i corsi di aggiornamento, l’amministratore può inserirli nel sistema (inserendo la data iniziale, il nome del corso, i crediti, il tipo del corso e  ), ricercarli tramite ID e eliminarli.

### 1.2.4 FUNZIONALITA’ AUTOMATICHE DEL SOFTWARE
Tutti i dati raccolti sono assicurati attraverso un backup automatico del sistema all’avvio del programma.
Un’ulteriore funzione del software è l’invio automatico di email al cliente (solo nel caso in cui abbia una casella di posta elettronica “gmail”) per ricordare un appuntamento (24h prima).


