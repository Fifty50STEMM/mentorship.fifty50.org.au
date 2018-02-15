from django.views import generic
from .models import Faq


class FaqView(generic.list.ListView):

    model = Faq

    def get_queryset(self, *args, **kwargs):
        qs = super(FaqView, self).get_queryset(*args, **kwargs)
        qs.filter(is_active=True)
        return qs
