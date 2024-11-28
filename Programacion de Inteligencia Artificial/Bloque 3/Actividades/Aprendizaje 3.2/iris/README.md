# How to use this Poetry project

I'll assume that Python 3.8+ and Poetry are installed.

-  Install required dependencies from `pyproject.toml`:

```bash
poetry install
```

-  Run the service:

```bash
	poetry run python iris/service.py
```

-  Execute a request (bash):

```bash
	curl --request POST "http://127.0.0.1:8000/[model endpoint]]" \
	--header "Content-Type: application/json" \
	--data-raw '{
		"longitud_petal": N.N,
    	"amplada_petal": N.N
	}'
```

In the [client.ipynb](notebooks/client.ipynb) file there are some sample executions for each trained model
