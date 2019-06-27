from django.shortcuts import render
from django.http import HttpResponse
from .form import studentForm

def register_db(request):
	#import pudb; pudb.set_trace()
	if request.method=='POST':
		form = studentForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data['name']
			last_name = form.cleaned_data['last_name']
			print(name,last_name)
			return render(request, 'login/index.html')		
	else:
		form = studentForm()
		return render(request,'register/index.html',{'form':form})