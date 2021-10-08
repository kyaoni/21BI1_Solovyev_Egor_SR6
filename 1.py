try:
    n=int(input('Введите количество элементов массива '))
except ValueError:
    print('Ошибка ввода')
else:
    if n>0:
        flag1=True
        array=[0]*n
        counter=0
        flag=0
        min_value=0
        for i in range(n):
                try:
                    array[i]=int(input('Введите элемент '))
                except ValueError:
                    flag1=False
                    break
        if flag1:
                min_value=array[0]
                for i in range(n):
                    if array[i]<min_value:
                        min_value=array[i]
                try:
                    delta=int(input('Введите delta '))
                except ValueError:
                    print('Ошибка ввода')
                else:
                    for i in range(n):
                        if abs(min_value-array[i])==delta:
                            counter+=1
                            flag=1
                    if flag==0:
                        print('В массиве нет подходящих элементов')
                    else:
                        print('Количество подходящих под условие элементов ', counter)
        else:
            print('Ошибка ввода')
    else:
        print('Ошибка ввода')