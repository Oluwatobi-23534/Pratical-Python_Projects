from twilio.rest import TwilioRestClient

account_sid = "AC445a30cfc5ce87fbca50f2da4dfccda4"
auth_token = "a9737ae88911de538527bd6289126901"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body = "Python 3 says hi from Twilio app!",
    to = "+2349162837696",
    from_= "+16206469267")

print(message.sid)
