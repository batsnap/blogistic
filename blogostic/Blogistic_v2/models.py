from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

from random import randint


# Create your models here.
class client(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    id_client=models.IntegerField(primary_key=True)
    Full_name=models.CharField(max_length=50)
    birthday=models.DateField()
    Card_number=models.CharField(max_length=30)

class worker(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    id_worker=models.IntegerField(primary_key=True)
    Full_name=models.CharField(max_length=50)
    experience=models.CharField(max_length=30)
    position=models.CharField(max_length=30,default='Грузчик',null=True)
    phone_number=models.CharField(max_length=14,null=True)

class operator(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    id_operator=models.IntegerField(primary_key=True)
    Full_name=models.CharField(max_length=50)
    experience=models.CharField(max_length=30)
    position=models.CharField(max_length=30,default='Оператор',null=True)
    phone_number=models.CharField(max_length=14,null=True)
    
class service(models.Model):
    id_service=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    cost=models.IntegerField(null=True,default=300)

class order(models.Model):
    type_pay_CHOICES=(
        ('card','Картой'),
        ('cash','Наличные')
    )
    status_order_choices=(
        ('В обработке','В обработке'),
        ('В процессе','В процессе'),
        ('Закончен','Закончен')
    )
    id_order=models.IntegerField(primary_key=True)
    id_client=models.ForeignKey('client',on_delete=models.CASCADE)
    id_operator=models.ForeignKey('operator',on_delete=models.CASCADE,default=operator.objects.all().filter(id_operator=randint(1,len(operator.objects.all())))[0].id_operator)
    id_worker=models.ForeignKey('worker',on_delete=models.CASCADE,default=worker.objects.all().filter(id_worker=randint(1,len(worker.objects.all())))[0].id_worker)
    addressPV=models.CharField(max_length=100)
    addressPD=models.CharField(max_length=100)
    date=models.DateField(null=True)
    time_in=models.TimeField(null=True)
    time_out=models.TimeField(null=True)
    count_objects=models.IntegerField()
    weight=models.FloatField()
    type_thing=models.CharField(max_length=100)
    confirmation_order=models.CharField(max_length=20,default='Подтвержденно')
    price=models.IntegerField()
    type_pay=models.CharField(max_length=100,choices=type_pay_CHOICES)
    status_order=models.CharField(max_length=100,default='В обработке',choices=status_order_choices)
    @admin.display(ordering='id_client')
    def name_client(self):
        return self.id_client.Full_name
    @admin.display(ordering='id_operator')
    def name_operator(self):
        return self.id_operator.Full_name
    @admin.display(ordering='id_worker')
    def name_worker(self):
        return self.id_worker.Full_name

class Car(models.Model):
    type_car_choieces=(
        ('small','Малый от 500 кг до 2 тонн'),
        ('medium','Средний от 2 тонн до 5 тонн'),
        ('big','Большой от 5 тонн до 16 тонн'),
        ('very_big','Сверхтяжелый от 16 тонн и выше')
    )
    id_car=models.IntegerField(primary_key=True)
    id_worker=models.ForeignKey('worker',on_delete=models.CASCADE)
    type_car=models.CharField(max_length=100,choices=type_car_choieces)
    price=models.CharField(max_length=100)
    @admin.display(ordering='id_worker')
    def name_worker(self):
        return self.id_worker.Full_name

class additional_service(models.Model):
    number_order=models.ForeignKey(order,on_delete=models.CASCADE)
    number_service=models.ForeignKey(service,on_delete=models.CASCADE)
    @admin.display(ordering='number_order')
    def name_service(self):
        return self.number_service.name

class Car_order(models.Model):
    number_order=models.ForeignKey(order,on_delete=models.CASCADE)
    number_car=models.ForeignKey(Car,on_delete=models.CASCADE)
    @admin.display(ordering='number_order1')
    def number_order1(self):
        return self.number_order.id
    @admin.display(ordering='number_car1')
    def number_car1(self):
        return self.number_car.id
class additional_serviceAdmin(admin.ModelAdmin):
    list_display=('number_order','name_service')
    ordering=('number_order',)
admin.site.register(additional_service,additional_serviceAdmin)