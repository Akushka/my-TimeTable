from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime

# Create your models here.

class DayOfTimeTable(models.Model):
    class Meta():
        db_table = 'DayOfTimeTable'
    day = models.CharField(max_length=15,verbose_name = "День недели")
    def __str__(self):
        return self.day

class LessonInDay(models.Model):
    class Meta():
        db_table = 'LessonInDay'
    lesson_id = models.ForeignKey(DayOfTimeTable)    
    nameLesson = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nameLesson 

class TimeTableBase(models.Model):
    class Meta():
        db_table = 'TimeTableBase'
    beginLesson = models.CharField(max_length=20)
    lengthLesson = models.CharField(max_length=20) 
    pauseLesson = models.CharField(max_length=20)
    arrTimeStr = []
     

