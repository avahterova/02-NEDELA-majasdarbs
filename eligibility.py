# Ievadam jautājumu par vecumu
vecums_input = input("Ievadi vecumu: ")

# Pārbaudām, vai ievade ir skaitlis
if vecums_input.isdigit():
    vecums = int(vecums_input)
else:
    print("Kļūda: vecumam jābūt skaitlim!")
    exit()  
if vecums < 0:
    print("Kļūda: vecums nevar būt negatīvs!")
    exit()
# Ievades funkcija, lai pārvērstu j/n uz bool
def yes_no_input(jautajums):
    atbilde = input(jautajums + " (j/n): ").strip().lower()
    if atbilde == "j":
        return True
    elif atbilde == "n":
        return False
    else:
        print("Kļūda: jā ievadīt 'j' vai 'n'")
        exit()

ir_aplieciba = yes_no_input("Vai ir autovadītāja apliecība?")
ir_students = yes_no_input("Vai ir students?")
ir_veterans = yes_no_input("Vai ir veterāns?")

# Loģiskas izteiksmes ar and, or, not
balsošana = vecums >= 18
auto_ire = vecums >= 21 and ir_aplieciba
senioru_atlaide = vecums >= 65 or ir_veterans
studentu_atlaide = (16 <= vecums <= 26) and ir_students

# Loģiskas izteiksmes ar and, or, not
print("---")
print(f"Balsošana: {'Jā ✓' if balsošana else 'Nē ✗'}")
print(f"Auto īre: {'Jā ✓' if auto_ire else 'Nē ✗'}")
print(f"Senioru atlaide: {'Jā ✓' if senioru_atlaide else 'Nē ✗'}")
print(f"Studentu atlaide: {'Jā ✓' if studentu_atlaide else 'Nē ✗'}")

