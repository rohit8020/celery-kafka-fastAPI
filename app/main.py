# app/main.py

from fastapi import FastAPI
from app.kafka_producer import send_task_event

app = FastAPI()


@app.post("/start-task/")
def start_task(duration: int):
    send_task_event(duration)   # 🔥 send to Kafka
    return {"status": "Task sent to Kafka"}

# @app.post("/start-task/")
# def start_task(duration: int):
#     task = long_running_task.delay(duration)
#     return {"task_id": task.id}

# @app.get("/task-status/{task_id}")
# def get_task_status(task_id: str):
#     task_result = celery.AsyncResult(task_id)  # ✅ FIX

#     if task_result.state == "PENDING":
#         return {"status": "Pending"}

#     elif task_result.state == "PROGRESS":
#         return {
#             "status": "In Progress",
#             "details": task_result.info
#         }

#     elif task_result.state == "SUCCESS":
#         return {
#             "status": "Completed",
#             "result": task_result.result
#         }

#     elif task_result.state == "FAILURE":
#         return {
#             "status": "Failed",
#             "error": str(task_result.info)
#         }

#     return {"status": task_result.state}