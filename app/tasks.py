from time import sleep
from app.celery_worker import celery

@celery.task(bind=True)
def long_running_task(self, duration: int):
    """
    Simulates a long-running task
    """
    for i in range(duration):
        sleep(1)
        self.update_state(
            state="PROGRESS",
            meta={"current": i + 1, "total": duration}
        )

    return {"status": "Task completed!", "duration": duration}