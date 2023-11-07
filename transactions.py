import json
from kafka import KafkaConsumer, KafkaProducer

ORDER_KAFKA_TOPIC= "order_details"
ORDER_CONFIRMED_KAFKA_TOPIC= "order_confirmed"

consumer= KafkaConsumer(
    ORDER_KAFKA_TOPIC,
    bootstrap_servers= "localhost:29092"
)

producer= KafkaProducer(
    bootstrap_servers= "localhost:29092"
)