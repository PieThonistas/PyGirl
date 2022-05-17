from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC19c0d741b2194a37606facfd6009c227"
# Your Auth Token from twilio.com/console
auth_token  = "1b665411b368208fda630db1c96824b8"

# TODO: look-up vercel command to hide tokens and sid

client = Client(account_sid, auth_token)

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