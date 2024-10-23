# Enunciado:
# Tarea MongoDB: Operaciones sobre la colección `listingsAndReviews` de la base de datos `sample_airbnb`

Una vez configurado tu clúster en MongoDB con los datos de ejemplo, como se explica en el libro de apuntes, debes implementar las siguientes operaciones en MongoSh sobre la colección **listingsAndReviews** de la base de datos **sample_airbnb**, que contiene los datos de una muestra de alojamientos de Airbnb:

1. Número de alojamientos en España (campo **country** dentro del objeto **address**).

2. Número de alojamientos que permiten alojar (campo **accommodates**) al menos a 10 personas.

3. Número de alojamientos que no tienen especificado un coste de limpieza (campo **cleaning_fee**).

4. Número de alojamientos que estén equipados (campo **amenities**) con microondas (**Microwave**) o horno (**Oven**).

5. Listado de todos los posibles tipos de propiedad (campo **property_type**).

6. Número de alojamientos que contienen la palabra "excellent" (sin distinguir mayúsculas de minúsculas) en el resumen (**summary**).

7. Añade un nuevo alojamiento con la siguiente información:
   - Nombre (**name**): **Nice apartment in Palma**
   - Tipo de propiedad (**property_type**): **Apartment**
   - Tipo de habitación (**room_type**): **Entire home/apt**
   - Dos equipamientos (**amenities**): **Kitchen** y **Parking**

8. Modifica el alojamiento que has creado en el apartado anterior (lo puedes recuperar a partir de su nombre) para añadir la siguiente información:
   - Capacidad (**accommodates**): 4
   - Habitaciones (**bedrooms**): 2
   - Camas (**beds**): 3
   - Baños (**bathrooms**): 1

9. Elimina el alojamiento que has creado y modificado en los dos apartados anteriores (lo puedes recuperar a partir de su nombre).

10. Nombre y precio (campo **price**) del alojamiento más caro en Portugal.

11. Nombre, país y número de reseñas (campo **number_of_reviews**) de los 3 alojamientos que tienen más reseñas.

12. Nombre y rating (campo **review_scores_rating** dentro del objeto **review_scores**) de los alojamientos de Barcelona (campo **market** dentro del objeto **address**) que tienen al menos 4 habitaciones (campo **bedrooms**) y 3 baños (campo **bathrooms**), con un rating superior a 95 sobre 100, ordenados por rating de mayor a menor.


# Solución:
Aquí teniu una solució de l'activitat d'aprenentatge, tot i que n'hi ha d'altres que també són igualment correctes.

  

Començam seleccionant la base de dades _sample\_airbnb_:

use sample\_airbnb

  
  
  

1. Nombre d'allotjaments d'Espanya:  

db.listingsAndReviews.find({"address.country":"Spain"}).count()

Una altra manera per comptar els documents és emprant el mètode _countDocuments_:

db.listingsAndReviews.countDocuments({"address.country":"Spain"})

Resultat: **633**  

  

2. Nombre d'allotjaments que permeten allotjar (camp _accommodates_) a almenys 10 persones:

db.listingsAndReviews.find({"accommodates":{$gte:10}}).count()

Resultat: **148**  

  

3. Nombre d'allotjaments que no tenen especificat un cost de neteja (camp _cleaning\_fee_):

db.listingsAndReviews.find({"cleaning\_fee":{$exists:false}}).count()

Resultat: **1531**  

  

4. Nombre d'allotjaments que estiguin equipats (camp _amenities_) amb microones (_Microwave_) o forn (_Oven_):

db.listingsAndReviews.find({"amenities":{$in:\["Microwave","Oven"\]}}).count()

Resultat: **1806**

  

5\. Llistat de tots els possibles tipus de propietat (camp _property\_type_) 

db.listingsAndReviews.distinct("property\_type")

Resultat:

