from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
# Create your views here.


class PrerakRedirectview(RedirectView):
    # url='https://www.instagram.com/'
    pattern_name='redirect'
    def get_redirect_url(self, *args: Any, **kwargs: Any):
        print(kwargs)
        return super().get_redirect_url(*args, **kwargs)