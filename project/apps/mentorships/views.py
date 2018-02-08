from django.urls import reverse_lazy
from django.views.generic import edit, detail
from django.http import HttpResponseRedirect

from .forms import SignupForm
from .models import UserUniversity, UserRole, UniversitySession, UserDegree

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

            uuser = form.instance

            for role in form.cleaned_data['roles']:
                usession = UniversitySession.objects.get(
                    university=form.cleaned_data['university'],
                    current=True
                )
                new_role = UserRole(
                    university_session=usession,
                    user=uuser,
                    role=role
                )
                new_role.save()

            new_degree1 = UserDegree(
                user=uuser,
                program=form.cleaned_data['degree_1'],
                study_year=form.cleaned_data['degree_1_year'],
                major=1,
            )
            new_degree1.save()

            if form.cleaned_data['degree_2']:
                new_degree2 = UserDegree(
                    user=uuser,
                    program=form.cleaned_data['degree_2'],
                    study_year=form.cleaned_data['degree_2_year'],
                    major=2,
                )
                new_degree2.save()

            return HttpResponseRedirect(
                reverse_lazy('uuser_detail', kwargs={'slug': form.instance.uni_id}))
        else:
            return super().post(request, *args, **kwargs)
