import json
from pymongo import MongoClient

uri = 'mongodb://admin:admin@mongo-nodo1:27018'
#client = MongoClient('mongo-nodo1', 27017)
client = MongoClient(uri)
#client = MongoClient(port=27017)
#db = client.get_default_database()
db = client.db1



#mongoimport --db db1 --collection BiciComprador --file BiciComprador.json --jsonArray
#mongoimport --db db1 --collection Comprador --file Comprador.json --jsonArray
#mongoimport --db db1 --collection Bicicleta --file Bicicleta.json --jsonArray



print("Queries")


#Agrupar por Color y Ordenar Ascendentemente
db.BiciComprador.aggregate([

    {
        $group :{
          _id:"$Color",
          Total:{$sum:1}, 
        }
    },
    {
        $project:{
            _id:0,
            Colores:"$_id",
            Total:1
        }

    },
    {
        $sort:{
            _id:1
        }
    }
])

#Agrupar por Edad
db.Comprador.aggregate([

    {
        $group :{
          _id:"$Edad",
          Total:{$sum:1}, 
        }
    },
    {
        $project:{
            _id:0,
            Edades:"$_id",
            Total:1
        }

    },
    {
        $sort:{
            _id:1
        }
    }
])
#Agrupar por fecha de creacion
db.Bicicleta.aggregate([

    {
        $group :{
          _id:"$FechaCreacion",
          Total:{$sum:1}, 
        }
    },
    {
        $project:{
            _id:0,
            Fechas:"$_id",
            Total:1
        }

    },
    {
        $sort:{
            _id:1
        }
    }
])


#Agrupo por color Amarillo, muestrar su fecha de cración y cuantas se crearon ese día
db.Bicicleta.aggregate([

    { $match :{ "color":"Amarillo"}},
          {$group: { _id: "$FechaCreacion", total:{ $sum: "$color" }}},
          {$sort:{toral: -1 }}
])
