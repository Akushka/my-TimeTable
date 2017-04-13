from django.shortcuts import render
from .models import DayOfTimeTable, LessonInDay, TimeTableBase
from .forms import NewDataIntevalForm   
import datetime

def TableTime_list(request):
    TimeTable = TimeTableBase.objects.get(pk=1)
    DayTableBases = DayOfTimeTable.objects.all()
    LessonInDays = LessonInDay.objects.all()
    
    form = NewDataIntevalForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            newTime = form.save(commit = False)
            TimeTable.beginLesson = newTime.beginLesson
            TimeTable.lengthLesson = newTime.lengthLesson
            TimeTable.pauseLesson = newTime.pauseLesson
            TimeTable.save()
    else:
        form = NewDataIntevalForm()
       # form.beginLesson.label('00:00')
    
    TimeTable.arrTimeStr = []

#узнаём максималоьное количество уроков на неделе
    count = 0 
    for DayTableBase in DayTableBases:
        #lesson = LessonInDay.objects.filter(lesson_id = DayTableBase.id)
        if len(LessonInDay.objects.filter(lesson_id = DayTableBase.id))>count:
            count = len(LessonInDay.objects.filter(lesson_id = DayTableBase.id))
    
#Длительность урок + перемена        
    totalTime = int(TimeTable.lengthLesson) + int(TimeTable.pauseLesson)
#Начало первого урока (берём из базы)       
    BeginTimeLesson = datetime.datetime.strptime(str(TimeTable.beginLesson)[:5], '%H:%M').strftime('%H:%M')
#В строку через запятую записывем расписание       
    timeStr = ''
    for i in range(count):
        EndTimeLesson = datetime.datetime.strptime(str(BeginTimeLesson), '%H:%M') + datetime.timedelta(minutes=int(TimeTable.lengthLesson)) 
        timeStr = timeStr + (str(BeginTimeLesson)+' - '+str(EndTimeLesson.strftime('%H:%M'))+',')
        BeginTimeLesson = datetime.datetime.strptime(str(BeginTimeLesson), '%H:%M') + datetime.timedelta(minutes=int(totalTime))
        BeginTimeLesson = datetime.datetime.strptime(str(BeginTimeLesson.strftime('%H:%M')), '%H:%M').strftime('%H:%M')
        
#В массив для вывода
    arrLessonTableViz = []
    timeStr = timeStr[:-1].split(',')
    for strTime in timeStr:
        TimeTable.arrTimeStr.append(strTime)
 
    return render(request, 'TimeTable/TableTime_list.html', {'TimeTable':TimeTable, 'DayTableBases':DayTableBases , 'form':form })
    











