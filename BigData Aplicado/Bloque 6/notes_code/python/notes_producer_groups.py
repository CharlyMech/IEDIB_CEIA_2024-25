from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
	bootstrap_servers=['localhost:9092'],
	value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for i in range(100):
	message = {"id": i, "text": f"Missatge {i}"}
	producer.send('tema-grups', value=message)
	print(f"Enviat: {message}")
	time.sleep(1)  # Simulam un retard entre missatges

producer.flush()
producer.close()