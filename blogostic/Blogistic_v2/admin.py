from django.contrib import admin
from .models import client, worker,operator,service,order,Car

class clientAdmin(admin.ModelAdmin):
    list_display = ('id_client','Full_name','birthday','Card_number')
    search_fields = ('Full_name','id_client')
    ordering=('id_client',)
admin.site.register(client,clientAdmin)

class workerAdmin(admin.ModelAdmin):
    list_display = ('id_worker','Full_name','experience','position','phone_number')
    search_fields = ('Full_name','id')
    ordering=('id_worker',)
admin.site.register(worker,workerAdmin)

class operatorAdmin(admin.ModelAdmin):
    list_display = ('id_operator','Full_name','experience','position','phone_number')
    search_fields = ('Full_name','id')
    ordering=('id_operator',)
admin.site.register(operator,operatorAdmin)

class serviceAdmin(admin.ModelAdmin):
    list_display=('id_service','name','cost')
    ordering=('id_service',)
admin.site.register(service,serviceAdmin)

class orderAdmin(admin.ModelAdmin):
    list_display = ('id_order','name_client','name_operator','name_worker','addressPV','addressPD','date','time_in','time_out','count_objects','weight','type_thing','confirmation_order','price','type_pay','status_order')
    ordering=('id_order',)
admin.site.register(order,orderAdmin)

class Car_serviceAdmin(admin.ModelAdmin):
    list_display=('id_car','name_worker','type_car','price')
    ordering=('id_car',)
admin.site.register(Car,Car_serviceAdmin)
# Register your models here.
