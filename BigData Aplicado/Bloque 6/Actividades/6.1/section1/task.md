### Tenemos un archivo CSV donde simularemos que un sensor va escribiendo lecturas de diversas variables ambientales, separadas por comas (,), con el siguiente formato:

-  ### fecha: cadena de texto con la fecha de la lectura, en formato dd/mm/yyyy. Por ejemplo: 23/02/2025

-  ### hora: cadena de texto con la hora de la lectura, en forma hh:mm:ss. Por ejemplo: 16:07:30

-  ### temperatura: número real (floato), expresada en grados centígrados. Por ejemplo: 17.7

-  ### humedad: número real (floato), expresada en porcentaje. Por ejemplo: 75.1

-  ### presión: número real (entero), expresada en milibares. Por ejemplo: 1012

### Tienes que configurar un conector source (en modo distribuido) para leer estos datos y guardarlos en un tópico de Kafka.

### A continuación, utilizando Python y la librería hdfs, debes ir volcando los eventos a un archivo en HDFS de tu clúster Hadoop. Si lo prefieres, puede utilizar una configuración con sólo un único nodo.

### El formato del archivo será el siguiente, con los valores separado por puntos y comas (;):

-  ### datahora: número entero, con la fecha y hora en formato timestamp de Unix.

-  ### temperatura

-  ### presión

-  ### humedad

### Para probarlo, simula las lecturas del sensor mediante echo, como hemos hecho en los apuntes. Por ejemplo:

```bash
echo "23/02/2025,16:07:30,17.7,75.1,1012" >> archivo.csv
```

---

<h3 style="color: black; background-color: red">NOTA</h3>

Durante la tutoría de día 18/03/2025 hemos podido comprobar que efectivamente con los pasos que voy a describir a continuación, la funcionalidad se realiza exitosamente. En algunos de los logs del mismo día se podrá ver.

He probado mediante la creación de nuevos tópicos, reiniciando servicios y máquinas virtuales pero nada ha funcionado.

Todo lo que es la parte de configuración y preparación del ejercicio podré proporcionar capturas de pantalla y datos verificados, pero habrá un punto en el que no podrá ser el caso ya que no he conseguido hacerlo funcionar correctamente. Principalmente me preocupa el script de Python (leer los comentarios explicativos dentro del código).

Cabe la posibilidad que haya algo que no estoy ejecutando correctamente y por eso falle. Quedo a la espera de corrección.

---

El primer paso que tenemos que realizar antes de empezar a crear los nuevos tópicos, consumidores y productores, es lanzar tanto ZooKeeper como el propio servicio de Kafka. Para ello ejecutamos los siguientes comandos en dos terminales diferentes:

```bash
# Lanzar ZooKeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Lanzar el servicio de Kafka
bin/kafka-server-start.sh config/server.properties
```

<b style="color: red">NOTA:</b> es importante que para todos los comandos que van a ser explicados se esté posicionado en el path donde se ha extraído Kafka. Por ejemplo en mi caso es `/home/carlos/Downloads/kafka_2.13-3.8.1`

El siguiente paso consistirá en crear un nuevo tópico mediante el siguiente comando:

```bash
bin/kafka-topics.sh --create --topic [topic_name] --bootstrap-server localhost:9092
```

En mi caso lo llamo `section_1`. Para comprobar que se ha creado correctamente se puede ejecutar el siguiente comando que lista los tópicos creados:

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
```

![Listado de tópicos](screenshots/0%20new%20topic.png)

El siguiente paso sería configurar el conector, en este caso el de tipo _source_ para consumir los datos desde un archivo. Como vamos a usar el modo distribuido, usaremos el archivo JSON.

```bash
nano config/connect-file-source.json
```

![Connector source para archivos JSON](screenshots/1%20connect%20file%20source.png)

Tras este paso se puede lanzar el worker (que actuará como una API REST) mediante el comando:

```bash
# Lanzar el worker
bin/connect-distributed.sh config/connect-distributed.properties
```

En otra terminal podemos ejecutar las requests a dicha API para hacer un POST del archivo de configuración _source_ y comprobar que efectivamente ha sido exitoso.

```bash
# Postear el conector para el archivo local
curl -X POST -H "Content-Type: application/json" --data @config/connect-file-source.json http://localhost:8083/connectors

# Ver todos los conectores posteados en el worker
curl http://localhost:8083/connectors
```

![Connector source para archivos JSON](screenshots/2%20post%20connector.png)

A este punto se podría decir que la parte de configuración está finalizada, por lo que es momento de crear el script consumidor del tópico en Python: [script consumidor](./section1_hdfs_consumer.py).

Es importante que antes de empezar a ejecutar todo, se cree el archivo en Hadoop tal y como se explica en los apuntes (recordad importante los permisos del directorio).

Para lanzar el script consumidor sencillamente abrimos otra terminal y ejecutamos el siguiente comando (substituyendo `file_name` por el nombre del archivo creado):

```bash
python3 [file_name].py
```

Otra forma de ver los eventos en el tópico será mediante este comando en otra terminal

```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic section_1 --from-beginning
```

Para generar un nuevo evento (una escritura en el archivo) ejecutamos el siguiente comando (adaptado del proporcionado en el enunciado):

```bash
echo "23/02/2025,16:07:30,17.7,75.1,1012" >> section1.csv
```

Desde la terminal donde se ha ejecutado el consumidor en Python se podrán ver (en caso de usar `print` en el código) los datos que se consumen.

Para comprobar el resultado, desde la máquina de hadoopmaster se puede ejecutar el siguiente comando para ver el contenido del archivo (sustituir `path/to/hdfs/file.csv` por el directorio completo, ejemplo debajo).

```bash
hdfs dfs -cat path/to/hdfs/file.csv

# En mi caso:
hdfs dfs -cat /user/hadoop/kafka/section1.csv
```
