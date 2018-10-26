#!/bin/sh
docker exec -it $(docker ps | grep ckan:2.8.1-opal | cut -d' ' -f 1) ckan-paster --plugin=ckan sysadmin add admin email=admin@example.com -c /etc/ckan/production.ini
