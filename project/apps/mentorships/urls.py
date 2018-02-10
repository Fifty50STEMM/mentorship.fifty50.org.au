from django.conf.urls import url

from . import views


urlpatterns = [
    url(r"^signup/$",
        views.UserUniversityCreateView.as_view(), name='account_signup'),

    url(r"^match/$",
        views.UserRoleMatchView.as_view(), name='uuser_match'),

    # @@TODO ANU specific slug
    url(r"^ANU/(?P<slug>[us0-9]+)/$",
        views.UserUniversityDetailView.as_view(), name='uuser_detail'),

]
