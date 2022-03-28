#This script generates the HMAC signature based on the sample payload
#Details: https://developers.mailerlite.com/docs/webhooks

import hmac
import base64

apikey="<mailerlite api key>" 

f = open("./sample-mailerlite-payload.json")
lines = f.read()
print(lines)
sig = hmac.new(apikey.encode(), lines.encode(), 'sha256')
print(base64.b64encode(sig.digest()))