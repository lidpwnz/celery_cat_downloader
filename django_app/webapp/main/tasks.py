from celery import shared_task
import requests as r
import uuid
from django.conf import settings
from django.core.mail import send_mail


CAT_URL = "http://thecatapi.com/api/images/get?format=src&type=gif"


@shared_task
def download_a_cat():
    resp = r.get(CAT_URL)
    file_ext = resp.headers.get('Content-Type').split('/')[1]
    file_name = settings.BASE_DIR / 'cats' / (str(uuid.uuid4()) + "." + file_ext)
    with open(file_name, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=128):
            f.write(chunk)
    return True

@shared_task
def send_email_task():
    send_mail('Celery task worked!', 'This is proof the task worked', 'lidpwnz@gmail.com', [''])
