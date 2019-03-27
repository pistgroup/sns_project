from django.shortcuts import render #render関数

def index(request):#renderとrequestはセット
	return render(request,'sns_apps/index.html')#request＋表示先

