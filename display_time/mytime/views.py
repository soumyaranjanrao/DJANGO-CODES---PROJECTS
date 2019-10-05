from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    str = datetime.datetime.now()
    return render(request,'index.html',{'c_time':str})

def f_time(request,x):
    str = datetime.datetime.now()+datetime.timedelta(hours=x)
    return render(request,'f_time.html',{'hours':x, 'f_time':str})