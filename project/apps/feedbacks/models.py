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
