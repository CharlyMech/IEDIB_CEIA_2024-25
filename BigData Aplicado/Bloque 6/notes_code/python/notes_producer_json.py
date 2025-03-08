import json
from kafka import KafkaProducer

producer = KafkaProducer(
	bootstrap_servers='localhost:9092',
	value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialitza els missatges com JSON
)

for i in range(10):
	message = {"id": i, "text": f"Missatge número {i}"}
	producer.send('tema-json', value=message) # Envia el missatge al topic tema-json
	print(f"Enviat: {message}")

producer.flush()  # Assegura que tots els missatges s'enviïn abans de tancar
producer.close()  # Tanca el recurs i, si queda algun missatge per enviar, l'envia