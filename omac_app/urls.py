from django.urls import path

from omac_app.views import TypeView, BreedView, AnimalView

urlpatterns = [
    path(
        "omac/type",
        TypeView.as_view({'get': 'list', 'post': 'create', 'put': 'update'}),
        name="type",
    ),
    path('omac/type/<int:pk>/', TypeView.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),



    path(
        "omac/breed",
        BreedView.as_view({'get': 'list', 'post': 'create', 'put': 'update'}),
        name="breed",
    ),
    path('omac/breed/<int:pk>/', BreedView.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),



    path(
        "omac/animal",
        AnimalView.as_view({'get': 'list', 'post': 'create', 'put': 'update'}),
        name="animal",
    ),
    path('omac/animal/<int:pk>/', AnimalView.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),
]
