n=int(input('Введите количество элементов массива '))
array=[0]*n
min=99999
counter=0
flag=0
for i in range(n):
	array[i]=int(input('Введите элемент '))
for i in range(n):
	if array[i]<min:
		min=array[i]
delta=int(input('Введите delta '))
for i in range(n):
	if array[i]-min==delta:
		counter+=1
		flag=1
if flag==0:
	print('В массиве нет подходящих элементов')
else:
	print('Количество подходящих под условие элементов ', counter)