# HubSpot PHP Sample Search Results Iterating App

Currently, this app focuses on demonstrating the functionality of
[Search the CRM API](https://developers.hubspot.com/docs/api/crm/search) endpoints
and related actions.

Please see the documentation on [Creating an app in HubSpot](https://developers.hubspot.com/docs-beta/creating-an-app)

## HubSpot Public API links used in this application

- [Search contacts](https://developers.hubspot.com/docs/crm/search)

## Note on Application Scopes

HubSpot provides a way to restrict application users access to the system to certain scopes.
In order to do that it is a good practice to make a set of scopes required by your application.
Please refer to [Initiate an Integration with OAuth 2.0](https://developers.hubspot.com/docs/methods/oauth2/initiate-oauth-integration) for documentation on the scope parameter passed to https://app.hubspot.com/oauth/authorize to make a set of scopes required.
[Scopes](https://developers.hubspot.com/docs/methods/oauth2/initiate-oauth-integration#scopes) explains how to make
optional scopes and talks about scopes available in HubSpot system.

## Setup App

Make sure you have [Docker Compose](https://docs.docker.com/compose/) installed.

## Configure

1. Copy .env.template to .env
2. Paste your HUBSPOT_CLIENT_ID and HUBSPOT_CLIENT_SECRET

### Running

The best way to run this project (with the least configuration), is using docker compose.  Change to the webroot and start it

```bash
docker-compose up -d --build
```

You should now be able to navigate to [http://localhost:8999](http://localhost:8999) and use the application.
Firstly you will need to authorize via OAuth there.
Than you can to go to the terminal window and start the following command in the application root

```bash
docker-compose exec web php /app/src/console/example.php
```