\[  
  'Aparthotel',             'Apartment',  
  'Barn',                   'Bed and breakfast',  
  'Boat',                   'Boutique hotel',  
  'Bungalow',               'Cabin',  
  'Camper/RV',              'Campsite',  
  'Casa particular (Cuba)', 'Castle',  
  'Chalet',                 'Condominium',  
  'Cottage',                'Earth house',  
  'Farm stay',              'Guest suite',  
  'Guesthouse',             'Heritage hotel (India)',  
  'Hostel',                 'Hotel',  
  'House',                  'Houseboat',  
  'Hut',                    'Loft',  
  'Nature lodge',           'Other',  
  'Pension (South Korea)',  'Resort',  
  'Serviced apartment',     'Tiny house',  
  'Townhouse',              'Train',  
  'Treehouse',              'Villa'  
\]

  

  

6\. Nombre d'allotjaments que contenen la paraula "_excellent_" (sense distingir majúscules de minúscules) en el resum (_summary_):

db.listingsAndReviews.find({"summary": {$regex:/excellent/i}} ).count()  

Resultat: **73**

  

  

7\. Afegeix un nou allotjament amb la següent informació:

*   Nom (_name_): _Nice apartment in Palma_
*   Tipus de propietat (_property\_type_): _Apartment_
*   Tipus d'habitació (_room\_type_): _Entire home/apt_
*   Dos equipaments (_amenities_): _Kitchen_ i _Parking_

db.listingsAndReviews.insertOne({"name":"Nice apartment in Palma", "property\_type": "Apartment", "room\_type":"Entire home/apt", "amenities": \["Kitchen","Parking"\]})

  

  

8\. Modifica l'allotjament que has creat en l’apartat anterior (el pots recuperar a partir del seu nom) per afegir la següent informació:

*   Capacitat (accommodates): 4
*   Habitacions (bedrooms): 2
*   Llits (beds): 3
*   Banys (bathrooms): 1

db.listingsAndReviews.updateOne({"name":"Nice apartment in Palma"}, {$set:{"accommodates":4, "bedrooms":2,"beds":3, "bathrooms":1}})

  

  

9\. Elimina l'allotjament que has creat i modificat en els dos darrers apartats (el pots recuperar a partir del seu nom):

db.listingsAndReviews.deleteOne({"name":"Nice apartment in Palma"})

  

  

10\. Nom i preu (camp _price_) de l'allotjament més car de Portugal:

db.listingsAndReviews.find({"address.country":"Portugal"},{"name":1,"price":1,"\_id":0 }).sort({"price":-1}).limit(1)

Resultat:

{  
  name: 'Casa de Vilela',  
  price: Decimal128("500.00")  
}

  

  

11\. Nom, país i nombre de _reviews_ (camp _number\_of\_reviews_) dels 3 allotjaments que tenen més reviews:

db.listingsAndReviews.find({},{"name":1,"address.country":1,"number\_of\_reviews":1,"\_id":0}).sort({"number\_of\_reviews":-1}).limit(3)

Resultat:

{  
  name: '#Private Studio - Waikiki Dream',  
  number\_of\_reviews: 533,  
  address: {  
    country: 'United States'  
  }  
}  
{  
  name: 'Near Airport private room, 2 bedroom granny flat\*\*',  
  number\_of\_reviews: 469,  
  address: {  
    country: 'Australia'  
  }  
}  
{  
  name: 'La Sagrada Familia (and metro) 4 blocks!',  
  number\_of\_reviews: 463,  
  address: {  
    country: 'Spain'  
  }  
}

  

  

12\. Nom i _rating_ (camp _review\_scores\_rating_ dins de l'objecte _review\_scores_) dels allotjaments de Barcelona (camp _market_ dins de l'objecte _address_) que tenen almenys 4 habitacions (camp _bedrooms_) i 3 banys (camp _bathrooms_), amb un _rating_ superior a 95 sobre 100, ordenats per rating de major a menor:

db.listingsAndReviews.find({"address.market": "Barcelona", "beds": {$gte:4}, "bathrooms": {$gte:3.0}, "review\_scores.review\_scores\_rating":{$gt:95}},{"name":1,"review\_scores.review\_scores\_rating":1,"\_id":0}).sort({"review\_scores.review\_scores\_rating":-1})

Resultat:  

{  
  name: "Big apartment by Barcelona's main train station",  
  review\_scores: {  
    review\_scores\_rating: 100  
  }  
}  
{  
  name: 'Autèntic Monumental 32',  
  review\_scores: {  
    review\_scores\_rating: 96  
  }  
}
