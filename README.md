# opal-ckan-docker
CKAN customized for OPAL project.

## How to use

1. Create necessary folders for CKAN volume
```
$ mkdir -p ckan-uploads/storage/uploads/group
```

2. Create .env file in the repo root with the following contents:
```
$ cat .env
CKAN_RECAPTCHA_PUBLICKEY=6Le...AIB
CKAN_RECAPTCHA_PRIVATEKEY=6Le...Gli
```

3. Start-up CKAN
```
docker-compose up -d
```

4. Create admin user
```
docker exec -it $(docker ps | grep ckan:2.8.1-opal | cut -d' ' -f 1) ckan-paster --plugin=ckan sysadmin add admin email=admin@example.com -c /etc/ckan/production.ini
```
