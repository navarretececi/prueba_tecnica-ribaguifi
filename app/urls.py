from django.views.generic.base import TemplateView
from django.urls import path

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('2', TemplateView.as_view(template_name='index2.html'))
]