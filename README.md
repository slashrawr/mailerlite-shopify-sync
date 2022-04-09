# mailerlite-shopify-sync

Mailerlite does not currently support bi-directional syncing between itself and shopify. Signups through a Mailerlite form are not created in Shopify. This means it's not possible to offer subscriber only discounts for example.

This Azure function solves that problem by providing an endpoint for a Mailerlite webhook that will create the customer in Shopify when the subscriber is created in Mailerlite.

# How to Use

> **_NOTE:_**  You will need to add a custom app to Shopify to obtain key and secret.

1. Configure environment variables (details of variables are below)
2. Deploy function
3. Configure Mailertlite webhook with function endpoint URL

# Configuration

The following environment variables need to be configured:
<table>
    <tr>
      <td><b>Variable</b></td>
      <td><b>Description</b></td>
    </tr>
    <tr>
        <td>apiversion</td>
        <td>Shopify API version - https://shopify.dev/api/usage/versioning</td>
    </tr>
    <tr>
        <td>mailerliteapikey</td>
        <td>Mailerlite API key - https://developers.mailerlite.com/docs/authentication</td>
    </tr>
    <tr>
        <td>shopifykey</td>
        <td>Shopify key - https://shopify.dev/apps/auth/admin-app-access-tokens</td>
    </tr>
    <tr>
        <td>shopifysecret</td>
        <td>Shopify secret - https://shopify.dev/apps/auth/admin-app-access-tokens</td>
    </tr>
    <tr>
        <td>shopurl</td>
        <td>URL of your Shopify store.</td>
    </tr>
</table>


# TODO

- [ ] Update "apiversion" to "shopifyapiversion" for consistency
- [ ] Terraform templates for provisioning
- [ ] More (and better) error handling
- [ ] More (and better) tests
- [ ] More customisation maybe?
- [ ] AWS Lambda maybe?

# More Info

- https://developers.mailerlite.com/docs/webhooks
- https://shopify.dev/api
