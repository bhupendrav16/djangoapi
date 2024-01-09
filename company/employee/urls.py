
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from employee.views import CompanyViewSet,StudentViewSet
router= routers.DefaultRouter()

router.register(f"companies", CompanyViewSet)
router.register(f"student",StudentViewSet )

urlpatterns = [
    path("",include(router.urls))

]
