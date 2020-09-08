from twilio.rest import client

account_sid = ''
auth_token = ''
client = client(account_sid, auth_token)

message = client.message.create(
                            from='+12266024690',
                            body='I cant believe this work',
                            to='+91000000000'
                        )

print(message.sid)                        