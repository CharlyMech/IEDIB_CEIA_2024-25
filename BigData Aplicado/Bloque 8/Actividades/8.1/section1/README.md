# Creación del recurso y clúster

En esta primera parte de la tarea explicaré el proceso necesario para la creación del recurso a utilizar en toda la tarea. La única diferencia será la carga de los datos ya que eso será exclusivo de cada una de los apartados. Esta parte es exactamente igual que en los apuntes.

El primer paso es irse al marketplace de Azure, buscar '_databricks_', seleccionar el primero, rellenar la información y esperar a que el recurso sea lanzado correctamente (_deployed_).

![Create resource 1](./screenshots/00%20create%20resource.png)

![Create resource 2](./screenshots/01%20create%20resource.png)

![Create resource 3 - deployed](./screenshots/02%20create%20resource%20-%20deployed.png)

![Resource panel](./screenshots/03%20resource.png)

Una vez finalizado este proceso, si se hace click en '_Go to resource_' aparecerá el panel de la última imagen. Desde éste se podrá abrir el espacio de trabajo (_workspace_) de databricks y ver si siguiente panel:

![Databricks workspace](./screenshots/04%20azure%20databricks%20workspace.png)

El siguiente paso es crear un clúster de Spark. Como se indica en los apuntes, dado que tenemos recursos limitados, este clúster únicamente dispondrá de un nodo. En la parte superior izquierda, se hace click en '_+ New_', se selecciona '_Cluster_' y se siguen los pasos (los mismos que en los apuntes).

![Create cluster 1](./screenshots/05%20create%20cluster.png)

![Create cluster 2](./screenshots/06%20create%20cluster.png)

![Create cluster 3](./screenshots/07%20create%20cluster%20-%20compute%20created.png)

Con el recurso ya creado por completo, lo que resta es añadir los datos necesarios para este apartado.

# Adición de los datos

El proceso descrito a continuación será replicado para el resto de apartados

![Add data](./screenshots/08%20add%20data.png)

![Add data goaslcorers](./screenshots/09%20add%20data%20-%20goalscorers.png)

![Add data results](./screenshots/10%20add%20data%20-%20results.png)

![Data added](./screenshots/11%20add%20data%20-%20data%20added.png)

Cuando los datos han sido añadidos, aparecerán bajo el _hive_metastore_.

# Creación del cuaderno y consultas a los datos.

Una vez los datos han sido cargados correctamente, se puede crear un nuevo cuaderno desde la parte superior izquierda (_+ New_) y esta vez seleccionamos '_Notebook_'.

### Carga de los datos en el cuaderno

El primer paso es instanciar los _data frames_, al igual que se ha realizado en repetidas ocasiones durante el curso con Python y la librería _pandas_, pero esta vez mediante Spark.

![Data added](./screenshots/12%20databrick%20notebook%20and%20data%20load.png)

En mi caso he decidido optar por usar la sintaxis SQL por ser más familiar para mi.

![Data added](./screenshots/13.png)

![Data added](./screenshots/14.png)

![Data added](./screenshots/15.png)

![Data added](./screenshots/16.png)

![Data added](./screenshots/17.png)

![Data added](./screenshots/18.png)
