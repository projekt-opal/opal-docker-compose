from subprocess import call
import time


for i in range(1,177):
	print "docker-compose exec ckan sh -c 'ckan-paster --plugin=ckanext-harvest harvester source model{} http://172.17.0.1:8000/model{}.ttl dcat_rdf model{}_importer TRUE diceupb MANUAL -c /etc/ckan/production.ini'".format(i+1, i+1, i+1)
	call("docker-compose exec ckan sh -c 'ckan-paster --plugin=ckanext-harvest harvester source model{} http://172.17.0.1:8000/model{}.ttl dcat_rdf model{}_importer TRUE diceupb MANUAL -c /etc/ckan/production.ini'".format(i+1, i+1, i+1), shell=True)
	print "docker-compose exec ckan sh -c 'ckan-paster --plugin=ckanext-harvest harvester job model{} -c /etc/ckan/production.ini'".format(i+1)
	call("docker-compose exec ckan sh -c 'ckan-paster --plugin=ckanext-harvest harvester job model{} -c /etc/ckan/production.ini'".format(i+1), shell=True)
	time.sleep(200) 


