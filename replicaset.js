// Crear una red para el Replica Set

docker network create mongo-rs

// Checar redes activas
docker network ls

// Crear tres contenedores para los nodos del Replica Set con distintos nombres, especificando
// que se conecten a la red que acabamos de crear

docker run --name mongo-nodo1 -d --net mongo-rs mongo --replSet "rs0" 
docker run --name mongo-nodo2 -d --net mongo-rs mongo --replSet "rs0"
docker run --name mongo-nodo3 -d --net mongo-rs mongo --replSet "rs0"

// Checar que los 3 contenedores esten ejecutandose
docker ps

// Conectarse a uno de los nodos
docker exec -it mongo-nodo1 mongo
// Dentro de mongo, checar status
rs.status()

// Inicializar el Replica Set 

config = {
      "_id" : "rs0",
      "members" : [
          {
              "_id" : 0,
              "host" : "mongo-nodo1:27017"
          },
          {
              "_id" : 1,
              "host" : "mongo-nodo2:27017"
          },
          {
              "_id" : 2,
              "host" : "mongo-nodo3:27017"
          }
      ]
  }

//Inicializar con la variable de config
rs.initiate(config)


//CREAR USUARIO Y PWD
db.createUser({user:'admin',pwd:'admin',roles:[]})



// Comprobar el status del Replica Set, en que nodo estoy? Status

rs.status()
// Quien es el primario?
rs.isMaster()

// En otra terminal solo para checar que sea secundario
docker exec -it mongo-nodo3 mongo

// Obtener la configuración

rs.conf()

// Habilitar un secundario para lectura
use db1
rs.slaveOk()
