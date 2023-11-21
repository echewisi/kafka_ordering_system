from kafka import KafkaConsumer


ORDER_CONFIRMED_KAFKA_TOPIC= "order_confirmed"

consumer= KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC, bootstrap_servers= "localhost:29092"
)