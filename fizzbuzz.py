# While True atkārtojam bezgalīgi līdz ievade ir korekta, Continue palīdz atkārtot ciklu līdz atbilde korekta, tad break 15.rindā

while True:
    user_input = input("Ievadi veselu skaitli N: ")

    if user_input == "":
        print("Tu neko neievadīji.")
        continue

    if not user_input.isdigit():
        print("Lūdzu, ievadi veselu skaitli.")
        continue

    N = int(user_input)
    break  

# Forpython3 fizzbuzz.py N
import sys

# Pārbaudam, vai arguments ir dots. Ja sarakstā ir mazāk par 2 elementiem, tad lietotājs NAV iedevis skaitli
if len(sys.argv) < 2:
    print("Lūdzu ievadi skaitli kā argumentu.")
    sys.exit()

# Pārbauda, vai tas ir skaitlis
if not sys.argv[1].isdigit():
    print("Ievadi veselu skaitli.")
    sys.exit()

N = int(sys.argv[1])

# For cikls, lai iestatītu nosacījumu par range un tālāk ar if, lai ierakstītu nosacījumus, kuri atspoguļosies tekstā
for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=", ")
    elif i % 3 == 0:
        print("Fizz", end=", ")
    elif i % 5 == 0:
        print("Buzz", end=", ")
    else:
        print(i, end=", ")
