# Especificam les versions que emprarem de Spark i JupyterLab
SPARK_VERSION="3.5.5"
JUPYTERLAB_VERSION="4.3.6"

# Cream la imatge Docker spark-master
docker build \
  --build-arg spark_version="${SPARK_VERSION}" \
  -f spark-master.Dockerfile \
  -t spark-master .

# Cream la imatge Docker spark-worker
docker build \
  --build-arg spark_version="${SPARK_VERSION}" \
  -f spark-worker.Dockerfile \
  -t spark-worker .

# Cream la imatge Docker jupyterlab
docker build \
  --build-arg spark_version="${SPARK_VERSION}" \
  --build-arg jupyterlab_version="${JUPYTERLAB_VERSION}" \
  -f jupyterlab.Dockerfile \
  -t jupyterlab .
