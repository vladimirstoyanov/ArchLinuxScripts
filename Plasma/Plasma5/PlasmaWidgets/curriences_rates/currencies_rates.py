import urllib2
import smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

filename = '/tmp/currencies.txt'
port = 465  # For SSL
smtp_server = "smtp.abv.bg"
sender_email = "vlado_stoianov1988@abv.bg"  # Enter your address
receiver_email = "vlado_stoyanovi@yahoo.com"  # Enter receiver address
password = ""
password_path = '/home/vladimir/abv_pass'

sell_if_usd=1.95
sell_if_eur=2.2
sell_if_try_=0.45
sell_if_gbp=2.5

def set_the_password ():
    f = open (password_path, 'r')
    result = f.read()
    result = result.replace ('\n','')
    result = result.replace ('\r','')
    f.close()
    return result

def send_an_email (body_text):
    body = body_text
    password = set_the_password()
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "The currency has changed: "
    message["Bcc"] = receiver_email
    message.attach(MIMEText(body, 'plain'))

    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_server, port, context )
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()

def read_previous_results ():
    try:
        f = open (filename, 'r')
    except:
        print "File " + filename + " cannot be oppened."
        return [0,0,0,0], "error"

    l_result = []
    for str1 in f.readlines():
           l1 =  str1.split (' ')
           if (len(l1)<2):
                f.close()
                retun [0,0,0,0], "error"
           l_result.append(float(l1[1]))
    f.close()
    return l_result, "ok"


def download_web_page ():
    #get the information from https://www.ccbank.bg/bg/valutni-kursove
    return urllib2.urlopen("https://www.ccbank.bg/bg/valutni-kursove").read()

#code - USD for example. Check all codes here: https://www.ccbank.bg/bg/valutni-kursove; content - the source code of https://www.ccbank.bg/bg/valutni-kursove
def get_currency_by_code (code, content):
    #search for first <td>USD</td> <td>USD</td> <td>1.00</td> <td>1.7902</td> #serch for third <td> after <td>USD</td>

    index = content.find ('<td>' + code + '</td>')
    if (index == -1):
        return 0.0, "error"

    index+=len('<td>' + code + '</td>')
    #find next third <td>
    for i in range(2):
        index_tmp = content.find('<td>', index, len(content))
        if (index_tmp == -1):
            return 0.0, "error"
        index= index_tmp + len('<td>')

    end_index = content.find('</td>', index, len(content))
    if (end_index == -1):
        return 0.0, "error"

    amount = content[index:end_index]

    for i in range(2):
        index_tmp = content.find('<td>', index, len(content))
        if (index_tmp == -1):
            return 0.0, "error"
        index= index_tmp + len('<td>')

    end_index = content.find('</td>', index, len(content))
    if (end_index == -1):
        return 0.0, "error"

    currency_value = content[index:end_index]
    result = 0
    try:
       result = float(currency_value)/float(amount)
    except:
        return 0.0, "error"

    return result, "ok"

content = download_web_page()

usd, result_usd = get_currency_by_code('USD', content)
try_, result_try_ = get_currency_by_code('TRY', content)
gbp, result_gbp = get_currency_by_code('GBP', content)
eur, result_eur = get_currency_by_code('EUR', content)

l_previous_results, status = read_previous_results ()
print str(l_previous_results) + ", status: " + status

f = open('/tmp/currencies.txt', 'w')
f.write ('USD: ' + str(usd) + ' result: ' + result_usd + '\n')
f.write ('TRY: ' + str(try_) + ' result: ' + result_try_ +  '\n')
f.write ('GDP: ' + str(gbp) + ' result: ' + result_gbp +  '\n')
f.write ('EUR: ' + str(eur) + ' result: ' + result_eur + '\n')
f.close()

print ('USD: ' + str(usd) + ' result: ' + result_usd)
print ('TRY: ' + str(try_) + ' result: ' + result_try_)
print ('GBP: ' + str(gbp) + ' result: ' + result_gbp)
print ('EUR: ' + str(eur) + ' result: ' + result_eur)

#send an email
text_to_send = ''
if (l_previous_results[0]!=usd and usd!=0 and sell_if_usd<=usd):
    text_to_send+=('USD: ' + str(usd) + '\n')

if (l_previous_results[1]!=try_ and try_!=0 and sell_if_try_<=try_):
    text_to_send+=('TRY: ' + str(try_) + '\n')

if (l_previous_results[2]!=gbp and gbp!=0 and sell_if_gbp<=gbp):
    text_to_send+=('GBP: ' + str(gbp) + '\n')

if (l_previous_results[3]!=eur and eur!=0 and sell_if_eur<=eur):
    text_to_send+=('EUR: ' + str(eur) + '\n')

if (text_to_send!=''):
        print "Sending an email with the following text: " + text_to_send
        send_an_email(text_to_send)
