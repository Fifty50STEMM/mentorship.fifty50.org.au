""" This application contains all the configurable settings for Mentorships as
well as User roles. Fifty50 Organisers will be able to add and change what users
are able in input."""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .validators import validate_uni_id

# @@ TODO this is something that should probably be set at a `University` level.
NUM_MAX_MENTEES = 3

CHOICE_ROLES = (
    ('mentee', 'Mentee'),
    ('mentor', 'Mentor'),
    ('organiser', 'Organiser'),
    ('other', 'Other'),
)

# @@ Could replace `na` with False
CHOICE_RELATIONSHIP_GENDER_MODE = (
    ('0', "Definitely"),
    ('1', 'If possible'),
    ('9', "Unconcerned"),
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

    universities = models.ManyToManyField(
        'universities.University', through='mentorships.UniversitySession')

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

    def __str__(self):
        return self.full_name


@python_2_unicode_compatible
class UniversitySession(models.Model):

    university = models.ForeignKey('universities.University')

    session = models.ForeignKey('mentorships.Session')

    # @@ TODO changing current session should resave all UniversityUser objects
    # to update "current" status for them.
    current = models.BooleanField(default=True)

    def __str__(self):
        return "{session} ({uni})".format(
            session=self.session.abbreviation,
            uni=self.university.abbreviation)

    def save(self, *args, **kwargs):

        # @@TODO write test for this
        if self.current is True:
            for us in UniversitySession.objects.filter(
                    university=self.university):
                us.current = False
            self.current = True
        super(UniversitySession, self).save(*args, **kwargs)


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
        _('Why do you want to become a mentor?'), null=True, blank=True)

    why_diversity = models.TextField(
        _('Why do you think diversity, equity and inclusion in STEM are important?'),  # noqa
        null=True, blank=True)

    hear_about = models.TextField(
        _('How did you hear about this program?'), null=True, blank=True)

    intended_study = models.CharField(
        _('Intended/Preferred Subject Area'), max_length=256, blank=True, default='')

    # @@ TODO probably should be something that can be set by organisers
    mentee_number = models.PositiveSmallIntegerField(
        null=True, default=0, validators=[MinValueValidator(0),
                                          MaxValueValidator(NUM_MAX_MENTEES)],
        help_text="Number of mentees you'd be willing to support (max is {}).".format(
            NUM_MAX_MENTEES)
    )

    gender_mode = models.CharField(
        _('Gender Mode'), blank=True, max_length=16,
        choices=CHOICE_RELATIONSHIP_GENDER_MODE)

    method_preferences = models.ManyToManyField(
        'universities.Method',
        verbose_name=_('What will be your medium of interaction in the program?'))

    degree_major = models.ForeignKey(
        'universities.Program', null=True, blank=True)

    is_current_mentor = models.BooleanField(default=False)

    is_current_mentee = models.BooleanField(default=False)

    # mentors = models.ManyToManyField('mentorships.Relationship',
    #                                  through='Relationship',
    #                                  through_fields=('roup', 'person'),
    #                                  )

    class Meta:
        verbose_name_plural = "university users"
        ordering = ('degree_major',)

    def __str__(self):
        return "{uni}: {user}".format(
            user=self.user.full_name,
            uni=self.university.abbreviation)

    def get_degree_major(self):
        try:
            return self.userdegree_set.filter(major=1)[0]
        except IndexError:
            return None

    def get_degrees_minor(self):
        minor_set = self.userdegree_set.filter(major=0)
        if minor_set:
            return minor_set
        else:
            return None

    def get_current_role_mentor(self):
        return self.userrole_set.filter(university_session__current=True, role='mentor')

    def get_current_role_mentee(self):
        return self.userrole_set.filter(university_session__current=True, role='mentee')

    def get_absolute_url(self):
        return reverse('uuser_detail', kwargs={'slug': self.uni_id})

    def save(self, *args, **kwargs):
        if self.get_degree_major():
            self.degree_major = self.get_degree_major().program
        super(UserUniversity, self).save(*args, **kwargs)


@python_2_unicode_compatible
class UserDegree(models.Model):

    user = models.ForeignKey('mentorships.UserUniversity')

    program = models.ForeignKey('universities.Program')

    study_year = models.ForeignKey('universities.StudyYear')

    major = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ('-major',)

    def __str__(self):
        num = 'major'
        if self.major == 0:
            num = 'minor'
        return "{user} [{num}]: {year} {program}".format(
            num=num, user=self.user.user.full_name,
            program=self.program, year=self.study_year)


@python_2_unicode_compatible
class UserRole(models.Model):
    """ Allow `User` to have a variety of `Role`s per `UniversitySession`.

    All `Role` relationships will be recreated each `UniversitySession`.
    """

    university_session = models.ForeignKey('mentorships.UniversitySession')

    user = models.ForeignKey('mentorships.UserUniversity')

    role = models.CharField(
        _('Role'), blank=True, max_length=16, choices=CHOICE_ROLES)

    is_active = models.BooleanField(default=False)

    relationship = models.ForeignKey(
        'mentorships.Relationship', null=True, blank=True)

    notes = models.CharField(
        _('Notes'), max_length=1024, blank=True, default='',
        help_text="Further information if necessary.")

    class Meta:
        unique_together = ('role', 'relationship')
        ordering = ('university_session', 'is_active',
                    'user__user__gender', 'user__gender_mode')

    def __str__(self):
        active = 'inactive'
        if self.is_active:
            active = 'active'
        return "{user}: {role} {session} [{active}]".format(
            user=self.user.user.full_name, role=self.role, active=active,
            session=self.university_session)


@python_2_unicode_compatible
class Relationship(models.Model):
    """ Allow `User` to have a variety of `Role`s per `UniversitySession`.

    All `Role` relationships will be recreated each `UniversitySession`.
    """

    university_session = models.ForeignKey('mentorships.UniversitySession')

    mentor = models.ForeignKey(
        'mentorships.UserRole', related_name='mentor')

    mentee = models.ForeignKey(
        'mentorships.UserRole', related_name='mentee')

    method = models.ForeignKey('universities.Method')

    class Meta:
        unique_together = ('university_session', 'mentee')

    def __str__(self):
        return "{mentor} => {mentee}".format(mentor=self.mentor, mentee=self.mentee)

    def save(self, *args, **kwargs):
        """ Check to ensure `UserRole`s are available before object save. """
        # @@ TODO write tests for this
        if not self.id:
            new_object = True

        super(Relationship, self).save(*args, **kwargs)
        """Associate new `Relationship` with `UserRole`s.
        ForeignKey on `UserRole` can only be created after `super().save()`
        has been run for this object.
        """
        if new_object:
            self.mentor.relationship = self
            self.mentor.is_active = True
            self.mentor.save()
            self.mentee.relationship = self
            self.mentee.is_active = True
            self.mentee.save()
