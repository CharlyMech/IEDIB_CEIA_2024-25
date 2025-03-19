### Queremos guardar los mensajes de Bluesky a partir de una (o más) palabra de búsqueda (la que quieras, pero mejor una de la que se generen mensajes a menudo) en una base de datos MySQL para poder procesarlo posteriormente.

### Tienes que configurar un conector source (en modo distribuido) para leer mensajes de Bluesky según tu búsqueda y guardarlos como eventos en un tópico de Kafka.

### A continuación, utilizando el conector de JDBC sink (en modo distribuido), debes guardar los eventos en una tabla de MySQL. La tabla debe tener todos los datos del evento del objeto payload, excepto el campo langs. Son estos:

-  ### uri
-  ### cid
-  ### text
-  ### createdAt
-  ### handle
-  ### displayName
-  ### avatar

---

A este punto de la actividad, supondré que todo lo realizado durante los ejercicios y ejemplos de los apuntes ha sido realizado e iré directamente a la explicación de la configuración para esta actividad. Supondremos que todos los servicios necesarios (Zookeeper, el broker de Kafka y el worker) también han sido lanzados correctamente.

El primer paso es configurar el archivo _source_ para Bluesky:

![Archivo de configuración source para Bluesky](./screenshots/0%20bluesky%20source.png)

Después de haber creado el archivo de configuración correctamente con el nuevo tópico, se ejecutan los siguientes comandos (al igual que en el apartado anterior) para hacer un POST del conector _source_ y comprobar que consume satisfactoriamente los datos:

```bash
# Terminal 1 (izquierda)
curl -X POST -H "Content-Type: application/json" --data @config/bluesky-source.json http://localhost:8083/connectors

# Terminal 2 (derecha)
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bluesky_ai --from-beginning
```

![Archivo de configuración source para Bluesky](./screenshots/1%20post%20source%20and%20check%20data.png)

Se puede ver la estructura de un post de Blueskye consumido en el archivo [topic_object.json](./topic_object.json). Nos interesa únicamente el contenido dentro de `payload`.

Como se delantaba en el enunciado, habrá que realizar transformaciones ya que hay estructuras de datos que no son soportadas por MySQL. Para ello he eliminado el topic y he parado el worker.

```bash
curl -X DELETE http://localhost:8083/connectors/bluesky-AI
```

El nuevo archivo _source_ se ve de la siguiente forma:

![Nuevo archivo source para Bluesky](./screenshots/2%20transformed%20source%20file.png)

Se vuelve a lanzar el worker, hacer POST del _source_ y lanzar el consumidor de kafka como hemos hecho anteriormente. Para generar una nueva entrada o evento, creamos un post en Bluesky con la palabra clave y tras unos segundos debería aparecer la nueva entrada ya formateada ([topic_ouput_transformed.json](./topic_ouput_transformed.json)):

![Crear un nuevo post con la palabra clave](./screenshots/3%20new%20post%20with%20words.png)

![Nueva consumición del tópico con los datos formateados](./screenshots/4%20consumed%20and%20transformed.png)

Una vez comprobado que funciona correctamente, podemos configurar el _sink_ para MySQL.
