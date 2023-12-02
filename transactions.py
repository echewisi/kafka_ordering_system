import json
from kafka import KafkaConsumer, KafkaProducer

ORDER_KAFKA_TOPIC= "order_details"
ORDER_CONFIRMED_KAFKA_TOPIC= "order_confirmed"
"""
qhat the trasnactions.py file does is it receives a particular order detail from the kafka producer, reads it
from the topic, decodes it, and sends back the required data points to a producer, writing to a new topic that confirms 
orders"""
consumer= KafkaConsumer(
    ORDER_KAFKA_TOPIC,
    bootstrap_servers= "localhost:29092"
)

producer= KafkaProducer(
    bootstrap_servers= "localhost:29092"
)

print("listening started")

while True:
    for message in consumer:
        consumed_message= json.loads(message.value.decode())
        print(consumed_message)
        user_id= consumed_message["user_id"]
        total_cost= consumed_message["total_cost"]
        
        data= {
            "customer_id": user_id,
            "customer_email": f'{user_id}@gmail.com',
            "total_cost": total_cost
        }
        
        print("successful transaction...")
        
        producer.send(
            ORDER_CONFIRMED_KAFKA_TOPIC, json.dumps(data).encode("utf-8")
        )