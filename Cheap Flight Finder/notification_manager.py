import requests
from twilio.rest import Client

ACCT_SID = "ACbbc68878b3949d47fdb5f25470dcfe74"
AUTH_TOK = "4f4e1e7a84229977007de38160a73672"

TWILIO_NUMBER = '+19083328805'

class NotificationManager:

    def __init__(self):
        self.client = Client(ACCT_SID, AUTH_TOK)

    def send_sms(self, message):
        message = self.client.messages.create(
            body= message,
            from_= TWILIO_NUMBER,
            to='+18457219250'
        )
        print(message.sid)