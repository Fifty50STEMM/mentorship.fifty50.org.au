""" This application contains all the configurable settings for Mentorships as
well as User roles. Fifty50 Organisers will be able to add and change what users
are able in input."""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .validators import validate_uni_id


NUM_MAX_MENTEES = 3

CHOICE_ROLES = (
    ('mentee', 'Mentee'),
    ('mentor', 'Mentor'),
    ('organiser', 'Organiser'),
    ('other', 'Other'),
)

# @@ Could replace `na` with False
CHOICE_RELATIONSHIP_GENDER_MODE = (
    ('strict', "It IS important to me to be matched to the same gender."),
    ('optional', 'If possible, match me to the same gender but not essential.'),
    ('na', "It IS NOT important to me which gender I am matched with."),
)


# Reference Models
# ------------------------------------------------------------------------------


@python_2_unicode_compatible
class Session(models.Model):
    """ Describe the Fifty50 'intake'. """

    year = models.PositiveSmallIntegerField(_('Year'), )

    order_in_year = models.PositiveSmallIntegerField(_('Order in Year'))

    reference = models.CharField(
        _('Reference'), max_length=255,
        help_text="Human readable version of session, eg 'Semester 1, 2018'")  # noqa

    abbreviation = models.CharField(
        _('Abbreviation'), unique=True, blank=True, max_length=32)

    def __str__(self):
        return self.abbreviation


class SessionWeek(models.Model):
    """ The template outlining what weeks there will be and what
    can happen during that week.

    Also can be used as a reference for relationship ratings.

    @@TODO decent UI will be necessary for organisers to understand
    what's going on here.

    @@TODO should another model be made so this can vary session to session?

    @@TODO potentially customisable at a 'per university' level
    """
    week = models.CharField(_('Week (number)'), unique=True, max_length=3)

    description = models.CharField(_('Full Name'), max_length=255)

    information = models.TextField(_('Information'), blank=True)

    # @@TODO perhaps file upload here.


@python_2_unicode_compatible
class UniversitySession(models.Model):

    university = models.ForeignKey('universities.University')

    session = models.ForeignKey('mentorships.Session')

    def __str__(self):
        return "{session} ({uni})".format(
            session=self.session.abbreviation,
            uni=self.university.abbreviation)


# Primary Function Models
# ------------------------------------------------------------------------------
# The following models are the essential purpose of the application for which
# all of the other objects play a support role.


@python_2_unicode_compatible
class UserUniversity(models.Model):
    """ Allow `User` to be associated with multiple `University` objects.

    On registration `User` is associated with `University`

    @@Note: not associated with department, would we want/not want to do this?
    @@Note: multitenancy or using sites is probably a bad idea for this project,
    this implementation is probably good.
    """

    user = models.ForeignKey('users.User')

    university = models.ForeignKey('universities.University')

    uni_id = models.CharField(
        _('University ID'), max_length=64, unique=True, validators=[validate_uni_id])

    # General information about this `User` experience at this `University`
    # -------------------------------------------------------------------------

    # @@ TODO probably should be method of organisers managing these questions
    # storing for for this first version is fine though.
    why_mentor = models.TextField(
        _('Why do you want to become a mentor?'), null=True)

    why_diversity = models.TextField(
        _('Why do you think diversity, equity and inclusion in STEM are important?'),  # noqa
        null=True)

    hear_about = models.TextField(
        _('How did you hear about this program?'), null=True)

    # @@ TODO probably should be something that can be set by organisers
    mentee_number = models.PositiveSmallIntegerField(
        null=True, default=0, validators=[MinValueValidator(0),
                                          MaxValueValidator(NUM_MAX_MENTEES)],
        help_text="Number of mentees you'd be willing to support (max is {}).".format(
            NUM_MAX_MENTEES)
    )

    gender_mode = models.CharField(
        _('Gender Mode'), blank=True, max_length=16,
        choices=CHOICE_RELATIONSHIP_GENDER_MODE,
        help_text="Note that if you would like to be matched to the same gender, you must select an option from the following field."  # noqa
    )

    method_preferences = models.ManyToManyField('universities.Method')

    class Meta:
        verbose_name_plural = "university users"

    def get_absolute_url(self):
        return reverse('uuser_detail', kwargs={'slug': self.uni_id})

    def __str__(self):
        return "{uni}: {user}".format(
            user=self.user.full_name,
            uni=self.university.abbreviation)


@python_2_unicode_compatible
class UserDegree(models.Model):

    user = models.ForeignKey('mentorships.UserUniversity')

    program = models.ForeignKey('universities.Program')

    study_year = models.ForeignKey('universities.StudyYear')

    def __str__(self):
        return "{uni}: {user}".format(
            user=self.user.user.full_name,
            uni=self.university.abbreviation)


@python_2_unicode_compatible
class UserRole(models.Model):
    """ Allow `User` to have a variety of `Role`s per `UniversitySession`.

    All `Role` relationships will be recreated each `UniversitySession`.
    """

    university_session = models.ForeignKey('mentorships.UniversitySession')

    user = models.ForeignKey('users.User')

    role = models.CharField(
        _('Role'), blank=True, max_length=16, choices=CHOICE_ROLES)

    def __str__(self):
        return "{user}: {role}".format(
            user=self.user.user.full_name, uni=self.role)


@python_2_unicode_compatible
class Relationship(models.Model):
    """ Allow `User` to have a variety of `Role`s per `UniversitySession`.

    All `Role` relationships will be recreated each `UniversitySession`.
    """

    university_session = models.ForeignKey('mentorships.UniversitySession')

    mentor = models.ForeignKey('users.User', related_name='mentor')

    mentee = models.ForeignKey('users.User', related_name='mentee')

    method = models.ForeignKey('universities.Method')

    class Meta:
        unique_together = ('university_session', 'mentee')

    def __str__(self):
        return "{mentor} => {mentee}".format(
            session=self.session.abbreviation,
            uni=self.university.abbreviation)
