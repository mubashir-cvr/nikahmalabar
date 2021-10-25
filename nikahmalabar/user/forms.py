from django import forms
from django.db.models import fields
from django.forms.models import fields_for_model
from django.utils.translation import ugettext_lazy as _
from .models import Image, UserProperties
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput



class UserPropertiesForm(forms.ModelForm):
    class Meta:
        model = UserProperties
        fields = '__all__' 
        widgets = { 
            'profileCreated': Select(attrs={'id':'profileCreated','name':'profileCreated','class': 'required form-control'}),
            'gender': Select(attrs={'name':'gender','id':'gender','class': 'required form-control'}),
            'martialStatus': Select(attrs={'id':'martialStatus','name':'martialStatus','class': 'required form-control'}),
            'bodyType': Select(attrs={'id':'bodyType','name':'bodyType','class': 'required form-control'}),
            'nationality': TextInput(attrs={'id':'nationality','name':'nationality','class': 'required form-control'}),
            'motherTongue': TextInput(attrs={'id':'motherTongue','name':'motherTongue','class': 'form-control','placeholder':'Mother tongue'}),
        }

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = '__all__'
#         widgets = { 
#                'image': FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
#             #    'user': Select(attrs={'class': 'form-control', 'value':request.user.id }),
#         }
