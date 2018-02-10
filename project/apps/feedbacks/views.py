from django import forms
from django.views.generic import edit
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit

from .models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['message', 'name', 'email']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Send Feedback',
                'message',
                'name',
                'email',
                Submit('submit', 'Send feedback')
            )
        )
        super(FeedbackForm, self).__init__(*args, **kwargs)


class FeedbackCreateView(edit.CreateView):

    model = Feedback
    form_class = FeedbackForm
