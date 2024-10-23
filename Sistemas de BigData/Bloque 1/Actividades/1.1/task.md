# Tarea evaluable CE_5074 1.1

Antes de comenzar la tarea, se deben de ejecutar los siguientes comandos en caso de utilizar la terminal (habiendo instalado mongo shell previamente):

```bash
# Conectarse al servidor con tus credenciales
mongosh "mongodb+srv://USER:PASSWORD@block1cluster.fwadg.mongodb.net/"
# Seleccionar la base de datos con la que trabajar
use sample_mflix
# Se mostrará por consola:
switched to db sample_mflix
```

Los comandos que se mostrarán a continuación han sido ejecutados mediante terminal pero comprobados mediante la interfaz gráfica MongoDB Compass.

## 1. Recupera el número de películas del año (campo _year_ 1980).

```bash
db.movies.find({'year': 1980}).count()
# > 167
```

![1](img/1.png)

## 2. Recupera el número de películas que tienen como único país (campo _countries_) España.

```bash
db.movies.find({'countries': ['España']}).count()
# > 0
```

![2 1](img/2-1.png)

Si cambiamos 'España' por 'Spain' el resultado es diferente:

```bash
db.movies.find({'countries': ['Spain']}).count()
# > 266
```

![2 2](img/2-2.png)

## 3. Recupera el número de películas que no tienen póster (campo _poster_).

```bash
db.movies.find({'poster': {$exists: false}}).count()
# > 3305
```

![3](img/3.png)

## 4. Recupera un listado de todos los géneros (campo _genre_) posibles.

```bash
db.movies.distinct('genres')
```

![4](img/4.png)

## 5. Recupera el número de películas que contienen la palabra 'war' (sin distinguir mayúsculas y minúsculas) en el argumento (campo _plot_).

```bash
db.movies.find({'plot': {$regex: /\bwar\b/i}}).count()
# > 843
```

![5](img/5.png)

## 6. Recupera el número de películas cuyo título acabe en un número.

```bash
db.movies.find({'title': {$regex: /\b\d$\b/i}}).count()
# > 218
```

![6](img/6.png)

## 7. Recupera la película dirigida por Steven Spielberg que tiene la mejor valoración IMDB (campo _rating_ dentro de campo _imdb_). Tienes que mostrar el título de la película y su valoración.

```bash
db.movies.find({ 'directors': ['Steven Spielberg'] }, { 'title': 1, 'imdb.rating': 1 }).sort({ 'imdb.rating': -1 }).limit(1)
```

![7](img/7.png)

## 8. Recupera las películas en las que aparece Robert De Niro y Al Pacino juntos en el reparto (campo _cast_) ordenadas de más reciente a más antigua. Tienes que mostrar el título de la película y su año.

```bash
db.movies.find({ 'cast': { $all: ['Robert De Niro', 'Al Pacino'] }}, { 'title': 1, 'year': 1, '_id': 0}).sort({'year': -1})
```

![8](img/8.png)

## 9. Recupera las películas en las que actúa Tom Hanks, que tienen al menos una valoración de 8 y que han ganado más de 22 premios (campo _wins_ dentro de campo _awards_), ordenadas alfabéticamente por título. Tienes que mostrar el título de la película, la valoración IMDB y el número de premios.

```bash
db.movies.find({$and :[{'cast': {$all: ['Tom Hanks']}}, {'awards.wins': {$gt: 22}}]}, {'title': 1, 'imdb.rating': 1, 'awards.wins': 1, '_id': 0}).sort({'title': 1})
```

![9](img/9.png)

## 10. Añade una nueva película, de la cual tenemos la siguiente información, respetando la estructura de los documentos que tenemos en la colección:

### a. Título: 'Oppenheimer'

### b. Géneros: historia y biografía

### c. Director: Christopher Nolan

### d. Año: 2023

```bash
db.movies.insertOne( {'title': 'Oppenheimer', 'genres': ['History', 'Biography'], 'directors': ['Christopher Nolan'], 'year': 2023} )
# { acknowledged: true, insertedId: ObjectId(STRING_ID_AUTO)} -> Lo importante es el acknowledged a true
```

Captura de una query para encontrar la película en MongoDB Compass:

![10](img/10.png)

## 11. Modifica la película que has creado en el apartado anterior para poner que su país es Estados Unidos, que su duración es de 180 minutos y que su valoración de IMDB es de 8,3. Tienes que respetar la estructura de los documentos que tenemos en la colección.

```bash
db.movies.updateOne( {'title': 'Oppenheimer'}, {$set: {'countries': ['USA'], 'runtime': 180, 'imdb.rating': 8.3}} )
# { acknowledged: true, insertedId: null, matchedCount: 1, modifiedCount: 1, upsertedCount: 0}
```

Captura de una query para encontrar la película en MongoDB Compass:

![11](img/11.png)

## 12. Elimina la película que has creado y modificado en los dos últimos apartados.

```bash
db.movies.deleteOne( {'title': 'Oppenheimer'} )
# { acknowledged: true, deletedCount: 1 }
```

Captura de una query para encontrar la película en MongoDB Compass:

![12](img/12.png)
