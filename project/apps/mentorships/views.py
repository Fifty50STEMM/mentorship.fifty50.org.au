from django.urls import reverse_lazy
from django.views.generic import edit, detail
from django.http import HttpResponseRedirect

from .forms import SignupForm
from .models import UserUniversity

from project.users.models import User


class UserUniversityDetailView(detail.DetailView):

    model = UserUniversity
    slug_field = 'uni_id'
    template_name = 'mentorships/uuser_detail.html'


class UserUniversityCreateView(edit.CreateView):

    model = UserUniversity
    form_class = SignupForm
    template_name = 'mentorships/uuser_create.html'

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        user = User.objects.filter(email=self.request.POST.get('email'))

        print(" ** ", self.request.POST['uni_id'])

        if not user:
            user = User.objects.create_user(
                username=self.request.POST['uni_id'],
                email=self.request.POST['email']
            )
            user.save()
        else:
            user = user[0]
        form.instance.user = user

        if form.is_valid():
            user.preferred_name = form.cleaned_data['preferred_name']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.gender = form.cleaned_data['gender']
            user.save()
            form.instance.user = user

            # @@ TODO: mentee number conceal/show
            # @@ TODO: validation if mentee & mentee number is 0

            form.instance.save()
            return HttpResponseRedirect(
                reverse_lazy('uuser_detail', kwargs={'slug': form.instance.uni_id}))
        else:
            return super().post(request, *args, **kwargs)
