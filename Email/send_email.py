import smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmail:
    def __init__ (self, port, smtpServer, senderEmail, receiverEmail, password):
        self.port = port
        self.smtpServer = smtpServer
        self.senderEmail = senderEmail
        self.receiverEmail = receiverEmail
        self.password = password

    def sendEmail (self, subject, bodyText):
        body = bodyText
        password = self.password
        message = MIMEMultipart()
        message["From"] = self.senderEmail
        message["To"] = self.receiverEmail
        message["Subject"] = subject
        message["Bcc"] = self.receiverEmail
        message.attach(MIMEText(body, 'plain'))

        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(smtp_server, self.port, context )
        server.login(self.senderEmail, self.password)
        server.sendmail(self.SendEmail, self.receiverEmail, message.as_string())
        server.quit()
