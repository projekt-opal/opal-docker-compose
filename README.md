# opal-ckan-docker
CKAN customized for OPAL project.

## How to use

1. Create .env file in the repo root with the following contents:
```
$ cat .env
CKAN_RECAPTCHA_PUBLICKEY=6Le...AIB
CKAN_RECAPTCHA_PRIVATEKEY=6Le...Gli
```

You can get a recaptcha key at https://www.google.com/recaptcha - make sure to select recaptcha v2 / "invisible" as an option. No need to specify a host if you run it at localhost.

2. Make sure that the ckan-storage directory has write permissions by all users. This can be enforced with:
```
$ chmod 777 ckan-storage
```

3. Start-up CKAN
```
docker-compose up -d
```

4. Create admin user
Run ```create-admin-user.sh`, which invokes the following command:
```
docker exec -it $(docker ps | grep ckan:2.8.1-opal | cut -d' ' -f 1) ckan-paster --plugin=ckan sysadmin add admin email=admin@example.com -c /etc/ckan/production.ini
```
