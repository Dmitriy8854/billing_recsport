from rest_framework.routers import DefaultRouter

from django.urls import include, path

from cats.views import OrderViewSet


router = DefaultRouter()
router.register("order", OrderViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
