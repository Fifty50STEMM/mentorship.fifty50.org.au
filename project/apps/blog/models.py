from django.db import models
from django.utils import timezone


class Post(models.Model):

    author = models.ForeignKey('users.User')

    title = models.CharField(max_length=200)

    text = models.TextField()

    image = models.ImageField(
        upload_to='blogs/post/', blank='', default='')

    create_date = models.DateTimeField(
        default=timezone.now)

    publish_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
