import random

años=random.randint(1,50)
cap=int(input("Ingrese el numero de capacitaciones: "))
if cap<0 :
    cap=0
sueldo=int(input("Ingrese el sueldo del trabajador: "))
print("Los años trabajados fueron: ",años)
if años<5:
    match (cap):
        case 0 : aum=0.08
        case 1 : aum=0.10
        case _: aum=0.12
elif años>=5:
    match (cap):
        case 0: aum=0.15
        case 1: aum=0.18
        case _: aum=0.20

su_aum=sueldo+(sueldo*aum)
print("El sueldo final será: ",su_aum)