import json
from datetime import datetime
from kafka import KafkaConsumer
from hdfs import InsecureClient

hdfs_client = InsecureClient("http://hadoopmaster:9870", user="hadoop")
hdfs_file = "/user/hadoop/kafka/temperatures.txt"

if not hdfs_client.status(hdfs_file, strict=False):
	with hdfs_client.write(hdfs_file, overwrite=True) as writer:
		writer.write(b"")  # Crear un fitxer buit       

consumer = KafkaConsumer('mysql_temperatures',
	bootstrap_servers=['localhost:9092'],
	auto_offset_reset='earliest',
	enable_auto_commit=True,
	group_id='my_group_id',
	value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Convertir JSON a diccionari
)

for message in consumer:
	msg = message.value
	print("Missatge rebut: ", msg)  

	payload = msg.get("payload", {}) 

	datahora_ms = payload.get("datahora", 0)
	if datahora_ms:
		datahora = datetime.utcfromtimestamp(datahora_ms / 1000).strftime('%d/%m/%Y %H:%M:%S')
	else:
		datahora = "UNKNOWN"

	valor = payload.get("valor", 0.0)

	# Afegir només els valors de datahora i valor, separats per comes, a HDFS
	with hdfs_client.write(hdfs_file, append=True) as writer:
		writer.write(f"{datahora},{valor}\n".encode("utf-8"))