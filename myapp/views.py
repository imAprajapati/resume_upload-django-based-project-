import imp
from django.shortcuts import render,HttpResponseRedirect
from .forms import ResumeForm
from django.views import View
from .models import Resume
# Create your views here.

class Homeview(View):
    def get(self,request):
        fm=ResumeForm()
        condidates=Resume.objects.all()
        return render(request,'home.html',{'condidates':condidates,'form':fm})


    def post(self,request):
        fm=ResumeForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')

class CondidateView(View):
    def get(self,request,id):
        data=Resume.objects.get(pk=id)
        return render(request,'condidate.html',{'condidate':data})

class Deletecondidate(View):
    def get(self,request,id):
        data=Resume.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')


