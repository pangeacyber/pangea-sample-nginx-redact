# Nginx - Redact sample app

This app shows an exmaple of what an integration between nginx and pangea's
redact service would look like.

## Overview

In this sample, we have a flask app that randomly generates both valid and
invalid SSNs & email addresses. In front of this app we have nginx with our
lua code block in its configuration that will be calling out pangea's redact
service to scrub the response of PII before returning it to the caller.

The redact service can be used for real time communications as well as data
intensive usecases.

Configuration of a caching mechanism for these requests is not possible in this
app as the flask app generates random data every request.

![setup](public/nginx-redact-setup.png)

### Flow

![flow](public/nginx-redact-flow.png)

## Usage

1. Go to [pangea.cloud](https://pangea.cloud) and sign up
1. Create an org, a project, and enable the redact service
1. Go to the [redact configuration settings page](https://console.pangea.cloud/service/redact/rulesets) and enable the `US_SSN` rule under `Us Identification Numbers` section.
1. Go to the [tokens page](https://console.pangea.cloud/project/tokens) and copy your redact token.
1. Set `PANGEA_REDACT_TOKEN` env variable to your copied token
1. Clone this repo: `git clone github.com/MichaelCombs28/nginx_redact_integration_sample.git`
1. Run `docker-compose up` in the cloned root folder

For more details regarding configuration and usage of redact, check out the [docs](https://pangea.cloud/docs/redact/).

### Fake unredacted PII generated by faker

```
curl localhost:8000
```

### Response with redacted data

```
curl localhost:8080
```

### Cleaning Up

```
docker-compose down --rmi all
```

## FAQs

#### I'm seeing an Internal Error

This means that either you don't have `PANGEA_REDACT_TOKEN` set or your token is invalid.
