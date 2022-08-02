from datetime import datetime, timedelta
from Servizi.Cliente import Cliente
from Servizi.Appuntamento import Appuntamento
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time
import os

class GestoreEmail:

    def __init__(self):
       self.Cliente = Cliente
       self.contenuto = []
       self.dataOra = datetime.datetime(year=1970, month=1, day=1, hour=00, minute=00)

    #se voglio fare la verifica sul cliente dovrei inserirlo negli attributi
    def gestoreEmail(self):

        #if ricercaUtilizzatoreId(self, Cliente.ID)

        #cliente come parametro?
    def getDatiAppuntamento(self):

        """
            if os.path.isfile('Dati\Appuntamenti.pickle'):
                with open('Dati\Appuntamenti.pickle', 'rb') as f:
                    appuntamenti = dict(pickle.load(f))
                    for appuntamento in appuntamenti.values():
                        if appuntamento.Cliente is Cliente:
                            return appuntamento
                    return None
            else:
                return None
        """


    #il cliente come attributo?
    def invioEmail(self):

        # dataInvio = appuntamento del cliente - timedelta(days=1)

        while now != dataInvio:
            now = datetime.now()
            time.sleep(300)


        if now == dataInvio:
            #inizio la connesione con il server della mia email (ancora da definire)
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.ehlo()
            smtp.starttls()

            #faccio il login
            smtp.login('YourMail@gmail.com', 'Your Password')

            msg = MIMEMultipart()

            #oggetto dell'email
            msg['Subject'] = subject

            #contenuto testuale
            msg.attach(MIMEText(text))

            #utilizzatore?
            to = Cliente.email

            smtp.sendmail(from_addr="hello@gmail.com",
                      to_addrs=to, msg=msg.as_string())

            smtp.quit()






