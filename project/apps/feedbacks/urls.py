from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views


urlpatterns = [
    url(r"$", views.FeedbackCreateView.as_view(), name='feedback_form'),

    url(r'^thanks/$', TemplateView.as_view(template_name='feedbacks/feedback_thanks.html'),
        name='feedback_success'),

]
