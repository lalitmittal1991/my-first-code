
# importing the required libraries  
from time import sleep  
from json import dumps  
from kafka import KafkaProducer  


# initializing the Kafka producer  
my_producer = KafkaProducer(  
	bootstrap_servers = ['localhost:8089'],
	api_version=(0,11,5),  
	value_serializer = lambda x:dumps(x).encode('utf-8')  
	)
print("producer_assigned")

# generating the numbers ranging from 1 to 500  
for n in range(500):
	print(n)
	my_data = {'num' : n}
	print(n)
	my_producer.send('testnum', value = my_data)
	sleep(5)