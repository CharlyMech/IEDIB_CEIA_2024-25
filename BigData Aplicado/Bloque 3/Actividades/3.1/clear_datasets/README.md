# Transform data for section 2 from task CE_5075 3.1

This notebook is used to remove `NaN` values from datasets and use the result for the HiveQL queries. To use this tiny project you need to follow the following steps:

-  Install the requited dependencies using Poetry ([how to install poetry](https://python-poetry.org/docs/#installation))

```bash
poetry install

```

-  Execute the script

```bash
poetry run python clear_datasets/transform.py [csv_url] -o/--output [file_name]

```

The `-o/--output` parameter is not required, the name from the URL will be set as default
