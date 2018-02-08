from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, HTML, ButtonHolder, Submit


from .models import UserUniversity, CHOICE_ROLES
from project.apps.universities.models import University
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
        initial="mentee",
        label="What roles would you like to have in Fify50 this semester?",
        help_text="If you're unsure select: Mentee"
    )

    preferred_name = forms.CharField(
        help_text="The name you prefer to be refered to as, eg 'Emily', 'Alex'.")

    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = UserUniversity
        fields = ['university', 'uni_id',  'why_mentor', 'why_diversity', 'hear_about',
                  'mentee_number', 'gender_mode',  'method_preferences']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Signup for Fifty50',
                Field('university', readonly=True),
                Field('uni_id',),
                Field('email',),
                Field('first_name',),
                Field('last_name',),
                Field('preferred_name',),
                Field('gender_mode'),
                Field('gender', required=False),
            ),
            Fieldset(
                'Are you a "Mentor" or a "Mentee"?',
                HTML(
                    """<small class="text-muted">Or both, or something else ...</small>"""),
                Field('roles'),
                Field('method_preferences'),
                Field('mentee_number',),
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
        self.fields['method_preferences'].widget.attrs['style'] = "height:3.5em"
        self.fields['mentee_number'].widget.attrs['style'] = "width: 4em"
        self.fields['gender_mode'].label = ""
