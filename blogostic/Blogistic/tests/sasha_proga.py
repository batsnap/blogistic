from random import randint
from re import L
def sasha2():
	n=int(input('Введите количество чисел: '))
	a=[int(input()) for i in range(n)]
	k=0
	for i in range(n):
		k+=a[i]
	print(k/n)
def sasha3():
	n=int(input('Введите количество чисел: '))
	l=int(input('Число для подсчета вхождений: '))
	a=[int(input()) for i in range(n)]	
	k=0
	for i in range(n):
		if a[i]==l:
			k+=1
	print(k)
def sasha4():
	n=int(input('Введите количество чисел: '))
	l=int(input('Число для подсчета вхождений: '))
	a=[int(input(f'Введите {i} число массива: ')) for i in range(n)]	# {i} подстановка
	k=0
	for i in range(n):
		if a[i]==l:
			k=i
			break
	print(k)
	'''
	break выход из цикла
	для вывода первого элемента который встретился первым
	'''
def sasha5():
	n=int(input('Введите количество чисел: '))
	l=int(input('Число для подсчета вхождений: '))
	a=[int(input()) for i in range(n)]	
	k=0
	for i in range(n):
		if a[i]%2==0:
			a[i]=a[i]//2
	print(a)
def sasha6():
	n=int(input('Введите количество чисел: '))
	l=int(input('Число для подсчета вхождений: '))
	a=[int(input()) for i in range(n)]	
	k=0
	for i in range(n-1):
		a[i],a[i+1]=a[i+1],a[i]
	print(a)
def sasha7():
	n=int(input('Введите количество чисел: '))
	l=int(input('позиция: '))
	m=int(input('число: '))
	a=[int(input(f'Введите {i} число массива: ')) for i in range(n)]	
	k=0
	a[l]=m
	print(a)
def sasha8():
	n=int(input('Введите количество чисел: '))
	m=int(input('число: '))
	a=[int(input(f'Введите {i} число массива: ')) for i in range(n)]	
	k=0
	for i in range(n):
		if a[i]==m:
			del a[i]
			break
	print(a)
def sasha9():
	a = [[2, 5, 1, 0], [1, 8, 4, 2], [6, 7, 3, 1]]
	for i in range(3):
		a[i].sort()#сортировка строки
		for j in range(4):
			print(a[i][j],end=' ')
		print()
def sasha10():
	n=int(input('Введите количество чисел: '))
	a=[randint(-10,10) for i in range(n)]
	polojitelnie=[]
	orticatelnie=[]
	for i in range(n):
		if a[i]>0:
			polojitelnie.append(a[i])
		else:
			orticatelnie.append(a[i])
	print(orticatelnie)
	print(polojitelnie)
sasha10()