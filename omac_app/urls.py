from django.urls import path

from omac_app.views import TypeView, BreedView

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

]
