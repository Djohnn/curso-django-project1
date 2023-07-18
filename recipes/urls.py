from django.urls import path

from recipes.views import _base, _contato, home

urlpatterns = [
    path("", view=home),
    path("contato/", view=_contato),
    path("base/", view=_base),
]
