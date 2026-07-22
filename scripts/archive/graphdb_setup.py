from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://localhost:7200/repositories/ifrs-gics")
sparql.setQuery("SELECT * WHERE { ?s ?p ?o } LIMIT 1")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print("Connected!")