from django.core.mail import send_mail, BadHeaderError
from djangoq_project.settings import DEFAULT_FROM_EMAIL


def send_email_task(to, subject, message):
    print(f"from={DEFAULT_FROM_EMAIL}, {to=}, {subject=}, {message=}")
    try:
        print("About to send_mail")
        send_mail(subject, message, DEFAULT_FROM_EMAIL, [DEFAULT_FROM_EMAIL])
    except BadHeaderError:
        print("BadHeaderError")
    except Exception as e:
        print(e)
