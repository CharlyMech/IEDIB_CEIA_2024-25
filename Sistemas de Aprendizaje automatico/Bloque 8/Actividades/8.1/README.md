# 1. Executa el codi del cas pràctic enllaçat des dels apunts i modifica'l perquè mostri la trajectòria que ha après l'agent. Quantes de moviments necessita per arribar a l'objectiu?

Exercici resolt en l'arxiu [GridWorld_exercises-1-2-3.ipynb](./GridWorld_exercises-1-2-3.ipynb) marcat amb `#! (1)`.

La definició del métode `get_best_trajectory` retornarà un array amb totes les coordenades, aleshores només fa falta fer uns `print()` de l'array al complet i la seva llargària menys un (es té en compte la posició inicial).

```python
...
trajectory = get_best_trajectory()
#! (1)
print(f'Camí après: {trajectory}')
print(f'Nombre de moviments: {len(trajectory) - 1}')
```

# 2. Canvia els obstacles perquè la trajectòria apresa per l'agent sigui la següent: `((0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(3,2),(2,2),(1,2),(0,2),(0,3),(0,4),(1,4),(2,4),(3,4),(4,4))`

Exercici resolt en l'arxiu [GridWorld_exercises-1-2-3.ipynb](./GridWorld_exercises-1-2-3.ipynb) marcat amb `#! (2)`.

En la primera graella del quadern, només fa falta fer les següents modificacions pero que la trajectòria canvï a l'indicada:

```python
# Grid setup
GRID_SIZE = 5
# OLD
# GOLD = (3, 3)
# TRAPS = [(2, 3), (3, 2), (2, 2)]
#! (2)
GOLD = (4, 4)
TRAPS = [(0,1), (1,1), (2,1), (3,1), (1,3), (2,3), (3,3), (4,3)]
# Accions possibles: amunt, avall , esquerra, dreta
ACTIONS = [(-1,0), (1,0), (0,-1), (0,1)]
```

# 3. Redueix el nombre d'epochs d'aprenentatge. A partir de quin valor l'agent sol aprendre a resoldre el problema?

Exercici resolt en l'arxiu [GridWorld_exercises-1-2-3.ipynb](./GridWorld_exercises-1-2-3.ipynb) marcat amb `#! (3)`.

En la graella on es definex els paràmetres d'aprenentatge, es realitzen les següents modificacions:

```python
# Q-learning parameters
Q = {}
alpha = 0.1
gamma = 0.9
epsilon = 0.2
# OLD
# episodes = 500
#! (3)
episodes = 250
```

# 4. Defineix un problema en què sigui impossible arribar a l'objectiu. Quina política aprèn l'agent en aquest cas?

Exercici resolt en l'arxiu [GridWorld_exercise-4_unreachable.ipynb](./GridWorld_exercise-4_unreachable.ipynb) marcat amb `#! (3)`.

La forma més fàcil de fer l'experiment impossible de realizar es rodejar l'objectiu d'obstacles (només fa falta els costats, no les cantonades). Fent algunes modificacions de l'arxiu per als exercicis prèvis s'obté el resultat desitjat.

```python
# Grid setup
GRID_SIZE = 5
# OLD
# GOLD = (3, 3)
# TRAPS = [(2, 3), (3, 2), (2, 2)]
# (2)
# GOLD = (4, 4)
# TRAPS = [(0,1), (1,1), (2,1), (3,1), (1,3), (2,3), (3,3), (4,3)]
#! (4)
GOLD = (4, 4)
TRAPS = [(3,4), (4,3)]
# Accions possibles: amunt, avall , esquerra, dreta
ACTIONS = [(-1,0), (1,0), (0,-1), (0,1)]
```

En aquest cas, he decidit que l'objectiu estigui en una cantonda de la graella i només utilitzar dos obstacles.

# 5. Obtén un codi com el del cas pràctic a través d'enginyeria de prompting. Quantes iteracions has necessitat? Has hagut de retocar el codi finalment a mà? Copia el teu codi a una cel·la del quadern i dona també la URL del teu diàleg sobre l'eina que hagis emprat.

Exercici resolt en el directori [GridWorld_exercise-5](./GridWorld_exercise-5/). En el meu cas he decidit utilitzar el xat de Claude i compartir-ho ([enllaç a l'artifact](https://claude.ai/share/e77690ad-ea63-444d-a9c5-985bbd1a2c03)).

Els primers prompts van ser el següents per donar context del codi i objectiu (`+` soc jo i `*` es Claude):

> \+ I'm going to give you my current code context and then I'll ask you about what I want you to do, so until I ask you, don't answer or tell me anything about this code context

> \* I understand. I'll wait for you to provide your current code context, and then I'll hold off on any responses until you explicitly ask me a question. Please go ahead and share the context whenever you're ready.

> \+ (Aferro el codi actual de l'arxiu original)

> \* I'm ready for your question about this code when you want to ask it. I've reviewed the Q-learning grid world implementation you've shared, but I'll wait for your specific instructions before responding with any analysis or suggestions.

> \+ As you can see this is an experiment of machine learning (reinforcement learning) where the system needs to "catch the gold". What I want you to do is to create a similar experiment (don't just modify this code, reinvent the wheel) that is based on this topic (machine learning, reinforcement learning). Provide the required python code with the required libraries. Use the same visualization system to show the experiment evolution

Despés d'això es retorna el contingut de l'arxiu [iteration_1.ipynb](./GridWorld_exercise-5/iteration_1.ipynb). El que es pot veure es que realitza exactament el mateix experiment però afegint una dinàmica de _predator and prey_ de tal forma que el target (la presa) es troba també en moviment. No conforme amb el resultat (tot i que es molt satisfactori), vaig realitzar un segon prompt.

> \+ Tell me more about this topic experiments, are there any other kind of experiments? Could it be another type of game rather than catching something? Could you please implement it and show me the code?

La resposta es troba en l'arxiu [iteration_2.ipynb](./GridWorld_exercise-5/iteration_2.ipynb). Ara el resultat m'intriga més ja que es més abstracte. L'agent ha decidit realitzar un experiment basat en dades meteorológiques.

Ja que al final me preguntava per si volia realitzar un experiment dels que proposava, vaig decidir realizar un tercer i últim prompt, en aquest cas sobre l'opció de _Natural Language Processing_ (resultat en l'arxiu [iteration_3.ipynb](./GridWorld_exercise-5/iteration_3.ipynb)), però lamentablement va arribar al límit de Claude per a un únic xat.

> \+ Try now with the Natural Language Processing as last example of RL experiments
