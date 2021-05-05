import smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage


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

    def sendEmailWithAttachment (self, subject, bodyText, attachment):
        strFrom = self.senderEmail
        strTo = self.receiverEmail

        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject
        msgRoot['From'] = str(Header(self.name + '<' + self.senderEmail + '>'))
        msgRoot['To'] = strTo

        msgRoot.preamble = '====================================================='

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        msgText = MIMEText('This object contains the plain text content of this email.')
        msgAlternative.attach(msgText)

        msgText = MIMEText(bodyText, 'html')
        msgAlternative.attach(msgText)

        fp = open(attachment, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)

        server = None

        print("Trying to connect to server: " + self.smtpServer)
        print ("Port: " + str(self.port))
        if (self.port!=587):
            context = ssl.create_default_context()
            server = smtplib.SMTP_SSL(self.smtpServer, self.port, context )
        if (self.port == 587):
            server = smtplib.SMTP(self.smtpServer, self.port)
            server.starttls()
        print("Trying to login with id: " + self.senderEmail)
        server.login(self.senderEmail, self.password)
        server.sendmail(self.senderEmail, self.receiverEmail, msgRoot.as_string())
        print("Email has been sent.")
        server.quit()
