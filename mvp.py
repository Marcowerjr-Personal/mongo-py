# Librería
from pymongo import MongoClient
try:
    # Datos de acceso de usuario al servidor
    user = 'mvp'
    password = 'mvp'

    # Construyendo el objeto conexión con Mongo
    client = MongoClient(f'mongodb://{user}:{password}@localhost:27017/')

    database = client.videogames
    node_collection = database.data

    data = {
        'game': 'Mario',
        'price': '$50',
    }

    node_collection.insert_one(data)
    
    result_set = node_collection.find()
    print('Juego   |    Precio')
    for n in result_set:
        print(n['game'], n['price'])
    
    
except Exception as e:
    
    print(f'Error: {format(e)}')
