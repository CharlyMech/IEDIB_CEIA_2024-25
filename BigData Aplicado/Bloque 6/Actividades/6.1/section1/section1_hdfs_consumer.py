import json
from datetime import datetime
from kafka import KafkaConsumer
from hdfs import InsecureClient

HDFS_FILE = '/user/hadoop/kafka/section1.csv' # HDFS file path
DATETIME_FORMAT = '%d/%m/%Y %H:%M:%S' # Datetime format in the payload
hdfs_client = InsecureClient('http://hadoopmaster:9870', user='hadoop')

if not hdfs_client.status(HDFS_FILE, strict=False):
	with hdfs_client.write(HDFS_FILE, overwrite=True) as writer:
		writer.write(b'') # create empty file

consumer = KafkaConsumer('section_1',
	bootstrap_servers=['localhost:9092'],
	auto_offset_reset='earliest',
	enable_auto_commit=True,
	group_id='my_group_id',
	value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Transform from json to dict
)

for message in consumer:
	msg = message.value
	print('Message: ', msg)
	payload = msg.get('payload', {}) 
	values = payload.split(',') # Split the payload by comma

	datetime_str = f'{values[0]} {values[1]}' # Get the first and second values, corresponding to date and time
	datatime_value = datetime.now().strftime('%d/%m/%Y %H:%M:%S') # Default value for datetime_value
	try:
		datatime_value = datetime.strptime(datetime_str, DATETIME_FORMAT).strftime('%d/%m/%Y %H:%M:%S')
	except ValueError:
		print(f'Error: Invalid datetime format: {datetime_str}\nLeaving datetime as current time: {datatime_value}')

	csv_line = f'{datatime_value},{values[2],values[3],values[4]}\n'.encode('utf-8')
	print(csv_line)

	with hdfs_client.write(HDFS_FILE, append=True) as writer:
		writer.write(csv_line)

""" 
	!! THIS CODE HAS NOT BEEN FULLY TESTED
"""