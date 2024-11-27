# Project management practice case

This repository is the proccess described in this chapter's notes to handle Python environments using Poetry.

## How to use this repository

#### Install Python and Poetry (if not installed)

First of all make sure you have Python 3.8+ installed in your system.

-  [Python releases official website](https://www.python.org/downloads/)

Then install `pipx` ([install pipx](https://pipx.pypa.io/stable/installation/)) to manage the packages. With all this installed, then proceed to install Poetry in your system.

-  [Poetry installation official guide](https://python-poetry.org/docs/#installation)

#### Install the dependencies

Once the content is downloaded (via clone or downloading the `.zip` file), access the directory and install the depencendies using Poetry:

```bash
	cd [directory]
	poetry install
```

#### Run the service and make a preduction

In this file, under `practice_case` directory, there is some flask code to run a server that will use the model generated to analyze data. To run the service, execute the following command:

```bash
	poetry run python practice_case/chrun_predict_app.py
```

Inside the `notebooks/study_case.ipynb`, there are some `curl` commands that will make the request to the service. You can also execute the same command in your terminal by using:

```bash
	curl --request POST "http://127.0.0.1:8000/predict" --header "Content-Type: application/json" --data-raw '{"gender": "female", "seniorcitizen": 1, "partner": "no", "dependents": "no", "phoneservice": "yes", "multiplelines": "yes", "internetservice": "fiber_optic", "onlinesecurity": "no", "onlinebackup": "no", "deviceprotection": "no", "techsupport": "no", "streamingtv": "yes", "streamingmovies": "no", "contract": "month-to-month", "paperlessbilling": "yes", "paymentmethod": "electronic_check", "tenure": 1, "monthlycharges": 85.7, "totalcharges": 85.7}'
```
