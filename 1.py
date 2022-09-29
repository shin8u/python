import random
x=random.randint(0,1000)
f=1
pod=1
max=0
first_i_max=1
last_i_max=1
first_i=1
last_i=1
i=1
print(i,x)
while(x!=0):
    a=random.randint(0,1000)
    i+=1
    print(i," ",a)
    f+=1
    if(a>x):
        pod+=1
        last_i+=1
    else:
        if(pod>max):
            first_i_max=first_i
            last_i_max=last_i
            max=pod
        pod=1
        first_i=i
        last_i=i
    x=a
if(max==1):max=0
print(f"Получено {f} чисел")
print(f"Наибольшая высота подъёма: {max}")
print(f"Промежуток подъема:[{first_i_max};{last_i_max}]")
