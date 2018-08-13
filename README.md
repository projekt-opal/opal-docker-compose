# opal-ckan-docker
CKAN customized for OPAL project.

## How to use

1. Create .env file in the repo root with the following contents:
```
$ cat .env
CKAN_RECAPTCHA_PUBLICKEY=6Le...AIB
CKAN_RECAPTCHA_PRIVATEKEY=6Le...Gli
```

2. Start-up CKAN
```
docker-compose up -d
```
