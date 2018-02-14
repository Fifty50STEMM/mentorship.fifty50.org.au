from django.db import models
from django.utils import timezone


class Post(models.Model):

    is_active = models.BooleanField(default=True)

    is_public = models.BooleanField(
        default=False, help_text="Defaults to only displaying to logged in users.")

    author = models.ForeignKey('users.User')

    title = models.CharField(max_length=200)

    slug = models.SlugField(max_length=100)

    text = models.TextField()

    image = models.ImageField(
        upload_to='blogs/post/', blank='', default='')

    create_date = models.DateTimeField(
        auto_now_add=True)

    publish_date = models.DateTimeField(
        default=timezone.now, blank=True, null=True)

    class Meta:
        ordering = ('publish_date',)

    def __str__(self):
        return self.title
