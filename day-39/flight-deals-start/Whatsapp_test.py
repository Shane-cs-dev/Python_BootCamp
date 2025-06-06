import os
from dotenv import load_dotenv
from twilio.rest import Client
#API
load_dotenv()
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  content_sid='HX229f5a04fd0510ce1b071852155d3e75',
  content_variables='{"1":"4091739999"}',
  to='whatsapp:+886965315213'
)
# import os
# from twilio.rest import Client
#
# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# ACCOUNT_SID = os.getenv("ACCOUNT_SID")
# AUTH_TOKEN = os.getenv("AUTH_TOKEN")
# CONTENT_SID = os.getenv("CONTENT_SID")
# client = Client(ACCOUNT_SID, AUTH_TOKEN)
#
# message = client.messages.create(
#     body="Hello there!",
#     from_="whatsapp:+14155238886",
#     to="whatsapp:+15005550006",
# )

print(message.body)




