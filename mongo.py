from pymongo import MongoClient


try:
    client = MongoClient()
    db = client['python']
except Exception as e:
    print('Err {}'.format(e))
    exit()

print(db.usuario.find_one())

registro = {"_id":5 ,"nome":"felipe","linguagem":"javascript"}
db.usuario.insert(registro)

print(db.usuario.find_one({"_id":5}))