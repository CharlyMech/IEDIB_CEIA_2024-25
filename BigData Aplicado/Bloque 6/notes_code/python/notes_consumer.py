from kafka import KafkaConsumer

consumer = KafkaConsumer('tema-prova',
	bootstrap_servers=['localhost:9092'],
	auto_offset_reset='earliest', # Comença a llegir des del primer missatge
	value_deserializer=lambda x: x.decode('utf-8')
)

for message in consumer:
	print("Missatge rebut: ", message.value)