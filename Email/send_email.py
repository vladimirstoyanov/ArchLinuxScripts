import smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

class SendEmail:
    def __init__ (self, port, smtpServer, senderEmail, receiverEmail, password, name):
        self.port = port
        self.smtpServer = smtpServer
        self.senderEmail = senderEmail
        self.receiverEmail = receiverEmail
        self.password = password
        self.name = name

    def sendEmail (self, subject, bodyText):
        body = bodyText
        message = MIMEMultipart()
        message["From"] = str(Header(self.name + '<' + self.senderEmail + '>'))
        message["To"] = self.receiverEmail
        message["Subject"] = subject
        message["Bcc"] = self.receiverEmail
        message.attach(MIMEText(body, 'plain'))

        context = ssl.create_default_context()
        print("Trying to connect to server: " + self.smtpServer)
        server = smtplib.SMTP_SSL(self.smtpServer, self.port, context )
        print("Trying to login with id: " + self.senderEmail)
        server.login(self.senderEmail, self.password)
        server.sendmail(self.senderEmail, self.receiverEmail, message.as_string())
        print("Email has been sent.")
        server.quit()
