import json
import time
from kafka import KafkaProducer

"""
in the order_backend the data sent by the producer to a certain topic holds the order_data endpoints.
the data sent is to be consumed by a consumer that will read the topic and get the data from the consumer"""


ORDER_KAFKA_TOPIC= "order_details"
ORDER_LIMIT= 20000

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
    time.sleep(2)
