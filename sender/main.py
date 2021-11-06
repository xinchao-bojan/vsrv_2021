import random
from time import sleep
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests

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


def sender(rooms):
    for k, v in rooms.items():
        rooms[k] = random.randrange(20, 1300)
    r = requests.post('https://httpbin.org/post', data=rooms)

if __name__ == '__main__':
    rooms = {
        'Прихожая': 0,
        'Кухня': 0,
        'Гостиная': 0,
        'Спальня': 0,
        'Детская': 0,
    }
    while True:
        sender(rooms)
        sleep(60)
