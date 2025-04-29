# Creación del nuevo recurso

Se siguen los mismos pasos para crer un nuevo cómputo que en el [apartado anterior](../section2/README.md) aplicando los parámetros necesarios para hacer uso del AutoML de Azure Databricks además de la correspondiente carga del archivo [penguins_size.csv](./penguins_size.csv).

![Create resource](./screenshots/00%20create%20ml.png)

![Load data](./screenshots/01%20load%20data.png)

# Crear un nuevo experimento

Para crear nuevo experimento, sencillamente se selecciona _Experiment_ en la parte superior izquierda (en el botón _+ New_) y se siguien los pasos mostrados en las imágenes siguientes (en este caso el experimento será de tipo Clasificación):

![Create experiment](./screenshots/02%20new%20experiment.png)

![Create experiment](./screenshots/03%20new%20experiment.png)

Al iniciar el experimento aparecerá la pantalla siguiente, indicando el tiempo restante de éste. Al principio no aparecerá nada, pero a medida que pasa el tiempo se irán registrando experimentos en formato de tabla.

![Running experiment](./screenshots/04%20running%20experiment.png)

![Running experiment](./screenshots/05%20running%20experiment.png)

![Running experiment - hyperparameters](./screenshots/06%20running%20experiment%20-%20hyperparameters.png)

# Registrar un nuevo modelo

En la parte superior derecha de la última imagen se puede apreciar un botón que dice _Register model_ el cual nos permite registrar un nuevo modelo para realizar predicciones. Se sisguen los pasos mostrados en las siguientes imágenes.

![Register model](./screenshots/07%20register%20model.png)

![Register model](./screenshots/08%20registered%20model.png)

En el apartado _Serving_ del menú lateral, creamos un nuevo endpoint para realizar las predicciones, asignándole a éste el modelo recién registrado.

![Create new endpoint](./screenshots/09%20create%20endpoint.png)

Una vez el endpoint está lanzado (indicado con el estado _Ready_), se podrán realizar peticiones desde la misma interfaz de Azure Databricks haciendo click el el botón superior derecho (_Use_)

![Endpoint request and response](./screenshots/10%20endpoint%20request%20and%20response.png)

-  [request.json](./request.json):

```json
{
	"dataframe_split": {
		"columns": [
			"island",
			"culmen_length_mm",
			"culmen_depth_mm",
			"flipper_length_mm",
			"body_mass_g",
			"sex"
		],
		"data": [
			["Torgersen", "39.1", "18.7", "181", "3750", "MALE"],
			["Torgersen", "36.7", "19.3", "193", "3450", "FEMALE"],
			["Torgersen", "38.9", "17.8", "181", "3625", "FEMALE"],
			["Torgersen", "39.2", "19.6", "195", "4675", "MALE"],
			["Torgersen", "37.8", "17.3", "180", "3700", "NA"]
		]
	}
}
```

-  [response.json](./response.json):

```json
{
	"predictions": ["Adelie", "Adelie", "Adelie", "Adelie", "Adelie"]
}
```

-  Código en python:

![Python code](./screenshots/11%20python%20code.png)

```python
import os
import requests
import numpy as np
import pandas as pd
import json

def create_tf_serving_json(data):
    return {'inputs': {name: data[name].tolist() for name in data.keys()} if isinstance(data, dict) else data.tolist()}

def score_model(dataset):
    url = 'https://adb-27584284548780.0.azuredatabricks.net/serving-endpoints/penguin/invocations'
    headers = {'Authorization': f'Bearer {os.environ.get("DATABRICKS_TOKEN")}', 'Content-Type': 'application/json'}
    ds_dict = {'dataframe_split': dataset.to_dict(orient='split')} if isinstance(dataset, pd.DataFrame) else create_tf_serving_json(dataset)
    data_json = json.dumps(ds_dict, allow_nan=True)
    response = requests.request(method='POST', headers=headers, url=url, data=data_json)
    if response.status_code != 200:
        raise Exception(f'Request failed with status {response.status_code}, {response.text}')
    return response.json()
```

Como conclusión sobre los resultados, se observa que únicamente ha predicho que la especie es '_Adelie_', lo cual puede hacer pensar que el modelo no es correcto. Realizamos otra request (esta vez con los mismos datos usados en el bloque 3 de la asignatura de programación) para comprobar si realmente el modelo no predice correctamente los datos.

![Second request](./screenshots/12%20second%20request.png)

-  [request2.json](./request2.json):

```json
{
	"dataframe_split": {
		"columns": [
			"island",
			"culmen_length_mm",
			"culmen_depth_mm",
			"flipper_length_mm",
			"body_mass_g",
			"sex"
		],
		"data": [
			["Biscoe", "39.1", "18.7", "181.0", "3750.0", "FEMALE"],
			["Dream", "45.3", "17.1", "200.0", "4200.0", "MALE"],
			["Torgersen", "50.0", "15.2", "210.0", "5000.0", "MALE"]
		]
	}
}
```

-  [response2.json](./response2.json):

```json
{
	"predictions": ["Adelie", "Chinstrap", "Gentoo"]
}
```

Ahora podemos observar que la predicción es uno de cada especie. La comparación con la entrega de la asignatura de programación del bloque 3 usando regresión logística es la siguiente:

| Num | Predicción Bloque 3 | Predicción Actual |
| --- | ------------------- | ----------------- |
| 1   | Adelie (0.999)      | Adelie            |
| 2   | Chinstrap (0.716)   | Chinstrap         |
| 3   | Gentoo (0.975)      | Gentoo            |

Observando los resultados comparados (porcentajes de probabilidad de la entrega 3 entre paréntesis) podemos concluir que el primer resultado puede resultar anómalo pero esta segunda prueba es bastante satisfactoria.
