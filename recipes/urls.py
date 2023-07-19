from django.urls import path

from . import views  # da pasta que estou importa o modulos

# from recipes.views import home # sendo assim não precisamos desse import

urlpatterns = [
    # path("", view=home), usando o import comentado o caminho seria esse.
    path("", views.home),
    path("recipes/<int:id>/", views.recipe),
]
