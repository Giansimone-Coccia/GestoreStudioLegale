from datetime import datetime, timedelta
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time
import os

class GestoreEmail:

    def __init__(self):
       self.Cliente = Cliente
       self.contenuto = ''
       self.dataOra = datetime.datetime(year=1970, month=1, day=1, hour=00, minute=00)

    #per gestire eventuali errori (es email non trovata)
    #def gestoreEmail(self):

        #if ricercaUtilizzatoreId(self, Cliente.ID)

        #cliente come parametro?
    def getDatiAppuntamento(self):
        return self.Appuntamento.getDatiAppuntamento()


    #il cliente come attributo?
    def invioEmail(self, emailStudio, cliente):

        dataInvio = self.getDatiAppuntamento().get('Data e Ora Inizio', None) - timedelta(days=1) #riguarda il delta

        now = datetime.now()
    '''
        #togliere il login
        
        while now != dataInvio:
            now = datetime.now()
            time.sleep(300)


        if now == dataInvio:
            #inizio la connesione con il server della mia email (ancora da definire)
            smtp = smtplib.SMTP(emailStudio, 587)
            smtp.ehlo()
            smtp.starttls()

            #faccio il login
            smtp.login('YourMail@gmail.com', 'Your Password')
    '''
            msg = MIMEMultipart()

            #oggetto dell'email
            msg['Subject'] = subject

            #contenuto testuale
            msg.attach(MIMEText('Le ricordiamo che il suo appuntamento è in data: ' + self.getDatiAppuntamento().get('Data e Ora Inizio', None)))

            #utilizzatore?
            to = cliente.getInfoUtilizzatore().get('email', None)

            smtp.sendmail(from_addr="hello@gmail.com",
                      to_addrs=to, msg=msg.as_string())

            smtp.quit()