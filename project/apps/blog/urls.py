from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$',
        views.PostListView.as_view(), name='post_list'),

    url(r'^post/(?P<slug>[-\w]+)/$',
        views.PostDetailView.as_view(), name='post_detail'),
]
