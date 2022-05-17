from twilio.rest import Client

from api.creds import TWILIO_API_KEY, TWILIO_SID

# TODO: look-up vercel command to hide tokens and sid

client = Client(TWILIO_SID, TWILIO_API_KEY)

message = client.messages.create(
    to="+18058618738", 
    from_="+19207969278",
    body= get_body())


def get-body():
  temp_SMS:[]
    if temp_SMS in method:
	temp_sms.append(method_response)
    else: 
  temp_sms.append(method_wrong)


print(message.sid)