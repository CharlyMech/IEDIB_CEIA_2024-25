# Siguiendo las instrucciones que hemos visto en el apartado 6 de los apuntes, crea un cluster sobre Docker con 1 nodo maestro, 3 nodos worker y un nodo para JupyterLab. Puedes utilizar las mismas imágenes que hemos utilizado en los apuntes. El worker 3 debe exponer el puerto `8083` para su interfaz web.

Durante este apartado consideraré que las imágenes descargadas en el [punto 6.2](https://iedib.net/avirtual/mod/book/view.php?id=62479&chapterid=73711) de los apuntes, donde se muestra el proceso de configuración del clúster están descargadas tal y como se indica (en el directorio `/home/spark/cluster` en mi caso) además de haberse ejecutado el archivo `build.sh`.

![Files required](./screenshots/0%20files.png)

El archivo `docker-compose.yml` corresponde al usado durante los apuntes para realizar la simulación de clústers con 1 _master_ y 2 _slaves_. Modificaremos este archivo añadiendo otra instancia de la imagen `spark-worker` y asignándole el puerto indicado en el enunciado ([archivo resultante](./docker-compose.yml)).

![Modified docker compose file](./screenshots/1%20new%20docker%20compose%20file.png)

Dentro del directorio donde se encuentra el archivo de Docker Compose se ejecuta el siguiente comando para arrancar los contenedores:

```bash
sudo docker-compose up
```

En otra terminal se ejecuta el siguiente comando para ver los contenedores activos:

```bash
sudo docker container ls
```

![Running containers](./screenshots/2%20running%20containers.png)

Como se puede ver en la imagen, actualmente se encuentran 3 _slaves_, 1 _master_ y el contenedor para ejecutar Jupyter activos y se puede acceder todas las interfaces que se han descrito en los apuntes (captura de pantalla para el _worker 3_ para demostrar que funciona correctamente):

![Worker 3 web interface at port 8083](./screenshots/3%20worker%203.png)
