from django.contrib.auth.models import User
from .models import client, operator, order,worker
from django import forms


class UserRegistrationForm(forms.ModelForm):
    username=forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    email=forms.CharField(label='Email')
    class Meta:
        model = client
        fields = ('Full_name', 'birthday','Card_number')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']      
    def clean_username(self):
        cd=self.cleaned_data['username']
        if User.objects.all().filter(username=cd).count()>=1:
            raise forms.ValidationError('Имя пользователя занято')
        return cd      

class NewOrderForm(forms.ModelForm):
    class Meta:
        model=order
        fields = ('addressPV', 'addressPD','count_objects', 'weight','type_pay')

class OrderForm(forms.ModelForm):
    class Meta:
        model=order
        fields='__all__'

class OperatorForm(forms.ModelForm):
    email=forms.CharField(label='Email')
    class Meta:
        model=operator
        fields='__all__'

class WorkerForm(forms.ModelForm):
    email=forms.CharField(label='Email')
    class Meta:
        model=worker
        fields='__all__'
class profile_client(forms.ModelForm):
    class Meta:
        model=client
        fields='__all__'
class profile_operator(forms.ModelForm):
    username=forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    email=forms.CharField(label='Email')
    class Meta:
        model=operator
        fields=('Full_name','experience','phone_number')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
    def clean_username(self):
        cd=self.cleaned_data['username']
        if User.objects.all().filter(username=cd).count()>=1:
            raise forms.ValidationError('Имя пользователя занято')
        return cd