from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .models import Pet
from .models import Pet_type
from .models import Breed
from .models import Que
from .models import Feedback
from .models import Answer
from .models import Contact
from django.contrib import auth
#from django.contrib.auth import authenticate,login,logout                                                                                                                                                     
# Create your views here.
listusers = []


def sign(request):
	return render(request, 'sign.html')


def signupcheck(request):
	name = request.GET.get('name')
	psw = request.GET.get('psw')
	email = request.GET.get("email")
	fname = request.GET.get("fname")
	mname = request.GET.get("mname")
	lname = request.GET.get("lname")
	mobno = request.GET.get("num")
	newuser = {"name": name, "psw": psw, "email": email,
			   "fname": fname, "mname": mname, "lname": lname, "mobno": mobno}
	listusers.append(newuser)
	User.objects.create(username=name, password=psw, email=email,
						fname=fname, mname=mname, lname=lname, mobno=mobno)
	listuser = User.objects.all()
	return render(request, 'login.html')


def login(request):
	return render(request, 'login.html')


def logincheck(request):
	name = request.GET.get('name')
	psw = request.GET.get('psw')
	print("name",name)
	print("password",psw)
	listuser = User.objects.all()
	listuser1 = list(listuser)
	print("list",listuser)
	print("list",listuser1)
	dict1 = {"user": listuser}
	print(dict1)
	for i in listuser:
		print(i)
		print("for_username",i.username)
		print("for_password",i.password)
		Flag = 1
		if(name==i.username and psw == i.password):
			Flag=0
			print("for_username",i.username)
			print("for_password",i.password)
			request.session['name']=name
			print("name",request.session.get('name'))
			return render(request, 'home.html')
	
		elif(Flag==1):
			return render(request, 'login.html')
		



def home(request):
	#name=request.GET['name']
	#request.session['name']=username
	return render(request, 'home.html')


def display(request):
	l1 = Pet.objects.all()
	dictd = {'display': l1}
	return render(request, 'petdetails.html', dictd)

def searchpettype(request):
	results = Pet_type.objects.all()
	return render(request, 'search.html', {'pettype': results})
	
def searchpet(request):
	pettype = request.GET.get('species')
	breedd = request.GET.get('breed')
	# sextype = request.GET.get('sex')
	# sizee  = request.GET.get('size')
	# agee  = request.GET.get('age')
	print(pettype)
	print('------')
	print(breedd)
	print('------')
	# print(sextype)
	# print('------')
	# print(sizee)
	# print('------') 
	# print(agee)
	# print('---')
	# l1=Pet.objects.filter(sex = sextype).filter(breed = breedd)
	l1 = Pet.objects.filter(pet_type = pettype).filter(breed = breedd)

	# .filter(age =  agee).filter(size = sizee)
	print('-----')
	print(l1)
	dictd = {'display': l1}

	return render(request, 'petdetails.html', dictd)
	
def searchpettype1(request):
	# petage=[]
	# petsex=[]
	# petsize=[]
	results = Pet_type.objects.all()
	results1 = Breed.objects.all()
	results2 = Pet.objects.values('sex').distinct()
	results3 = Pet.objects.values('size').distinct()
	results4 = Pet.objects.values('age').distinct().order_by('age')
	# petsex.append(results2)
	# petage.append(results4)
	# petsize.append(results3)
	# print('-------')
	# dict1={'petagee':petage}
	# dict2={'petsizee':petsize}
	# dict3={'petsexx':petsex}
	# # print(listpet)
	# print(dict1)
	# print('--')
	# print(dict2)
	# print('--')
	# print(dict3)
	return render(request, 'search.html', {'pettype': results, 'breedtype': results1, 'sextype':results2, 'sizetype':results3 , 'agetype':results4 })



def contactus(request):
	return render(request, 'contactus.html')


def contactadd(request):
	fname = request.GET.get('fname')
	lname = request.GET.get('lname')
	email = request.GET.get('email')
	message = request.GET.get('message')
	print(fname)
	print(lname)
	listcc = []
	dictcc = {"fname": fname, "lname": lname,
			  "email": email, "message": message}
	print(dictcc)
	listcc.append(dictcc)
	Contact.objects.create(fname=fname, lname=lname,
						   email=email, message=message)
	Contact.objects.all()
	return render(request, 'home.html')


def feedadd(request):
	email = request.GET.get('email')
	message = request.GET.get('txt')
	print(email)
	print(message)
	Feedback.objects.create(email=email, message=message)
	Feedback.objects.all()
	return render(request, 'home.html')


def feed(request):
	return render(request, 'feedback.html')


def ques(request):
	l2 = Que.objects.all()
	dictq = {'ques': l2}
	return render(request, 'ques.html', dictq)
	
def ans(request):
	answer = request.GET.get('a.id')
	print(ans)
	answer.objects.create(answer=answer)
	answer.objects.all()
	return render(request,'home.html')
def blog(request):    
    return render(request,'blogs.html')
def donate(request):
	return render(request, 'donate.html')
#def logout(request):
	#del request.session['name']
	#if request.session.has_key("name"):
		#print("session exist")
	#else:
		#print("session expire")
	return render(request,'logout.html')
def logout(request):
    auth.logout(request)
    print("name",request.session.get('name'))
    return render(request,'logout.html')
    
def add(request):
	addForm = add()
	data={"addForm":addForm }
	return render(request,'add.html',data)





