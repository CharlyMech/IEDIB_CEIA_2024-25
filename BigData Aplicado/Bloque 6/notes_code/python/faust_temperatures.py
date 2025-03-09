import faust

app = faust.App('temperature_app', broker='kafka://localhost:9092')

class TemperatureRecord(faust.Record):
	id: int
	sensor_id: int
	temperatura: float
	ingest_time: int
	origen: str

# Topic d'entrada i de sortida
input_topic = app.topic('mysql_temperatures', value_type=TemperatureRecord)
output_topic = app.topic('faust_temperatures_altes', value_type=TemperatureRecord)

@app.agent(input_topic)
async def filter_high_temperatures(stream):
	async for record in stream:
		if record.temperatura > 22:
			await output_topic.send(value=record)

if __name__ == '__main__':
	app.main()