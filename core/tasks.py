import time

from dockerapp.celery_app import app


@app.task
def sample_task(num1):
    for i in range(5):
        num1 += 1
        time.sleep(1)
        print(f"Num: {num1}")

    return num1
