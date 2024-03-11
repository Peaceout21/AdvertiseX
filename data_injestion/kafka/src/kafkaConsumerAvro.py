from confluent_kafka import Consumer, KafkaError
from fastavro import reader
import io

config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(**config)
consumer.subscribe(['bid-requests'])

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        message_bytes = io.BytesIO(msg.value())
        for record in reader(message_bytes):
            print(record)

finally:
    consumer.close()
