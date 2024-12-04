Dissenya un graf dirigit que representi una petita xarxa de comunicacions amb els següents requisits:

-  El graf té dos tipus de nodes (etiquetes): Ciutat i Poble El graf té un mínim de 10 nodes (meitat ciutats, meitat pobles).
-  Cada node té dues propietats: nom (una cadena de text) i poblacio (un número enter).
-  Les ciutats tenen més de 10.000 habitants i els pobles menys.
-  El graf té un mínim de 30 arestes (recordem que és un graf dirigit, les arestes tenen direcció), de dos tipus diferents: CARRETERA i PISTA.
-  Cada aresta té dues propietats: distancia (en quilòmetres, un número enter) i temps (en minuts, un número enter)
-  S'ha de poder arribar i sortir de cada node (cada node ha de tenir almenys una aresta d'entrada i una de sortida)

Crea el teu graf en Neo4j (en el Sandbox o en el teu servidor local) i executa les següents consultes:

1. Recupera el nom de totes les ciutats.
2. Recupera tots els pobles als quals s'hi pot arribar per carretera (sense usar les pistes), a través d'una única aresta.
3. Tria el nom d'una ciutat i recupera tots els pobles i ciutats als quals podem arribar per carretera (a través d'una única aresta) des d'ella.
4. Tria el nom d'un poble i recupera tots els pobles i ciutats des dels quals podem arribar (a través d'una única aresta) fins a ell. Indica també si s'hi arriba per carretera o per pista.
5. Afegeix un nou node poble, amb les seves dades, amb una aresta d'entrada i una altra de sortida.
6. Modifica la població del node anterior.
7. Esborra les dues arestes del nou node.
8. Esborra el nou node.
9. Recupera tots els pobles de menys de 5.000 habitants.
10.   Recupera tots els pobles des dels quals es pot arribar per carretera (a través d'una única aresta) a una ciutat de més de 20.000 habitants.
11.   Recupera el nom i població de totes les ciutats, ordenades per població, de major a menor.
12.   Tria el nom d'una ciutat i fes un recorregut en amplitud des d'ella.
13.   Tria el nom d'un poble i fes un recorregut en profunditat des d'ell.
14.   Tria el nom de dues ciutats que no estiguin directament connectades i recupera el camí més curt en temps entre elles, emprant l'algorisme de Dijkstra.
15.   Tria el nom de dos pobles que no estiguin directament connectats i recupera el camí més curt en distància entre ells, emprant l'algorisme de Dijkstra.
16.   Determina el grau de sortida (influència) de cada node del graf, ordenats de major a menor.
17.   Determina el valor de proximitat (closeness) de cada node del graf, ordenats de major a menor.
18.   Determina el valor d'intermediació (betweenness) de cada node del graf, ordenats de major a menor.
19.   Determina el nombre de triangles de cada node del graf, ordenats de major a menor. Per fer-ho, abans projecta el teu graf a un nou graf GDS no dirigit.
20.   Tria dos noms de ciutats o pobles que no estiguin directament connectats i determina el número de veïnats comú.

> Quan en l'enunciat diu "a través d'una única aresta", vol dir "a través d'un enllaç directe", sense tenir en compte camins que passin per diversos nodes, només connexions directes. Per exemple, en la pregunta 3, has de triar una ciutat, per exemple Inca, i has de contestar quins pobles o ciutats estan directament connectats per carretera des d'Inca. És a dir, a través de les arestes de tipus carretera que surten del node Inca, a quins nodes podem arribar?

```
Quan hem creat un graf GDS en els exemples dels apunts, només teníem una etiqueta i un tipus de relació. Aquí en tenim dos de cada, així que, quan projectem el nostre graf a un graf GDS, li hem de passar una llista d'etiquetes de nodes i una llista de noms de relacions.

Per tant, amb aquesta sentència projectaríem el nostre graf a un graf GDS amb nom 'xarxa':

CALL gds.graph.project(
    'xarxa',
    ['Poble',  'Ciutat'],
    ['PISTA', 'CARRETERA']
)


Tingues present que aquí no hem especificat les propietats de cost de les arestes. Així que hauràs de fer algun canvi en aquesta sentència per obtenir el graf GDS que necessites.
```
