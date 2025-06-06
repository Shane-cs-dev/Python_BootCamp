import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
CONTENT_SID = os.getenv("CONTENT_SID")
class WhatsappNotification:
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_whatsapp(self, context):
        try:
            message = self.client.messages.create(
            from_= "whatsapp:+14155238886",
            body = context,
            to='whatsapp:+886965315213'
            )
            print(f"Message sent successfully!")
        except  Exception as e:
            print(f"Error sending Whatsapp message: {e}")

