from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


CHOICE_GENDER = (
    ('m', 'Male'),
    ('f', 'Female'),
    ('x', 'pass'),
)


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    preferred_name = models.CharField(
        _('Name of User'), blank=True, max_length=100,
        help_text="The name you prefer to be refered to as.")

    full_name = models.CharField(
        _('Full Name'), blank=True, max_length=100,
        help_text="eg. 'Francesca Maclean' or 'Emily Li Xiu Ying'"),

    gender = models.CharField(
        _('Gender'), blank=True, max_length=1, choices=CHOICE_GENDER)

    profile = models.TextField(_('About Me'), blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
