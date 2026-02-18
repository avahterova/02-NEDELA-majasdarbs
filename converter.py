# ===== KONVERSIJAS KOEFICIENTI =====
KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020

print("Izvēlies konversiju:")
print("1) km <-> mi")
print("2) kg <-> lb")
print("3) L <-> gal")
print("4) $ <-> €")
Lietotāja_izvēle = input("> ")

if Lietotāja_izvēle == "1":
    print("Virziens:")
    print("1) km -> mi")
    print("2) mi -> km")
    Konvertēšanas_virziens = input("> ")
    if Konvertēšanas_virziens != "1" and Konvertēšanas_virziens != "2":
        print("Kļūda: jāizvēlas 1 vai 2")
        exit()
        
    try:
        value = float(input("Ievadi vērtību: "))
    except ValueError:
        print("Kļūda: jāievada skaitlis")
        exit()
        
    if Konvertēšanas_virziens == "1":
        result = value * KM_TO_MI
        print(f"{value:.2f} km = {result:.2f} mi")
    elif Konvertēšanas_virziens == "2":
        result = value / KM_TO_MI
        print(f"{value:.2f} mi = {result:.2f} km")
    else:
        print("Nepareizs virziens")

