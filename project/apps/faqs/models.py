from django.db import models

# @@ TODO could add FAQ groupings/headings


class Faq(models.Model):

    is_active = models.BooleanField(default=True)

    question = models.CharField(max_length=2047)
    answer = models.TextField()

    slug = models.SlugField()

    order = models.SmallIntegerField()

    class Meta:
        ordering = ('order', )

    def __str__(self):
        return self.question
