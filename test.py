from elasticsearch_dsl import connections

connections.create_connection(hosts=['localhost'], timeout=20)
print(connections.get_connection().cluster.health())
