from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors', views.ListAllDirectors.as_view()),
    path('directors/<int:pk>', views.DetailOneDirector.as_view(), name='director-detail'),
    path('actors', views.ListAllActors.as_view()),
    path('actors/<slug:slug>', views.DetailOneActor.as_view(), name='actor-detail'),
]
