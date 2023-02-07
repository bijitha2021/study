import threading
lock =threading.Lock()

class Email_sender:
    __instance = None
    def __new__(cls,*args,**kwargs):
        if  cls.__instance == None:
            print("creating")
            cls.__instance= object.__new__(cls)
        return cls.__instance

    @staticmethod
    def get_instance():
        if Email_sender.__instance == None:
            Email_sender.__instance = Email_sender()
        return Email_sender.__instance

    def estabisgh_connection(self, st):
        lock.acquire()
        for i in range(10):
            print("estabishing connection for ", st+str(i))
        lock.release()


    def send_mail(self,from_adr,to_adr,subject,matter):
        self.estabisgh_connection(from_adr)
        for i in range(20):
            print("mail sent to {} from {} with subject{} an matter {}".format(str(i) + from_adr,to_adr,subject,matter))

        return True


