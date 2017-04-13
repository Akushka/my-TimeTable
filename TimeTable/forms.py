# -*- coding: utf-8 -*

_autor_ ='macpro'

from django.forms import ModelForm
from .models import TimeTableBase
        
class NewDataIntevalForm(ModelForm):
    class Meta:
        model = TimeTableBase
        #model.beginLesson.label='Your name'
        fields = ['beginLesson','lengthLesson','pauseLesson']
        
                