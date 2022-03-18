# Librería
from pymongo import MongoClient
try:
    # Datos de acceso de usuario al servidor
    user = 'root'
    password = 'root'

    # Construyendo el objeto conexión con Mongo
    client = MongoClient(f'mongodb://{user}:{password}@localhost:27017/')

    database = client.blockchain
    node_collection = database.data

    data = {
        'key': 1211,
        'name': 'Sensor de movimiento',
        'value': 12
    }

    node_collection.insert_one(data)
    
    result_set = node_collection.find()
    print('Clave  |  Nombre  |  Valor')
    for n in result_set:
        print(n['key'], n['name'], n['value'])
    
    
except Exception as e:
    
    print(f'Error: {format(e)}')
