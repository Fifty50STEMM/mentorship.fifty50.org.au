from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, HTML, ButtonHolder, Submit


from .models import UserUniversity, CHOICE_ROLES
from project.apps.universities.models import University, Program, StudyYear
from project.users.models import CHOICE_GENDER


class SignupForm(forms.ModelForm):

    university = forms.ModelChoiceField(
        queryset=University.objects.all(),  # is_active=True),
        initial=University.objects.first(),
    )

    email = forms.EmailField()

    gender = forms.CharField(
        label="I identify as", required=False,
        widget=forms.Select(choices=CHOICE_GENDER))

    roles = forms.MultipleChoiceField(
        choices=CHOICE_ROLES,
        widget=forms.CheckboxSelectMultiple(),
        initial="mentee",
        label="What roles would you like to have in Fify50 this semester?",
        help_text="If you're unsure select: Mentee"
    )

    first_name = forms.CharField()
    last_name = forms.CharField()
    preferred_name = forms.CharField(required=False)

    interests = forms.CharField(
        required=False,
        help_text="Briefly list any interests that might help in setting you up in a good mentor-mentee relationship (limit 500 chars).")  # noqa

    degree_1 = forms.ModelChoiceField(
        queryset=Program.objects.filter(is_STEMM=True, is_active=True),
        help_text="Must be STEMM course.")
    degree_1_year = forms.ModelChoiceField(
        queryset=StudyYear.objects.all())

    degree_2 = forms.ModelChoiceField(
        queryset=Program.objects.filter(is_active=True), required=False)
    degree_2_year = forms.ModelChoiceField(
        queryset=StudyYear.objects.all(), required=False)

    class Meta:
        model = UserUniversity
        fields = ['university', 'uni_id',  'why_mentor', 'why_diversity', 'hear_about',
                  'mentee_number', 'gender_mode',  'method_preferences']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Signup for Fifty50',
                Field('roles'),
                Field('mentee_number'),
                Field('first_name',),
                Field('last_name',),
                Field('university', readonly=True),
                Field('uni_id',),
                Field('email',),
                Field('preferred_name',),
                Field('interests',),
                Field('method_preferences'),
                Field('gender_mode'),
                Field('gender', required=False),
            ),

            Fieldset(
                'What are you Studying?',
                Field('degree_1',),
                Field('degree_1_year',),
            ),
            Fieldset(
                '2nd Degree?',
                Field('degree_2',),
                Field('degree_2_year',),
            ),
            Fieldset(
                'Let us know about your interest in making STEMM more diverse:',
                Field('why_mentor',),
                Field('why_diversity',),
                Field('hear_about',),
            ),
            ButtonHolder(
                Submit('submit', 'Join now')
            )
        )
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['university'].widget.attrs['readonly'] = True
        self.fields['why_mentor'].widget.attrs['rows'] = 3
        self.fields['why_diversity'].widget.attrs['rows'] = 3
        self.fields['hear_about'].widget.attrs['rows'] = 3
        self.fields['why_mentor'].required = False
        self.fields['why_diversity'].required = False
        self.fields['hear_about'].required = False

        self.fields['method_preferences'].widget.attrs['style'] = "height:3.5em"
        self.fields['mentee_number'].widget.attrs['style'] = "width: 4em"
        self.fields['gender_mode'].label = "Would you prefer a mentee/mentor that is the same gender as you?"
