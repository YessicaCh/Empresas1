from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .form import loginForm
from apps.user.models import Student2, Mentor, User, Courses_Student, Course, Students_Mentor
from django.contrib import messages

mem_glob = Mentor()
sm_glob = Students_Mentor()
studiamt = Student2()

def setMem(mem):
	mem_glob = mem

def login(request):	
	if request.method == 'POST':		
		form = loginForm(request.POST)
		#user = authenticate(username=form.fields['nick_name'], password=form.fields['password'])
		username = request.POST.get('nick_name')
		password = request.POST.get('password')
		global studiamt
		global sm_glob
		global mem_glob
		print("oksoks!!!!!!!!!!!!!!!!!!!!!!!", username)
		try:
			stu = User.objects.get(Q(nick_name=username) & Q(password=password))
			if stu.Student_Mentor == True:
				stu = Student2.objects.get(Q(nick_name=username) & Q(password=password))
				sm = Students_Mentor.objects.get(Q(studentA=stu.id) | Q(studentB=stu.id))
				cursos = Courses_Student.objects.filter(Q(student2=stu.id))
								
				studiamt = stu				
				sm_glob = sm

				print(cursos[1].course.name)				
				return render(request, 'contentuser/index.html', {'stu': stu, 'cursos': cursos})
				#return render(request, 'contentuser/userimdex.html', {'stu': stu, 'sm': sm})
			else:
				mem = Mentor.objects.get(Q(nick_name=username) & Q(password=password))
				sm = Students_Mentor.objects.get(Q(mentor=mem.id))
				cursos = Courses_Student.objects.filter(Q(student2=sm.id))
				
				mem_glob = mem
				sm_glob = sm				
				print('wii ',len(cursos))
				################################

				return render(request, 'contentuser/memdex.html', {'mentor': mem, 'cursos': cursos})
				#return render(request, 'contentuser/imdex.html', {'stu': mem, 'sm': sm})
			
		except Student2.DoesNotExist or Mentor.DoesNotExist:
			print('!!!!!!!--***********no estas en la bd')
			messages.warning(request, ' nickname or password does not exist')
			return redirect('login')
	else:
		form = loginForm()
		return render(request, 'login/index.html', {'form': form})

    #return HttpResponse("Index")


def contentuseruser(request):  # of Studiant
	if request.method == 'GET':
		print('contentuser GET')
		#print(mem_glob)
		return render(request, 'contentuser/userimdex.html', {'stu': studiamt, 'sm': sm_glob})
	else:
		print('contentuser POST')
		return render(request, 'contentuser/userimdex.html', {'stu': studiamt, 'sm': sm_glob})


def contentuser(request):  # Of mentor
	if request.method == 'GET':
		print('contentuser GET')
		print(mem_glob.name)
		return render(request, 'contentuser/imdex.html', {'mentor': mem_glob, 'sm': sm_glob})
	else:
		print('contentuser PUT')
		return render(request, )
		#return render(request, 'contentuser/imdex.html', {'mentor': mem_glob, 'sm': sm_glob})
