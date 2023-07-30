from django.shortcuts import render
import datetime
now = datetime.datetime.now()
# Create your views here.

def index(request):
    return render(request, 'ismyBirthday/index.html', {
        'ismyBirthday': now.day == 7 and now.month == 4
    })

def index_p(request):
    return render(request, 'ismyBirthday/index.html', {
        'ismyBirthday': now.day == 6 and now.month == 9
    })

def index_t(request):
    return render(request, 'ismyBirthday/index.html', {
        'ismyBirthday': True
    })
