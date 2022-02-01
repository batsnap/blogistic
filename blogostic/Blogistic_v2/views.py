from django.http import HttpRequest
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User,Group
from .models import client,operator,worker,order,additional_service,service
from random import randint
from django.contrib.postgres.search import SearchVector
from .forms import UserRegistrationForm,NewOrderForm,OrderForm,OperatorForm,WorkerForm,profile_operator


def main(request):
	return render(request,'main.html')

def profile(request):
	if request.user.is_authenticated:
		user1=User.objects.all().filter(username=request.user.username)[0]
		if client.objects.all().filter(user=user1).count()==1:
			profile=client.objects.all().filter(user=user1)[0]
		elif operator.objects.all().filter(user=user1).count()==1:
			profile=operator.objects.all().filter(user=user1)[0]
		elif worker.objects.all().filter(user=user1).count()==1:
			profile=worker.objects.all().filter(user=user1)[0]
		return render(request,'registration/profile.html',context={'profile': profile,'user':user1})
	else:
		return render(request,'registration/not_login.html')


def registration(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			user_form = UserRegistrationForm(request.POST)
			if user_form.is_valid():
				new_user = user_form.save(commit=False)
				new_user.id_client=client.objects.all().count()+1
				user=User()
				user.id=User.objects.all().count()+1
				user.email=user_form.cleaned_data['email']
				user.set_password(user_form.cleaned_data['password'])
				user.username=user_form.cleaned_data['username']
				user.first_name=user_form.cleaned_data['Full_name'].split(' ')[0]
				user.last_name=user_form.cleaned_data['Full_name'].split(' ')[1]
				user.save()
				new_user.user=user
				new_user.save()
				return HttpResponseRedirect('/accounts/profile')
		else:
			user_form = UserRegistrationForm()
		return render(request, 'registration/registration.html', {'user_form': user_form})
	else:
		return render(request,'registration/already_registrated.html')
def profile_orders(request):
	if request.user.is_authenticated:
		Order=order.objects.all().filter(id_client=client.objects.all().filter(user=request.user)[0].id_client)
		return render(request,'list_orders.html',context={'Order':Order})
def newOrder(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			order_form=NewOrderForm(request.POST)
			if order_form.is_valid():
				new_order=order_form.save(commit=False)
				new_order.id_order=order.objects.count()+1
				new_order.id_client=client.objects.all().filter(user=request.user)[0]
				new_order.price=(new_order.weight//50)*500
				new_order.save()
				return HttpResponseRedirect('/accounts/profile/orders')
		else:
			order_form=NewOrderForm()
		return render(request, 'new_order.html', {'order_form': order_form})
	else:
		return render(request,'registration/not_login.html')
def services(request):
	return render(request,'services.html')

def Prices(request):
	return render(request,'prices.html')

def Cars(request):
	return render(request,'cars.html')


def show_operators(request):
	if request.method=='POST':
		operators=operator.objects.all().annotate(search=SearchVector('Full_name','id_operator','user__email','phone_number')).order_by('id_operator').filter(search=request.POST.get('search'))
	else:
		operators=operator.objects.all().order_by('id_operator')
	return render(request,'operators/operators_list.html',context={'operators':operators})

def show_workers(request):
	if request.method=='POST':
		workers=worker.objects.all().annotate(search=SearchVector('Full_name','id_worker','user__email','phone_number')).order_by('id_worker').filter(search=request.POST.get('search'))
	else:
		workers=worker.objects.all().order_by('id_worker')
	return render(request,'operators/workers_list.html',context={'workers':workers})
def show_orders(request):
	
	if request.method=='POST':
		if request.POST.get('search')=='':
			orders=order.objects.all().order_by('id_order')
			add_service={}
			for i in orders:
				add_service[i]=additional_service.objects.all().filter(number_order=i)
		else:		
			orders=order.objects.all().annotate(search=SearchVector('id_client__Full_name')).order_by('id_order').filter(search=request.POST.get('search'))
			add_service={}
			for i in orders:
				add_service[i]=additional_service.objects.all().filter(number_order=i)
	else:
		orders=order.objects.all().order_by('id_order')
		add_service={}
		for i in orders:
			add_service[i]=additional_service.objects.all().filter(number_order=i)	
	return render(request,'operators/orders_list.html',context={'add_service':add_service})

def one_order(request,id):
	Order=order.objects.all().filter(id_order=id)[0]
	if request.method=='POST':
		print(request.POST)
		Order.id_order=request.POST['id_order']
		Order.id_client=client.objects.all().filter(id_client=request.POST['id_client'])[0]
		Order.id_operator=operator.objects.all().filter(id_operator=request.POST['id_operator'])[0]
		Order.id_worker=worker.objects.all().filter(id_worker=request.POST['id_worker'])[0]
		Order.addressPV=request.POST['addressPV']
		Order.addressPD=request.POST['addressPD']
		Order.date=request.POST['date']
		Order.time_in=request.POST['time_in']
		Order.time_out=request.POST['time_out']
		Order.count_objects=request.POST['count_objects']
		Order.weight=request.POST['weight']	
		Order.type_thing=request.POST['type_thing']
		Order.confirmation_order=request.POST['confirmation_order']
		Order.price=request.POST['price']
		Order.type_pay=request.POST['type_pay']
		Order.status_order=request.POST['status_order']
		Order.save()
		return HttpResponse('<script type="text/javascript">window.close()</script>')
	else:
		form=OrderForm(instance=Order)
		return render(request,'operators/order.html',{'form':form})
def one_worker(request,id):
	Worker=worker.objects.all().filter(id_worker=id)[0]
	if request.method=='POST':
		print(request.POST)
		Worker.user=User.objects.all().filter(id=request.POST['user'])[0]
		Worker.id_worker=request.POST['id_worker']
		Worker.Full_name=request.POST['Full_name']
		Worker.experience=request.POST['experience']
		Worker.position=request.POST['position']
		Worker.phone_number=request.POST['phone_number']
		Worker.save()
		return HttpResponse('<script type="text/javascript">window.close()</script>')
	else:
		form=WorkerForm(instance=Worker)
		return render(request,'operators/worker.html',{'form':form})

def one_operator(request,id):
	Operator=operator.objects.all().filter(id_operator=id)[0]
	if request.method=='POST':
		print(request.POST)
		Operator.user=User.objects.all().filter(id=request.POST['user'])[0]
		Operator.id_worker=request.POST['id_operator']
		Operator.Full_name=request.POST['Full_name']
		Operator.experience=request.POST['experience']
		Operator.position=request.POST['position']
		Operator.phone_number=request.POST['phone_number']
		Operator.save()
		return HttpResponse('<script type="text/javascript">window.close()</script>')
	else:
		form=OperatorForm(instance=Operator)
		return render(request,'operators/operator.html',{'form':form})

def profile_edit(request):
	Operator=operator.objects.all().filter(user=request.user.id)[0]
	if request.method=='POST':
		form=profile_operator(request.POST)
		if form.is_valid():
			print(request.POST)
			return HttpResponse('<script type="text/javascript">window.close()</script>')
	else:
		form=profile_operator()
	return render(request,'registration/profile_edit.html',{'form':form})
def generation_base(request):
	a=order.objects.all()
	for j in range(500):
		l=service.objects.all()
		for i in range(3):
			add_services=additional_service()
			add_services.number_order=a[j]
			add_services.number_service=l[i]
			add_services.save()
	return render(request,'main.html')
def max_sasha():
	a=[int(input(f'Введите {i} число-')) for i in range(10)]
	max_buf=-99999999999999999999999999999
	for i in range(10):
		if a[i]>max_buf:
			max_buf=a[i]
	print('Максимальное число в массиве-',max_buf)
