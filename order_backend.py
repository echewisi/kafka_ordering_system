import json
import time
from kafka import KafkaProducer, KafkaConsumer, KafkaClient


ORDER_KAFKA_TOPIC= "order_details"
ORDER_LIMIT= 15

producer= KafkaProducer(bootstrap_servers="localhost:29092")
print("going to generate order after ten seconds")
print("will generate one unique order every 10 seconds!")

for order in range(1, ORDER_LIMIT):
    data={
        "order_id": order,
        "user_id": f'tom_{order}',
        "total_cost": order*2,
        "items": "burger, sandwich"
    }
    
    producer.send(
        ORDER_KAFKA_TOPIC, json.dumps(data).encode("utf-8")
    )
    print(f'Done sending....{order}')
    time.sleep(10)
