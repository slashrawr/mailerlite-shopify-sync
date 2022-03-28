# mailerlite-shopify-sync

Mailerlite does not currently support bi-directional syncing between itself and shopify. This is problematic when you want to use discounts in Shopify for subscription groups.

This Azure function solves that problem by providing an endpoint for a Mailerlite webhook that will create the customer in Shopify when the subscriber is created in Mailerlite.

# TODO

- Terraform templates for provisioning
- More (and better) error handling
- More (and better) tests
- More customisation maybe?
- AWS Lambda maybe?

# More Info

- https://developers.mailerlite.com/docs/webhooks
- https://shopify.dev/api
