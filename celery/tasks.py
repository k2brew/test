from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')

@app.task
def add(x, y):
    f = open("output.txt","a")
    val = x + y
    f.writelines(str(x) + " + " + str(y) + " = " + str(val) + "\n")
    f.close()
    return val