
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("v1/", include(("omac_app.urls", "v1"), namespace="v1")),
]
