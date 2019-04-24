# coding: utf-8
from django.shortcuts import render,redirect #render関数
from .forms import Daycreateform

def index(request):#renderとrequestはセット
	return render(request,'sns_apps/index.html')#request＋表示

def add(request):
	form = Daycreateform(request.POST or None)

	if request.method == 'POST' and form.is_valid():
		form.save()
		return redirect('sns_apps:index')
	context={
		'form':form
	}
	return render(request,'sns_apps/day_form.html',context)