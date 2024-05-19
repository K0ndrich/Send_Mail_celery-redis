# файл содержит таски который будет выполнять celery

from config.celery import app
from .service import send


# @app.task декоратор указыват что ето фнукция которую будет выполянть celery
@app.task
def send_spam_email(a=5):
    
    print(a)
    # send(user_email)
