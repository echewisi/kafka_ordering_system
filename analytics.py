from kafka import KafkaConsumer
import json


ORDER_CONFIRMED_KAFKA_TOPIC= "order_confirmed"

consumer= KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC, bootstrap_servers= "localhost:29092"
)

total_orders_count= 0
total_revenue= 0
print("listening...")
while True:
    for message in consumer:
        print("updating analytics...")
        command_message= json.loads(message.value.decode())
        total_cost= float(command_message["total_cost"])
        total_orders_count += 1
        total_revenue += total_cost
        print(f"orders today...{total_orders_count}")
        print(f"Revenue so far today...{total_revenue}")