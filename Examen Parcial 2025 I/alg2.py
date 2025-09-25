flag=True
while flag :
    num=int(input("Ingrese un numero: "))
    if 100<=num<=1000 and num%2==0:
        flag=False
    else :
        print("Error, ingrese un numero par del 100 al 1000")

u=num%10
d=(num//10)%10
c=num//100

if num<500 :
    if u==9:
        print("La unidad es: ",u)
    elif d==9:
        print("La decena es: ",d)
    else: 
        print("Ninguna cifra es 9")
if 500<=num<=999:
    if u==c :
        print("El numero es capicúa")
    else :
        print("El numero no es capicua")
if num>999 :
    print(pow(num,8))
    