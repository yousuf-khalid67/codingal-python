from abc import ABC
class Notification(ABC):
    def send_message(self, receiver, message):
        pass
class Email_Notification(Notification):
    def send_message(self, receiver, message):
        print(f"sending email to {receiver}: {message}")

class Sms_Notification(Notification):
    def send_message(self, receiver, message):
        print(f"sending sms to {receiver}: {message}")

e1=Email_Notification()
e1.send_message("Bob", "hi")

sms1=Sms_Notification()
sms1.send_message("mimi", "are u hungry?")