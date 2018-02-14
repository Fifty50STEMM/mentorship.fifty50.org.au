from django.views import generic
from django.utils import timezone
from .models import Post




class PostListView(generic.list.ListView):

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now())


class PostDetailView(generic.detail.DetailView):

    model = Post
