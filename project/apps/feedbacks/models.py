from django.core.mail import send_mail
from django.db import models


class Feedback(models.Model):

    name = models.CharField(max_length=128)

    email = models.EmailField()

    date_create = models.DateTimeField(auto_now_add=True)

    message = models.TextField()

    class Meta:
        verbose_name_plural = 'feedback'

    def __str__(self):
        return "{}: {} ({})".format(self.date_create, self.name, self.email)

    def email_feedback(self):
        message = """{}
{}
---
message:
{}
""".format(self.name, self.email, self.message)
        send_mail(
            'Fifty50: Feedback received from website',
            message,
            'fifty50mentoring+webserver@gmail.com',
            ['fifty50mentoring@gmail.com'],
            fail_silently=True,
        )

    def save(self, *args, **kwargs):
        super(Feedback, self).save(*args, **kwargs)
        self.email_feedback()
