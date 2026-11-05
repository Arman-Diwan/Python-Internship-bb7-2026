class Notification:
    def send(self):
        print("Sending a notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")


notifications = [
    Notification(),
    EmailNotification(),
    SMSNotification()
]

for notification in notifications:
    notification.send()