from datetime import datetime, timedelta
import smtplib

from PyQt5.QtWidgets import QMessageBox

from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento
from GestoreStudioLegale.Utilities.Utilities import Tools


class GestoreEmail:

    appuntamento = Appuntamento()
    tool = Tools()

    def __init__(self):
        self.destinatario = ""
        self.appuntamentiList = []

    def invioEmail(self):
        try:
            oggetto = "Si ricorda l'appuntamento presso lo studio legale \n"
            contenuto = 'Appuntamento: '+'\n'+ 'TIPO PROCEDIMENTO: '+f"{self.getDatiAppuntamento()['Tipo Procedimento']}"+'\n'+'DATA E ORA INIZIO: '+f"{self.getDatiAppuntamento()['Data e Ora Inizio']}"+'\n'+'DATA E ORA FINE: '+f"{self.getDatiAppuntamento()['Data e Ora Fine']}"
            messaggio = oggetto + contenuto

            email = smtplib.SMTP("smtp.gmail.com", 587)

            email.ehlo()
            email.starttls()
            email.login("ProgettoStudioLegale0@gmail.com", "bzpklkbsziismfdv")

            email.sendmail("ProgettoStudioLegale0@gmail.com", self.getDatiAppuntamento()['Cliente'].email , messaggio.encode('utf-8'))
            email.quit()
        except Exception:
            print("Non esiste un appuntamento fissato per domani")

    def getDatiAppuntamento(self):
        self.appuntamentiList = self.tool.loadAppuntamenti()
        for appuntamento in self.appuntamentiList:
            if appuntamento.getDatiAppuntamento()['Data e Ora Inizio'] == datetime.now().replace(second=0, microsecond=0) + timedelta(days=1):
                return appuntamento.getDatiAppuntamento()