# opal-ckan-docker
CKAN customized for OPAL project.

## How to use

1. Create .env file in the repo root with the following contents:
```
$ cat .env
CKAN_RECAPTCHA_PUBLICKEY=6Le...AIB
CKAN_RECAPTCHA_PRIVATEKEY=6Le...Gli
CRAWLER_TRIPLESTORE_USERNAME=...
CRAWLER_TRIPLESTORE_PASSWORD=...
CRAWLER_TRIPLESTORE_URL=...
```

You can get a recaptcha key at https://www.google.com/recaptcha - make sure to select recaptcha v2 / "invisible" as an option. No need to specify a host if you run it at localhost.

all variables are listed in env_sample file (You must set appropriate values for them).

2. Make sure that the ckan-storage directory has write permissions by all users. This can be enforced with:
```
$ chmod 777 ckan-storage
```

3. Start-up
```
docker-compose up -d
```

4. Create ckan admin user, initializing harvesting DB, and setting up Mesasge brokers by running afterRun.sh (Run them one by one (or run the file) after bringing up all services in previous step)
