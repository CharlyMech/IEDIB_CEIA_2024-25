import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
	'tema-json',
	bootstrap_servers='localhost:9092',
	auto_offset_reset='earliest',  # Comença a llegir des del primer missatge
	value_deserializer=lambda v: json.loads(v.decode('utf-8'))  # Deserialitza JSON
)

for message in consumer:
	print(f"Rebut: {message.value}")  