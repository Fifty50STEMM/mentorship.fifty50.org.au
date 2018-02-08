""" This application contains all the configurable refeference and naming
convention settings for Universities and Degrees."""
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class University(models.Model):
    """ The university. eg. ANU """

    full_name = models.CharField(_('Full Name'), max_length=255)

    abbreviation = models.CharField(
        _('Abbreviation'), max_length=32)

    url = models.URLField(_('Website'), blank=True)

    class Meta:
        verbose_name_plural = "universities"

    def __str__(self):
        return self.abbreviation


class Department(models.Model):
    """ Department responsible for program. eg. CECS """

    is_STEMM = models.BooleanField(_('Is STEMM eligible'), default=True)

    university = models.ForeignKey('universities.University')

    full_name = models.CharField(_('Full Name'), max_length=255)

    abbreviation = models.CharField(
        _('Abbreviation'), blank=True, max_length=32)

    is_active = models.BooleanField(_('Is Active'), default=True)

    url = models.URLField(_('Website'), blank=True)

    def __str__(self):
        return self.abbreviation


@python_2_unicode_compatible
class Cycle(models.Model):
    """ Category model for degree level/cycle. Eg. Bachelor, Master,
Graduate Certificate"""

    full_name = models.CharField(
        _('Full Name'), max_length=255, help_text="Master, Bachelor")

    abbreviation = models.CharField(
        _('Abbreviation'), blank=True, max_length=32)

    def __str__(self):
        return self.full_name


@python_2_unicode_compatible
class Degree(models.Model):

    full_name = models.CharField(
        _('Full Name'), max_length=255,
        help_text="Science, Computing, Clinical Psychology, BiologicalScience (Advanced)")  # noqa

    abbreviation = models.CharField(
        _('Abbreviation'), blank=True, max_length=32)

    is_active = models.BooleanField(_('Is Active'), default=True)

    def __str__(self):
        return self.full_name


@python_2_unicode_compatible
class Program(models.Model):

    university = models.ForeignKey('universities.University')

    department = models.ForeignKey('universities.Department', null=True)

    cycle = models.ForeignKey('universities.Cycle')

    degree = models.ForeignKey('universities.Degree')

    is_STEMM = models.BooleanField(_('Is STEMM eligible'), default=True)

    full_name = models.CharField(
        _('Full Name'), max_length=255, blank=True, default='',
        help_text="Science, Computing, Clinical Psychology, BiologicalScience (Advanced)")  # noqa

    abbreviation = models.CharField(
        _('Abbreviation'), blank=True, max_length=32)

    is_active = models.BooleanField(_('Is Active'), default=True)

    def __str__(self):
        return self.full_name


@python_2_unicode_compatible
class StudyYear(models.Model):
    """ Study year reference """

    study_year = models.CharField(_('Year of Study (number)'), max_length=3)

    reference = models.CharField(
        _('Year of Study'), max_length=128,
        help_text="Human readable version of year of study, eg 'First Year, Final Year'")  # noqa

    def __str__(self):
        return self.reference


class Method(models.Model):
    """ Allowable mentorship methods, eg. Onlines, In Person.

    @@TODO potentially customisable at a 'per university' level
    """

    description = models.CharField(_('Description'), max_length=255)

    def __str__(self):
        return self.description
