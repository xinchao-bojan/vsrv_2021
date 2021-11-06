import random
from time import sleep
from datetime import datetime
import requests
import threading


def sender(room):
    r = requests.post('http://127.0.0.1:8000/api/motion/create/', data={'room': room, 'motion': random.randrange(20, 1300)})
    print(r.status_code)


if __name__ == '__main__':
    rooms = [
        'Прихожая',
        'Кухня',
        'Гостиная',
        'Спальня',
        'Детская',
    ]
    while True:
        # for room in rooms:
        t1 = threading.Thread(target=sender, args=['Прихожая'])
        t2 = threading.Thread(target=sender, args=['Кухня'])
        t3 = threading.Thread(target=sender, args=['Гостиная'])
        t4 = threading.Thread(target=sender, args=['Спальня'])
        t5 = threading.Thread(target=sender, args=['Детская'])

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        # t.join()
        # sender(rooms)
        sleep(60)
