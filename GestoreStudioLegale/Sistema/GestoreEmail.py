from datetime import datetime, timedelta
import smtplib

from PyQt5.QtWidgets import QMessageBox

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
        contenuto = 'Appuntamento: '+'\n'+ 'TIPO PROCEDIMENTO: '+f"{self.getDatiApp()['Tipo Procedimento']}"+'\n'+'DATA E ORA INIZIO: '+f"{self.getDatiApp()['Data e Ora Inizio']}"+'\n'+'DATA E ORA FINE: '+f"{self.getDatiApp()['Data e Ora Fine']}"
        messaggio = oggetto + contenuto

        email = smtplib.SMTP("smtp.gmail.com", 587)

        email.ehlo()
        email.starttls()
        email.login("ProgettoStudioLegale0@gmail.com", "bzpklkbsziismfdv")

        print(self.getDatiApp()['Cliente'].email)
        email.sendmail("ProgettoStudioLegale0@gmail.com", self.getDatiApp()['Cliente'].email , messaggio.encode('utf-8'))
        email.quit()
      except Exception:
        self.problema()

    def getDatiApp(self):
        self.appuntamentiList = self.tool.loadAppuntamenti()
        for appuntamento in self.appuntamentiList:
            if appuntamento.getDatiAppuntamento()['Data e Ora Inizio'] == datetime.now().replace(second=0, microsecond=0) + timedelta(days=1):
                return appuntamento.getDatiAppuntamento()

    def problema(self):
        msg = QMessageBox()
        msg.setWindowTitle("Attenzione")
        msg.setText("Problema durante l'invio della e-mail")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()