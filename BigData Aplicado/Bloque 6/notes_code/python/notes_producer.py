from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"]
)

producer.send("tema-prova", value="Un nou esdeveniment".encode("utf-8")) # Envia l'esdeveniment al buffer del broker
producer.flush() # Garanteix que el missatge s'enviï immediatament