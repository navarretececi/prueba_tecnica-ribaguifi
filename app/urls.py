from django.views.generic.base import TemplateView
from django.urls import path

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('page-2', TemplateView.as_view(template_name='page2.html')),
    path('page-3', TemplateView.as_view(template_name='page3.html')),
]