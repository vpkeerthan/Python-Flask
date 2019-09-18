from pykafka import KafkaClient

client = KafkaClient(hosts="localhost:9092")
topic = client.topics['sample']
producer = topic.get_sync_producer()


count = 1
while count < 10000:
    message = ("Message-" + str(count)).encode('ascii')
    producer.produce(message)
    print (message)
    count = count + 1

