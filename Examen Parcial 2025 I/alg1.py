import random
q=int(input("Ingrese la cantidad de productos comprados: "))
print("La cantidad de productos llevados es:",q)
sede=random.randint(1,3)
print("La sede seleccionada es de: ",sede)
pre=0

if q<10 :
    match (sede):
        case 1 :
            pre=9
        case 2 :
            pre=7.5
        case 3 :
            pre=6
elif 10<=q<=100 :
    match (sede):
        case 1 :
            pre=8.5
        case 2:
            pre=6
        case 3:
            pre=4.5
elif 100<q<=500 :
    match (sede):
        case 1 :
            pre=5
        case 2 :
            pre=4.5
        case 3:
            pre=3
elif q>500 :
    match (sede):
        case 1:
            pre=4.5
        case 2:
            pre=3.5
        case 3:
            pre=2

if sede==2:
    if q<45 :
        desc=pre*0.05
    else :
        desc=pre*0.10

if sede==3 :
    quin=q//15
    vale=quin*2
    desc=0
if sede==1 :
    desc=0

print("El precio unitario por",q,"productos llevados es de: ",pre)
ic=pre*q
ip=ic-desc

print("\nEl importe de compra será de: ",ic)
print("El importe de descuento fue de: ",round(desc,3))
print("El importe a pagar es de: ",round(ip,3))