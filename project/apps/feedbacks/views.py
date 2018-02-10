from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit
from django import forms
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import edit

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


class FeedbackCreateView(SuccessMessageMixin, edit.CreateView):

    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback_success')
    success_message = "Thank you! Your message was sent."
