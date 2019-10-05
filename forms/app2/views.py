from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from app2.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def contactus(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = request.POST.get('contact_name')
        email = request.POST.get('contact_email')
        number = request.POST.get('contact_number')
        content = request.POST.get('contact_content')
        subject = 'Important Message please check your inbox'
        message = 'hello i am soumya ranjan rao would like to say you that i have created the django forms'
        from_mail = settings.EMAIL_HOST_USER
        to_list = [email,from_mail]
        send_mail(subject,message,from_mail,to_list,fail_silently=False)
        return HttpResponseRedirect('thankyou')
    return render(request,'contactus.html',{'form':form})

def thankyou(request):
    return render(request,'/thankyou.html')
