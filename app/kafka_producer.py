# app/kafka_producer.py

from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)
print("Connected to Kafka ✅")

def send_task_event(duration: int):
    producer.send("tasks", {"duration": duration})
    producer.flush()