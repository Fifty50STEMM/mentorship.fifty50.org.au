from django.views.generic import edit
from django.http import HttpResponse
from django.views import View

from .forms import SignupForm
from .models import UserUniversity


class UserUniversityCreateView(edit.CreateView):

    model = UserUniversity
    form_class = SignupForm
    template_name = 'mentorships/profile_create.html'
