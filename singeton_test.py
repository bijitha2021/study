import time

from singleton_pattern import Email_sender
import threading

lst_threads = []
for t in range(100):
    email_sender = Email_sender()
    test = threading.Thread(target = email_sender.send_mail, args = ("bijitha@gmai.com"+ str(t),'subin@gmai.com','test_sub','matter'))
    lst_threads.append(test)
    test.start()



