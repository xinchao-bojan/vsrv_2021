import random
from time import sleep
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email():
    server = 'smtp.mail.ru'
    user = 'bojan.alarm@mail.ru'
    password = 'НЕ СКАЖУ'

    recipients = ['sk.schooldude@gmail.com']
    sender = 'bojan.alarm@mail.ru'
    subject = 'СИГНАЛИЗАЦИЯ'
    text = f'У вас обнаружена подозрительная активность в {datetime.now()}'
    html = '<html><head></head><body><p>' + text + '</p></body></html>'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = ' safe inside <' + sender + '>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'SAFE INSIDE'

    part_text = MIMEText(text, 'plain')
    part_html = MIMEText(html, 'html')

    msg.attach(part_text)
    msg.attach(part_html)

    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()


def sender(alarm_list):
    random.shuffle(alarm_list)
    choice = random.choice(alarm_list)
    if choice:
        try:
            send_email()
            print(f'email sended at {datetime.now()}')
        except Exception as e:
            print(e)
            print(f'error while sending email at {datetime.now()}')
    else:
        print('now everything is ok')
    return alarm_list


if __name__ == '__main__':
    alarm_list = [0] * 900
    alarm_list += ([1] * 100)
    while True:
        alarm_list = sender(alarm_list)
        sleep(60)
