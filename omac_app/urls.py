from django.urls import path

from omac_app.views import TypeView

urlpatterns = [
    path(
        "omac/type",
        TypeView.as_view({'get': 'list', 'post': 'create', 'put': 'update'}),
        name="type",
    ),
    path('omac/type/<int:pk>/', TypeView.as_view({'put': 'update', 'delete': 'destroy'})),
]
