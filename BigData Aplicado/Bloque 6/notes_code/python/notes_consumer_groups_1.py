from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
	'tema-grups',
	bootstrap_servers=['localhost:9092'],
	group_id='grup-consumidors',  # Mateix grup per compartir els missatges
	auto_offset_reset='earliest',
	enable_auto_commit=True,
	value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("Consumidor 1 esperant missatges...")
for message in consumer:
	print(f"Consumidor 1 ha rebut: {message.value}")  