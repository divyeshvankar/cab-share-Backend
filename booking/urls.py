from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import BookViewSet

router = DefaultRouter()

urlpatterns = [
    path(r'', include(router.urls)),
    path('book/', BookViewSet.as_view(), name="book"),
]
