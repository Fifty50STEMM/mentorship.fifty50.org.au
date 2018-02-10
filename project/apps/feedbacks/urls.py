from django.conf.urls import url

from . import views


urlpatterns = [
    url(r"$", views.FeedbackCreateView.as_view(), name='feedback_form'),
]
