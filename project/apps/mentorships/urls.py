from django.conf.urls import url

from .views import (UserUniversityCreateView, UserUniversityDetailView)


urlpatterns = [
    url(r"^signup/$",
        UserUniversityCreateView.as_view(), name='account_signup'),

    # @@TODO ANU specific slug
    url(r"^ANU/(?P<slug>[us0-9]+)/$",
        UserUniversityDetailView.as_view(), name='uuser_detail'),
]
