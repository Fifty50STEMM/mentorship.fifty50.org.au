from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic


from .forms import SignupForm
from .models import UserUniversity, UserRole, UniversitySession, UserDegree, Relationship
from project.apps.universities.models import Method

from project.users.models import User


class UserUniversityDetailView(generic.detail.DetailView):

    model = UserUniversity
    slug_field = 'uni_id'
    template_name = 'mentorships/uuser_detail.html'


class UserUniversityCreateView(SuccessMessageMixin, generic.edit.CreateView):

    model = UserUniversity
    form_class = SignupForm
    template_name = 'mentorships/uuser_create.html'
    success_message = "Thank you! You have signed up as: %(first_name) %(last_name) [%(uni_id)]"

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
            user.interests = form.cleaned_data['interests']
            user.save()
            form.instance.user = user

            # @@ TODO: mentee number conceal/show
            # @@ TODO: validation if mentee & mentee number is 0

            form.instance.save()

            uuser = form.instance

            uuser.method_preferences.set(
                form.cleaned_data['method_preferences'])

            for role in form.cleaned_data['roles']:
                usession = UniversitySession.objects.get(
                    university=form.cleaned_data['university'],
                    current=True
                )
                n = 1
                if role == 'mentor':
                    n = form.cleaned_data['mentee_number']

                # create multiple mentor "roles" if mentee_number > 1
                for i in range(0, n):
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


class UserRoleMatchView(SuccessMessageMixin, generic.TemplateView):

    template_name = 'mentorships/uuser_match.html'
    success_message = 'Saved.'

    # @@ TODO differentiate sessions using URL params/current session

    def post(self, request, *args, **kwargs):
        # super(UserRoleMatchView, self).post(request, *args, **kwargs)
        context = self.get_context_data(**kwargs)
        for key in request.POST:
            if request.POST[key]:
                if key[:6] == "mentor":
                    mentor = UserRole.objects.get(pk=key.split("-")[1])
                    mentee = UserRole.objects.get(pk=request.POST[key])
                    new_relationship = Relationship(
                        mentor=mentor,
                        mentee=mentee,
                        university_session=UniversitySession.objects.get(
                            current=True),
                        method=Method.objects.first())
                    try:
                        new_relationship.save()
                    except IntegrityError:
                        messages.warning(request, 'User previously matched.')
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(UserRoleMatchView, self).get_context_data(**kwargs)
        context['mentors'] = UserRole.objects.filter(
            role='mentor', relationship__isnull=True)
        context['mentees'] = UserRole.objects.filter(
            role='mentee', relationship__isnull=True)
        context['matched'] = Relationship.objects.filter(university_session__current=True)
        return context
