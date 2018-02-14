from django.views import generic
from django.utils import timezone
from .models import Post


class PostMixin(object):

    model = Post

    def get_queryset(self):
        posts = super(PostMixin, self).get_queryset()

        # @@ TODO better practice to use queryset manager on model, have `active()` method, per
        # https://docs.djangoproject.com/en/2.0/topics/db/managers/#creating-a-manager-with-queryset-methods
        # The following applies to both ListView and DetailView though.

        posts = posts.filter(
            publish_date__lte=timezone.now(), is_active=True)

        if self.request.user.is_anonymous():
            posts = posts.filter(is_public=True)

        return posts


class PostListView(PostMixin, generic.list.ListView):

    pass


class PostDetailView(PostMixin, generic.detail.DetailView):

    pass
