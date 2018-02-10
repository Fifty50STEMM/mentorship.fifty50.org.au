from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


CHOICE_GENDER = [
    (None, ''),
    ('f', 'Female'),
    ('m', 'Male'),
    ('x', 'private'),
]


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns around the globe.
    # Although people are still confused by `full_name` convention, including
    # `first` and `last` as intermediaries.
    # `last_name` is also useful for sorting.

    email = models.EmailField(_('Email'))

    first_name = models.CharField(
        _('First Name'), blank=True, max_length=255)

    last_name = models.CharField(
        _('Last Name'), blank=True, max_length=255)

    preferred_name = models.CharField(
        _('Preferred Name'), blank=True, max_length=100,
        help_text="The name you prefer to be refered to as.")

    full_name = models.CharField(
        _('Full Name'), blank=True, max_length=100,
        help_text="eg. 'Francesca Maclean' or 'Emily Li Xiu Ying'")

    gender = models.CharField(
        _('Gender'), blank=True, default='', max_length=1,
        choices=CHOICE_GENDER)

    interests = models.CharField(
        _('Interests, hobbies or sports'), blank=True, max_length=512)

    profile = models.TextField(_('About Me'), blank=True)

    def __str__(self):
        if self.full_name:
            return "{} (@{})".format(self.full_name, self.username)
        else:
            return self.username

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'username': self.username})

    def save(self, *args, **kwargs):
        self.full_name = "{} {}".format(self.first_name, self.last_name)
        if not self.preferred_name:
            self.preferred_name = self.first_name
        super(User, self).save()
