## Seleccionam la imatge base
# Especificam com a imatge base una imatge Debian llleuger amb Java 8 JRE
FROM openjdk:8-jre-slim


## Descarregam e instal·lam les dependències
# Definim les variables del Dockerfile
ARG spark_version
ARG jupyterlab_version
ARG hdfs_simulat=/opt/workspace #directori compartit on simulam HDFS
ARG jupyterlab_web=8888 # port per a la interfície web de JupyterLab

# Definim la variable d'entorn amb el port de JupyterLab
ENV JUPYTERLAB_PORT=${jupyterlab_web}

# Definim les variables d'entorn amb el directori que simula HDFS
ENV HDFS_SIMULAT=${hdfs_simulat}

# Instal·lam la darrera versió estable de Python3
RUN mkdir -p ${hdfs_simulat} && \
    apt-get update -y && \
    apt-get install -y python3 && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*
RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    pip3 install gdown numpy matplotlib scipy scikit-learn

# Instal·lam la versión especificada de Pyspark i JupyterLab
RUN pip3 install wget pyspark==${spark_version} jupyterlab==${jupyterlab_version}


## Executam les ordres en arrencar el contenidor
# Montam el HDFS simulat en una carpeta amb dades persistents
VOLUME ${hdfs_simulat}
#CMD ["bash"]

# Exposam el port utilitzat per JupyterLab
EXPOSE ${jupyterlab_web}

# Especificam la ruta de treball dins del contenidor
WORKDIR ${HDFS_SIMULAT}

# Executam JupyterLab en el port especificat
CMD jupyter lab --ip=0.0.0.0 --port=${JUPYTERLAB_PORT} --no-browser --allow-root --NotebookApp.token=
