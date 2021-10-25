from django.http import response
from django.http.response import Http404, HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from collections import namedtuple
from rest_framework import generics,viewsets, mixins
from user import models
from user.models import User, UserProperties,UserEducationLocationContact,Image
from .serializers import UserPropertiesSerializer, UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken,APIView
from rest_framework.settings import api_settings
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q
import user
# from. import models


 # Create your views here.
 
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserPropertiesViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializers.UserPropertiesSerializer
    queryset = UserProperties.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)

class UserEducationLocationContactViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializers.UserEducationLocationContactSerializer
    queryset = UserEducationLocationContact.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)

class TestAuthView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class =serializers.UserSerializer
    
    def get(self,request,format=None):
        

        email= str(self.request.user.email)
        return HttpResponse(email)
    
class LoadHeaderView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class =serializers.UserSerializer
    
    def get(self,request,format=None):
        image = Image.objects.filter(user=self.request.user).first()
        user = UserProperties.objects.filter(user=self.request.user).first()
        nameUser = str(user.name)
        imageUrl=str(image.image.url)
        return HttpResponse(nameUser +','+imageUrl)


# UserAllData = namedtuple('UserAllData', ('userproperties', 'usereducation'))
# class UserAllViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing the Tweets and Articles in your Timeline.
#     """
#     def list(self, request):
#         userdata = UserAllData(
#             userproperties=models.UserProperties.objects.all(),
#             usereducation=models.UserEducationLocationContact.objects.all(),
#         )
#         serializer =serializers.UserCollectionSerializer(userdata)
#         return serializer.data

class UserPropertiesAll(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializers.UserAllserializer
    queryset = models.Image.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        user = models.UserProperties.objects.get(user=self.request.user)
        gender ='female'
        if user.gender=='female':
            gender='male'
            
        return self.queryset.filter(profile__gender = gender)
    
    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)
    
    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'retrieve':
            # raise Http404 if user has no subscription
            return serializers.UserAllserializerDetailled

        return self.serializer_class
    