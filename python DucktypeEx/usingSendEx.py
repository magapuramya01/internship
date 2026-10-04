class EmailNotification:
    def send(self):
        print("Email sent")


class SMSNotification:
    def send(self):
        print("SMS sent")


def notify(obj):
    obj.send()


notify(EmailNotification())
notify(SMSNotification())