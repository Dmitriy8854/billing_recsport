from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import OrderViewSet
from . import views

app_name = "services"

router = DefaultRouter()
router.register("order", OrderViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("index/", views.index, name="index"),
]
