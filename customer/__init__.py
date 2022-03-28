import logging
import os
import json
import hmac
import base64
import shopify
import azure.functions as func

shop_url = os.environ["shopurl"]
session = shopify.Session(shop_url, os.environ["apiversion"], os.environ["shopifysecret"])

def main(req: func.HttpRequest) -> func.HttpResponse:
    if 'X-MailerLite-Signature' in req.headers:
        signature = req.headers['X-MailerLite-Signature']
    else:
        return func.HttpResponse("Missing X-MailerLite-Signature header.", status_code=401)

    payload = json.loads(req.get_body())
    logging.info(payload)
    
    verisig = base64.b64encode(hmac.new(os.environ["mailerliteapikey"].encode(), bytes(req.get_body()), 'sha256').digest())

    if signature != verisig.decode():
        return func.HttpResponse("Request cannot be authenticated.", status_code=401)

    logging.info("Signature verified")
    shopify.ShopifyResource.activate_session(session)

    customer = shopify.Customer()

    try:
        events = payload['events']
        for event in events:
            subscriber = event['data']['subscriber']
            customer.first_name = subscriber['name']
            customer.last_name = subscriber['fields'][2]['value']
            customer.email = subscriber['email']
            customer.accepts_marketing = True
            customer.verified_email = True
            response = customer.save()
            logging.info("Success: " + str(response))
    except:
        return func.HttpResponse("Bad or malformed request.", status_code=400)

    shopify.ShopifyResource.clear_session()

    return func.HttpResponse("Customer created successfully.", status_code=200)