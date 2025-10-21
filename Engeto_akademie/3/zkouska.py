import math, datetime, modul_Engeto, random
import modul_Engeto
from random import random

vek_uzivatele = 150
if vek_uzivatele < 18:
    print("Kofola")
elif vek_uzivatele >=18 and vek_uzivatele < 64:
    print("Nazdravi")
elif vek_uzivatele >= 64 and vek_uzivatele < 140:
    print("Pozor, pijte s rozumem")
else:
    print("Chyba, spatně zadaný věk")

#Funkce
def obvod_trojuhelniku(strana_a, strana_b, strana_c):
    obvod = strana_a+strana_b+strana_c
    return obvod

#Zadaní: a=45, b=56, c=150
print(obvod_trojuhelniku(45,56,150))

#print(math.sqrt(16))
aktualni_cas = datetime.datetime.now()
print(aktualni_cas)

# pouziti funkce z modulu
print(modul_Engeto.rozdil(50,5))