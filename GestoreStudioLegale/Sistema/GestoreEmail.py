from datetime import datetime, timedelta
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time
import os

from GestoreStudioLegale.Utilities.Utilities import Tools


class GestoreEmail:

    def __init__(self):
        self.Appuntamento = None
        self.appuntamentiList = []
        self.tool = Tools()
        self.destinatario = ""

    def invioEmail(self):
      try:
        oggetto = "Si ricorda l'appuntamento presso lo studio legale \n"
        contenuto = 'Appuntamento: '+'\n'+ 'TIPO PROCEDIMENTO: '+f"{self.getDatiApp()['Tipo Procedimento']}"+'\n'+'ID: '+f"{self.getDatiApp()['ID']}"+'\n'+'DATA E ORA INIZIO: '+f"{self.getDatiApp()['Data e Ora Inizio']}"+'\n'+'DATA E ORA FINE: '+f"{self.getDatiApp()['Data e Ora Fine']}"
        messaggio = oggetto + contenuto

        email = smtplib.SMTP("smtp.gmail.com", 587)

        email.ehlo()
        email.starttls()
        email.login("ProgettoStudioLegale0@gmail.com", "bzpklkbsziismfdv")


        #emailDestinatari =
        email.sendmail("ProgettoStudioLegale0@gmail.com", "destinatario" , messaggio.encode('utf-8'))
        email.quit()
      except Exception:
        print("eccezione")

    def getDatiApp(self):
        self.appuntamentiList = self.tool.loadAppuntamenti()
        for appuntamento in self.appuntamentiList:
            if appuntamento.getDatiAppuntamento()['Data e Ora Inizio'] == datetime.now().replace(second=0, microsecond=0) + timedelta(days=1):
                return appuntamento.getDatiAppuntamento()



