**T'has quedat amb ganes d'aprendre més?**

En els apunts i la tasca no hem entrat a veure com podríem definir consultes amb agregacions. Aquestes operacions poden ser útils per analitzar les dades. Per exemple, en un dataset amb les vendes d'una cadena de tendes, ens podria interessar agrupar les vendes per comunitat autònoma i treure'n la mitjana de cada una, per saber on estan funcionant millor els nostres productes.  

En SQL tenim una sèrie de clàusules (_group by_, _having_) i de funcions (_count_, _sum_, _min_, _max_, _avg_) que ens permeten d'una manera senzilla utilitzar agregacions en les nostres consultes.

En MongoDB no és tan senzill. Hem d'utilitzar les anomenades **_aggregation pipelines_**.

Una _aggregation pipeline_ (_canonada d'agregació_ seria la traducció literal) consisteix en una o més etapes que processen documents:

*   Cada etapa realitza una operació sobre els documents d'entrada. Per exemple, una etapa pot filtrar documents, una altra agrupar documents i una altra, calcular valors.
*   Els documents que surtin d'una etapa es passen a la següent.
*   Una _aggregation pipeline_ pot retornar resultats per a grups de documents. Per exemple, retorna els valors total, mitjà, màxim i mínim.

Vegem un exemple, que conté dues etapes i que retorna la quantitat total de comandes que s'han fet de pizzas de mida petita agrupats per nom de pizza:

    db.orders.aggregate( [
       // Etapa 1: Filtrar els documents de comandes de pizzes per la seva mida (petita)
       {
          $match: { size: "small" }
       },
       // Etapa 2: Agrupa els documents resultats per nom de pizza i calcula la quantitat total
       {
          $group: { _id: "$name", totalQuantity: { $sum: "$quantity" } }
       }
    ] )  

  

L'etapa de $match:  

*   filtra els documents que tenen mida (_size_) petita (_small_)
*   passa els documents resultats a l'etapa de $group

L'etapa de $group:  

*   agrupa els documents que li arriben per nom de pizza
*   utilitza $sum per calcular la quantitat total (_quantity_) per a cada nom de pizza (name). La quantitat total s'emmagatzema en un cap _totalQuantity_ del document retornat

  
La següent imatge mostra alguns dels operadors que es poden utilitzar en les etapes d'una _pipeline_:  

![Operadors d'etapes d'una aggregation pipeline](https://iedib.net/avirtual/pluginfile.php/113169/mod_page/content/5/Operadors%20detapes%20duna%20aggregation%20pipeline.png)

Imatge: Operadors d'etapes d'una aggregation pipeline

  
Trobareu tots els detalls d'aquests operadors a [https://www.mongodb.com/docs/manual/reference/operator/aggregation-pipeline/](https://www.mongodb.com/docs/manual/reference/operator/aggregation-pipeline/)  
  
A més, alguns dels operadors d'acumulació més habituals són aquests:  

*   [$count](https://www.mongodb.com/docs/manual/reference/operator/aggregation/count-accumulator/#mongodb-group-grp.-count)
*   [$sum](https://www.mongodb.com/docs/manual/reference/operator/aggregation/sum/#mongodb-group-grp.-sum)
*   [$avg](https://www.mongodb.com/docs/manual/reference/operator/aggregation/avg/#mongodb-group-grp.-avg)
*   [$min](https://www.mongodb.com/docs/manual/reference/operator/aggregation/min/#mongodb-group-grp.-min)
*   [$max](https://www.mongodb.com/docs/manual/reference/operator/aggregation/max/#mongodb-group-grp.-max)

Trobareu el llistat complet al'apartat "Accumulators" de [https://www.mongodb.com/docs/manual/reference/operator/aggregation/](https://www.mongodb.com/docs/manual/reference/operator/aggregation/)  
  

  

IMPORTANT

Podeu trobar més informació sobre les operacions d'agregació al manual de MongoDB: [https://www.mongodb.com/docs/manual/aggregation/](https://www.mongodb.com/docs/manual/aggregation/)  

I també al llibre online [Practical MongoDB Aggregations](https://www.practical-mongodb-aggregations.com/front-cover.html). 

  

  

A partir d'aquí, intenta respondre aquestes dues preguntes, escrivint les _aggregation pipelines_ corresponents:

1\. En la col·lecció _restaurants_ de la base de dades _sample\_restaurants_, quants restaurants de cuina espanyola hi ha a cada districte?

2\. En la col·lecció _movies_ de la base de dades _sample\_mflix_, quin és el gènere amb una qualificació imdb mitjana més alta? (pista: necessitaràs l'operador $unwind)
