from django.urls import path, re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.ProgramFormView.as_view(), name="index"),
    path("downloads", views.ProgramListView.as_view(), name="downloads"),
    path("downloads/<str:channel>/<str:efirweek>/", views.download_file, name="download_file"),
]
# url 'download_file' program.channel program.efirweek
# path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),