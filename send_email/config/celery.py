# ето файл служит для создания celery внутри нашего текущего проекта

import os
from celery import Celery

# устанавливаем путь к настроякам celery проекта
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# создание celery для текущего проекта
app = Celery("config")

# устанавливаем истчник настроек для celery , теперь в setting.py -> CELERY асоциируться с celery
app.config_from_object("django.conf:settings", namespace="CELERY")

# автоматическое обнаружение модулей tasks.py в нашем приложении
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
