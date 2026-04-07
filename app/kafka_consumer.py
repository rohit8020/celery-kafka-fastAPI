# app/kafka_consumer.py

from kafka import KafkaConsumer
import json
from app.tasks import long_running_task   # ✅ ADD THIS

print("🚀 Starting Kafka Consumer...")

consumer = KafkaConsumer(
    "tasks",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="task-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

print("✅ Connected to Kafka, waiting for messages...")

for message in consumer:
    data = message.value
    print(f"📥 Received: {data}")

    # 🔥 THIS WAS MISSING
    task = long_running_task.delay(data["duration"])

    print(f"📤 Sent to Celery: {task.id}")