import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests, datetime
from bs4 import BeautifulSoup
email_sender_account = "1bi19cs@gmail.com" #your email
email_sender_username = "1bi19cs"  #your email username
email_sender_password = "cnsproj123"#your email password
email_smtp_server = "smtp.gmail.com" #change if not gmail.
email_smtp_port = 587 #change if needed.
email_recepients = ["sridevisriman04@gmail.com"] #your receipts
def SendEmail (confirmed_cases,recovered_cases,deaths,time):
    email_subject = f"Reporting COVID-19 Cases at {time}"
    email_body = '<html><head></head><body>'
    email_body += '<style type="text/css"></style>'
    email_body += f'<h2>Reporting COVID-19 Cases at {time}</h2>'
    #confirmed cases
    email_body += f'<h1 style="color: rgb(86, 0, 251);">'
    email_body += f'<b>Confirmed cases</b>: '
    email_body += f'{confirmed_cases}</h1>'
    #recovered cases
    email_body += f'<h1 style="color: rgb(9, 179, 23);">'
    email_body += f'<b>Recovered cases</b>: '
    email_body += f'{recovered_cases}</h1>'
    #deaths
    email_body += f'<h1 style="color: rgb(212, 44, 44);">'
    email_body += f'Deaths </b>: '
    email_body += f'{deaths}</h1>'
    #footer
    email_body += '<br>Reported By'
    email_body += '<br>COVID-19 BOT</body></html>'
    server = smtplib.SMTP(email_smtp_server,email_smtp_port)
    print(f"Logging in to {email_sender_account}")
    # To inform the email server that the client wants to upgrade from an insecure connection to a secure one using TLS
    server.starttls()
    server.login(email_sender_username, email_sender_password)
    for recipient in email_recepients:
        print(f"Sending email to {recipient}")
        message = MIMEMultipart('alternative')
        message['From'] = email_sender_account
        message['To'] = recipient
        message['Subject'] = email_subject
        message.attach(MIMEText(email_body, 'html'))
        server.sendmail(email_sender_account,recipient,message.as_string())
    server.quit()
url = "https://www.worldometers.info/coronavirus/"
req = requests.get(url)
bsObj = BeautifulSoup(req.text, "html.parser")
data = bsObj.find_all("div",class_ = "maincounter-number")
NumTotalCase = data[0].text.strip().replace(',', '')
NumDeaths = data[1].text.strip().replace(',', '')
NumRecovered = data[2].text.strip().replace(',', '')
TimeNow = datetime.datetime.now()
SendEmail(NumTotalCase,NumRecovered,NumDeaths,TimeNow)
print(f"End")