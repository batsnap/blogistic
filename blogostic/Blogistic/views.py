

from django.shortcuts import render,HttpResponseRedirect
#from .models import additional_service, order,client,operator,worker,Car,service
from random import randint
from time import time
from ..Blogistic_v2.forms import UserRegistrationForm,NewOrderForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.postgres.search import SearchVector
def main(request):
	a=open('/home/batyr/Projects/web/web_programming/blogistic/blogostic/Blogistic/tests/clients.txt','r')
	
	for i in a:
		l=i.split('/')[3]
		l=l[6]+l[7]+l[8]+l[9]+'-'+l[3]+l[4]+'-'+l[0]+l[1]
		user=User()
		user.id=User.objects.count()+1
		user.username=i.split('/')[2]
		user.set_password(i.split('/')[1])
		user.email=i.split('/')[4]
		user.first_name=i.split('/')[0].split(' ')[0]
		user.last_name=i.split('/')[0].split(' ')[1]
		user.save()
		clien=client()
		clien.id_client=client.objects.count()+1
		clien.user=user
		clien.Full_name=i.split('/')[0]
		clien.birthday=l
		clien.Card_number=i.split('/')[5]
		clien.save()
		l=''
	
	a=open('/home/batyr/Projects/web/web_programming/blogistic/blogostic/Blogistic/tests/operator.txt','r')
	
	for i in a:
		user=User()
		user.id=User.objects.count()+1
		user.set_password(i.split('/')[1])
		user.email=i.split('/')[4]
		user.first_name=i.split('/')[0].split(' ')[0]
		user.last_name=i.split('/')[0].split(' ')[1]
		user.is_staff=True
		user.username=i.split('/')[2]
		user.save()
		clien=operator()
		clien.id_operator=operator.objects.count()+1
		clien.user=user
		clien.Full_name=i.split('/')[0]
		clien.phone_number=i.split('/')[5]
		clien.position=i.split('/')[3]
		clien.experience=str(randint(1,10))+' лет'
		clien.save()
	a=open('/home/batyr/Projects/web/web_programming/blogistic/blogostic/Blogistic/tests/worker.txt','r')
	
	for i in a:
		user=User()
		user.id=User.objects.count()+1
		user.set_password(i.split('/')[1])
		user.email=i.split('/')[4]
		user.first_name=i.split('/')[0].split(' ')[0]
		user.last_name=i.split('/')[0].split(' ')[1]
		user.is_staff=True
		user.username=i.split('/')[2]
		user.save()
		clien=worker()
		clien.id_worker=worker.objects.count()+1
		clien.user=user
		clien.Full_name=i.split('/')[0]
		clien.phone_number=i.split('/')[5]
		clien.position=i.split('/')[3]
		clien.experience=str(randint(1,10))+' лет'
		clien.save()
'''
def profile(request):
	if request.user.is_authenticated:
		user1=User.objects.all().filter(username=request.user.username)[0]
		try:
			profile=client.objects.all().filter(user=user1)[0]
		except:
			pass
		try:
			profile=operator.objects.all().filter(user=user1)[0]
		except:
			pass
		try:
			profile=worker.objects.all().filter(user=user1)[0]
		except:
			pass
		return render(request,'registration/profile.html',context={'profile': profile,'user':user1})
	else:
		return render(request,'registration/not_login.html')

@csrf_exempt
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
	return render(request,'base.html')

def Prices(request):
	return render(request,'prices.html')

def Cars(request):
	return render(request,'cars.html')

def generation_base(request):
	for i in range(1,501):
		for j in range(1,4):
			k=additional_service()
			k.number_order=order.objects.all().filter(id_order=i)[0]
			k.number_service=service.objects.all().filter(id_service=j)[0]
			k.save()
	return render(request,'main.html')
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
	#if request.method=='POST':
	#	orders=order.objects.all().annotate(search=SearchVector('Full_name','id_worker','user__email','phone_number')).order_by('id_worker').filter(search=request.POST.get('search'))
	#else:
	orders=order.objects.all().order_by('id_order')
	return render(request,'operators/orders_list.html',context={'orders':orders})

'''































