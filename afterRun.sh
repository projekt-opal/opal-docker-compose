docker-compose exec ckan sh -c 'ckan-paster --plugin=ckan sysadmin add admin email=admin@example.com -c /etc/ckan/production.ini'
docker-compose exec ckan sh -c 'ckan-paster --plugin=ckanext-harvest harvester initdb --config=/etc/ckan/production.ini'
docker-compose exec -d ckan sh -c 'ckan-paster --plugin=ckanext-harvest harvester fetch_consumer --config=/etc/ckan/production.ini'
docker-compose exec -d ckan sh -c 'ckan-paster --plugin=ckanext-harvest harvester gather_consumer --config=/etc/ckan/production.ini'
