from django.urls import path
from . import views

urlpatterns = [
    # post views
    path('',views.main),
    path('Services',views.services),
    path('Prices',views.Prices),
    path('Cars',views.Cars),
    path('accounts/profile',views.profile),
    path('accounts/registration',views.registration),
    path('accounts/profile/edit',views.profile_edit),
    path('accounts/profile/orders',views.profile_orders),
    path('accounts/profile/make_order',views.newOrder),
    path('gen_base',views.generation_base),
    path('accounts/operator/operators',views.show_operators),
    path('accounts/operator/workers',views.show_workers),
    path('accounts/operator/orders',views.show_orders),
    path('accounts/operator/orders/<int:id>',views.one_order),
    path('accounts/operator/workers/<int:id>',views.one_worker),
    path('accounts/operator/operators/<int:id>',views.one_operator)
]
