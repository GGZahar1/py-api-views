from django.urls import path, include
from rest_framework import routers

from cinema.views import (MovieViewSet, CinemaHallViewSet, ActorListView,
                          ActorDetailView, GenreListView, GenreDetailView)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinema_halls = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)

cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

urlpatterns = [
    path("", include(router.urls)),
    path("cinema_halls/", cinema_halls),
    path("cinema_halls/<int:ok>/", cinema_hall_detail),
    path("actors/", ActorListView.as_view()),
    path("actors/<int:pk>/", ActorDetailView.as_view()),
    path("genres/", GenreListView.as_view()),
    path("genres/<int:pk>/", GenreDetailView.as_view()),
]

app_name = "cinema"
