from django import views
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import CustomerAPIView, Studentviewset
from .views import Marksviewset
from .views import Studentview
from .views import Contactviewset

router = routers.DefaultRouter()
router.register("student", Studentviewset)
router.register("Marks", Marksviewset)
router.register("Contact", Contactviewset)

urlpatterns = [
    path("", include(router.urls)),
    path("test/", Studentview.as_view()),
    path("admin/", admin.site.urls),
    path('customer/',CustomerAPIView.as_view()),
    path('customer/<int:cus_id>',CustomerAPIView.as_view())
]
