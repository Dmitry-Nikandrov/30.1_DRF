from django.contrib import admin
from django.urls import include, path

from materials.urls import app_name

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("materials.urls", namespace=app_name)),
]