'''
	



	type=['small','medium','big','very_big']
	price=['5000','7000','8000','10000']
	for i in range(50):
		car=Car()
		car.id_car=Car.objects.count()+1
		car.id_worker=worker.objects.all().filter(position='Водитель')[randint(0,worker.objects.all().filter(position='Водитель').count()-1)]
		l=randint(0,3)
		car.type_car=type[l]
		car.price=price[l]
		car.save()

def generation_base(request):
	a=open('/home/batyr/Projects/web/web_programming/blogistic/blogostic/Blogistic/tests/name2.txt','r')
	k=[]
	for i in a:
		k.append(i.replace('\n',''))
	for i in range(50):
		Orders=order()
		Orders.id_order=order.objects.count()+1
		Orders.id_client=client.objects.all()[randint(1,client.objects.count())-1]
		Orders.id_operator=operator.objects.all()[randint(1,operator.objects.count())-1]
		Orders.id_worker=worker.objects.all().filter(position='Водитель')[randint(1,worker.objects.all().filter(position='Водитель').count()-1)]
		Orders.addressPV=k[i].split('/')[0]
		Orders.addressPD=k[i].split('/')[1]
		Orders.date='2022-01-16'
		Orders.time_in='10:15'
		Orders.time_out='15:15'
		Orders.count_objects=randint(5,20)
		Orders.weight=randint(5,20)*50
		Orders.type_thing='Коробки'
		Orders.price=(Orders.weight//50)*500
		if randint(-1,1)==1:
			Orders.type_pay='card'
		else:
			Orders.type_pay='cash'
		Orders.save()
	return render(request,'main.html')

		a=open('/home/batyr/Projects/web/web_programming/blogistic/blogostic/Blogistic/tests/clients.txt','r')
	
	for i in a:
		l=i.split('/')[3]
		l=l[6]+l[7]+l[8]+l[9]+'-'+l[3]+l[4]+'-'+l[0]+l[1]
		user=User()
		user.id=User.objects.count()+1
		user.username=i.split('/')[2]
		user.set_password(i.split('/')[1])
		user.email=i.split('/')[4]
		user.first_name=i.split('/')[0].split(' ')[0]
		user.last_name=i.split('/')[0].split(' ')[1]
		user.save()
		clien=client()
		clien.id_client=client.objects.count()+1
		clien.user=user
		clien.Full_name=i.split('/')[0]
		clien.birthday=l
		clien.Card_number=i.split('/')[5]
		clien.save()
		l=''
	
	a=open('/home/batyr/Projects/web/web_programming/blogistic/blogostic/Blogistic/tests/operator.txt','r')
	
	for i in a:
		user=User()
		user.id=User.objects.count()+1
		user.set_password(i.split('/')[1])
		user.email=i.split('/')[4]
		user.first_name=i.split('/')[0].split(' ')[0]
		user.last_name=i.split('/')[0].split(' ')[1]
		user.is_staff=True
		user.username=i.split('/')[2]
		user.save()
		clien=operator()
		clien.id_operator=operator.objects.count()+1
		clien.user=user
		clien.Full_name=i.split('/')[0]
		clien.phone_number=i.split('/')[5]
		clien.position=i.split('/')[3]
		clien.experience=str(randint(1,10))+' лет'
		clien.save()
	a=open('/home/batyr/Projects/web/web_programming/blogistic/blogostic/Blogistic/tests/worker.txt','r')
	
	for i in a:
		user=User()
		user.id=User.objects.count()+1
		user.set_password(i.split('/')[1])
		user.email=i.split('/')[4]
		user.first_name=i.split('/')[0].split(' ')[0]
		user.last_name=i.split('/')[0].split(' ')[1]
		user.is_staff=True
		user.username=i.split('/')[2]
		user.save()
		clien=worker()
		clien.id_worker=worker.objects.count()+1
		clien.user=user
		clien.Full_name=i.split('/')[0]
		clien.phone_number=i.split('/')[5]
		clien.position=i.split('/')[3]
		clien.experience=str(randint(1,10))+' лет'
		clien.save()

a=open('/home/batyr/Projects/web/web_programming/blogistic/blogostic/Blogistic/tests/address.txt','r')
	k=[]
	for i in a:
		k.append(i.replace('\n',''))
	for i in range(500):
		Orders=order()
		Orders.id_order=order.objects.count()+1
		Orders.id_client=client.objects.all()[randint(1,client.objects.count())-1]
		Orders.id_operator=operator.objects.all()[randint(1,operator.objects.count())-1]
		Orders.id_worker=worker.objects.all().filter(position='Водитель')[randint(1,worker.objects.all().filter(position='Водитель').count()-1)]
		Orders.addressPV=k[i].split('/')[0]
		Orders.addressPD=k[i].split('/')[1]
		Orders.date='2022-01-17'
		Orders.time_in='10:15'
		Orders.time_out='15:15'
		Orders.count_objects=randint(5,20)
		Orders.weight=randint(5,20)*50
		Orders.type_thing='Коробки'
		Orders.price=(Orders.weight//50)*500
		if randint(-1,1)==1:
			Orders.type_pay='card'
		else:
			Orders.type_pay='cash'
		Orders.save()
-----------------------------
			groupss=Group.objects.all()[0]
	oper=operator.objects.all()
	for i in oper:
		i.user.groups.add(groupss)
		i.save()
		'''