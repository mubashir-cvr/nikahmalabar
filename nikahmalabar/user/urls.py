from django.db import router
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'user'



router = DefaultRouter()
router.register("properties",views.UserPropertiesViewSet)
router.register("Bproperties",views.UserEducationLocationContactViewSet)
router.register("collectproperties",views.UserPropertiesAll)



urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('test_auth/',views.TestAuthView.as_view(),name='testauth'),
    path('header_load/',views.LoadHeaderView.as_view(),name='header_load'),
    path('',include(router.urls)),

]