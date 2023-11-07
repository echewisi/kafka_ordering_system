import json
from kafka import KafkaConsumer

ORDER_CONFIRMED_KAFKA_TOPIC= "order_confirmed"

consumer= KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC, bootstrap_servers= "localhost:29092"
)

emails_sent= set()
print("email is listening...")

while True:
    for message in consumer:
        consumed_message= json.loads(message.value.decode())
