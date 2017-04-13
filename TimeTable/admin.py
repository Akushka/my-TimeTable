from django.contrib import admin
from .models import DayOfTimeTable, TimeTableBase, LessonInDay

class LessonInDay(admin.TabularInline):
    model = LessonInDay
   # fields = ['nameLesson']
    extra = 1
       
class LessonAdmin(admin.ModelAdmin):
    fields = ('day',)
    inlines = [LessonInDay]
    
    
admin.site.register(DayOfTimeTable, LessonAdmin)
admin.site.register(TimeTableBase)

