from django.db import models
import json

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.http.response import JsonResponse
from versatileimagefield.fields import VersatileImageField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create Save a User"""
        if not email:
            raise ValueError('User must have a Email')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if user:
            return user

    def create_superuser(self, email, password):
        """Create and Save a super User"""
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self.db)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """"Custom Model"""
    email = models.EmailField(max_length=225, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    
class UserProperties(models.Model):

    GENDER_CHOICES = (('male', 'Male'),('female', 'Female'),('other', 'Other'))
    profileCreated_CHOICES = (('self','Self'),('parent','Parent'),('brother','Brother'),('sister','Sister'))
    martialStatus_CHOICES = (('single','Single'),('divorced','Divorced'),)
    bodyType_CHOICES = (('slim','Slim'),('muscular','Muscular'),('fat',('Fat')))
    """User Properties"""
    user = models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
    profileCreated =models.CharField(max_length=225,choices=profileCreated_CHOICES,default="self")
    name = models.CharField(max_length=225)
    gender = models.CharField(max_length=225,choices=GENDER_CHOICES,default="male")
    community = models.CharField(max_length=225)
    moblie = models.CharField(max_length=225)
    preferredProfile = models.CharField(max_length=225)
    dateOfBirth = models.DateField()
    relegion = models.CharField(max_length=225)
    nationality = models.CharField(max_length=225)
    height = models.CharField(max_length=225) 
    weight = models.CharField(max_length=225) 
    martialStatus = models.CharField(max_length=225,choices=martialStatus_CHOICES,default="single") 
    complexion = models.CharField(max_length=225) 
    ethnicGroup = models.CharField(max_length=225) 
    bodyType = models.CharField(max_length=225,choices=bodyType_CHOICES,default="slim") 
    physicalStatus = models.CharField(max_length=225)
    motherTongue = models.CharField(max_length=225)

    class Meta:
        verbose_name_plural = ('UserProperties')
       
    def __str__(self):
        return str(self.name)



class UserEducationLocationContact(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
    highestEducation = models.CharField(max_length=225)
    profession = models.CharField(max_length=225)
    professionType = models.CharField(max_length=225)

    nativeCountry = models.CharField(max_length=225)
    nativeState = models.CharField(max_length=225)
    nativeCity = models.CharField(max_length=225)

    primaryNumber = models.CharField(max_length=225)
    secondaryNumber = models.CharField(max_length=225)
    preferedContact = models.CharField(max_length=225)
    relation = models.CharField(max_length=225)
    describe = models.TextField


    def __str__(self):
        return str(self.highestEducation)




    def __str__(self):
        return str(self.user)


   

class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = VersatileImageField('Profile',blank=True,null=True,upload_to="Profile/")
    profile= models.ForeignKey(UserProperties,on_delete=models.CASCADE)
    education= models.ForeignKey(UserEducationLocationContact,on_delete=models.CASCADE)