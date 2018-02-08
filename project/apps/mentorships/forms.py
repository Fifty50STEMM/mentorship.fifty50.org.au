from django import forms

from .models import UserUniversity


class SignupForm(forms.ModelForm):

    class Meta:
        model = UserUniversity
        fields = ['university', 'uni_id', 'why_mentor', 'why_diversity',
                  'hear_about', 'mentee_number', 'gender_mode',  'method_preferences']
