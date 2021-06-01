import smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage


class SendEmail:
    def __init__ (self, port, smtpServer, senderEmail, receiverEmail, password, name):
        self.__port = port
        self.__smtpServer = smtpServer
        self.__senderEmail = senderEmail
        self.__receiverEmail = receiverEmail
        self.__password = password
        self.__name = name

    def __sendEmail (self, msgRoot):
        server = None
        print("Trying to connect to server: " + self.__smtpServer)
        print ("Port: " + str(self.__port))
        if (self.__port!=587):
                context = ssl.create_default_context()
                server = smtplib.SMTP_SSL(self.__smtpServer, self.__port, context )
        if (self.__port == 587):
                print ("Starting ttls...")
                server = smtplib.SMTP(self.__smtpServer, self.__port)
                server.starttls()
        print("Trying to login with id: " + self.__senderEmail)
        server.login(self.__senderEmail, self.__password)
        server.sendmail(self.__senderEmail, self.__receiverEmail, msgRoot.as_string())
        print("Email has been sent.")
        server.quit()

    def sendEmail (self, subject, bodyText):
        body = bodyText
        message = MIMEMultipart()
        message["From"] = str(Header(self.__name + '<' + self.__senderEmail + '>'))
        message["To"] = self.__receiverEmail
        message["Subject"] = subject
        message["Bcc"] = self.__receiverEmail
        message.attach(MIMEText(body, 'plain'))

        self.__sendEmail(message)

    def sendEmailWithAttachment (self, subject, bodyText, attachment):
        strFrom = self.__senderEmail
        strTo = self.__receiverEmail

        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject
        msgRoot['From'] = str(Header(self.__name + '<' + self.__senderEmail + '>'))
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

        self.__sendEmail(msgRoot)
