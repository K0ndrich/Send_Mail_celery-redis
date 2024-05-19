from django.core.mail import send_mail


# send_mail функция для отправки разсылок пользователям на email
def send(user_email):
    send_mail(
        "Вы подписаны на розсылку",
        "Мы будем присылать много спама",
        "123kondrich@gmail.com",
        [user_email],
        fail_silently=False,
    )
