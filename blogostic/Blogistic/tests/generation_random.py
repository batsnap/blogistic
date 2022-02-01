from random import randint,shuffle,choice
from requests import get,post
from bs4 import BeautifulSoup
import json
from time import sleep
def phone_number(k):
	m=[]
	for i in range(k):
		m.append('+7'+str(randint(1000000000,9999999999)))
	return m
def pass_list(k,l):
	chars = '+-*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	passt_list=[]
	for n in range(k):
		password =''
		for i in range(l):
			password += choice(chars)
		passt_list.append(password)
	return passt_list
def transliterate(list):
	m=[]
	for i in range(0,len(list)):
		m.append(list[i].split(' ')[0]+' '+list[i].split(' ')[1]+' '+list[i].split(' ')[2])
	slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
	  'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
	  'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
	  'ц':'c','ч':'ch','ш':'sh','щ':'sch','ъ':'','ы':'y','ь':'','э':'e',
	  'ю':'u','я':'ya', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'YO',
	  'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
	  'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H',
	  'Ц':'C','Ч':'CH','Ш':'SH','Щ':'SCH','Ъ':'','Ы':'y','Ь':'','Э':'E',
	  'Ю':'U','Я':'YA',',':'','?':'',' ':'_','~':'','!':'','@':'','#':'',
	  '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
	  ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
	  '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
	  'Є':'e', '—':''}
		
   # Циклически заменяем все буквы в строке
	for i in range(len(m)):
		for key in slovar:
			m[i] = m[i].replace(key, slovar[key])
		m[i]=m[i]+str(i)
	return m
def dates(k):
	l={"start": "1950-01-01","end": "2004-12-31"}
	header={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36','content-type':'application/json;charset=UTF-8'}
	url='https://randomall.ru/api/general/date'
	m=[]
	for i in range(k):
		sleep(1)
		resp=post(url,headers=header,data=json.dumps(l))
		m.append(resp.text.replace('"',''))
	return m
def email(k,usernames):
	m=[]
	for i in range(k):
		m.append(usernames[i]+'@sorrrry.xyz')
	return m
def card_numbers(k):
	return [str(randint(1000,9999))+' '+str(randint(1000,9999))+' '+str(randint(1000,9999))+' '+str(randint(1000,9999))+' ' for i in range(k)] 
def names1(k):
	url='https://randomus.ru/name?type=0&sex=0&count='+str(k)
	response=get(url)
	soup=BeautifulSoup(response.text,'html')
	return soup.find('textarea').text.split('\n')

def gen_order():
	pass
def gen_client(k):
	a=open('clients.txt','a')
	names=names1(k)
	passoword=pass_list(k,8)
	usernames=transliterate(names)
	date=dates(k)
	emails=email(k,usernames)
	cards=card_numbers(k)
	for i in range(k):
		a.write(names[i]+'/'+passoword[i]+'/'+usernames[i]+'/'+date[i]+'/'+emails[i]+'/'+cards[i]+'\n')
def gen_worker(k):
	a=open('worker.txt','w')
	names=names1(k)
	passoword=pass_list(k,8)
	usernames=transliterate(names)
	emails=email(k,usernames)
	phone_numbers=phone_number(k)
	for i in range(k):
		if i<k//2:
			a.write(names[i]+'/'+passoword[i]+'/'+usernames[i]+'/'+'Грузчик'+'/'+emails[i]+'/'+phone_numbers[i]+'\n')
		else:
			a.write(names[i]+'/'+passoword[i]+'/'+usernames[i]+'/'+'Водитель'+'/'+emails[i]+'/'+phone_numbers[i]+'\n')
def gen_operator(k):
	a=open('operator.txt','w')
	names=names1(k)
	passoword=pass_list(k,8)
	usernames=transliterate(names)
	emails=email(k,usernames)
	phone_numbers=phone_number(k)
	for i in range(k):
		a.write(names[i]+'/'+passoword[i]+'/'+usernames[i]+'/'+'Оператор'+'/'+emails[i]+'/'+phone_numbers[i]+'\n')
def gen_adress():
	a=open('name2.txt','r')
	b=open('address.txt','w')
	k=[]
	for i in a:
		k.append(i.split('/')[0])
		k.append(i.split('/')[1])
	l=[]
	for i in range(len(k)):
		for j in range(len(k)):
			if j!=i:
				l.append(k[i]+'/'+k[j]+'\n')
	shuffle(l)
	for i in l: 
		b.write(i)
	
gen_adress()
#gen_worker(100)
#gen_operator(100)