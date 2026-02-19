# Imports priekš nejauša skaitļa ģenerēšanas

import random

# Atkārtošana - spēlēt vēlreiz
while True:  

    pareizais_skaitlis = random.randint(1, 100)
    meginajumi = 0

    print("Es iedomājos skaitli no 1 līdz 100.")
    print("Tev ir 10 mēģinājumi to uzminēt.")

# Skaitļa minēšana

    while True:  

        minejums = input("Tavs minējums: ")

        # Pārbaudām vai ievade ir skaitlis
        try:
            minejums = int(minejums)
        except ValueError:
            print("Lūdzu ievadi veselu skaitli!")
            continue

        meginajumi += 1

        if minejums > pareizais_skaitlis:
            print("Par lielu!")
        elif minejums < pareizais_skaitlis:
            print("Par mazu!")
        else:
            print("Apsveicu! Tu uzminēji!")
            break

        if meginajumi == 10:
            print("Tu iztērēji visus mēģinājumus!")
            break

    print(f"Pareizais skaitlis bija: {pareizais_skaitlis}")
    print(f"Mēģinājumu skaits: {meginajumi}")

    velreiz = input("Vai vēlies spēlēt vēlreiz? (j/n): ")

    if velreiz.lower() != "j":
        print("Paldies par spēli!")
        break
