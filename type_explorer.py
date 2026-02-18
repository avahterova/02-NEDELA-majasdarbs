# ===== PAMATA DATU TIPI =====
teksts = "Ziedi"
skaitlis = 13
komata_skaitlis = 3.14
patiesiba = True
nekas = None

# ===== DATU TIPU IZVADS =====
# print(type(teksts)) # <class 'str'>
# print(type(skaitlis)) # <class 'int'>
# print(type(komata_skaitlis)) # <class 'float'>
# print(type(patiesiba)) # <class 'bool'>
# print(type(nekas)) # <class 'NoneType'>

# # ===== TRUTHY / FALSY PIEMĒRI =====
# print(bool(""))      # False — tukša virkne
# print(bool(" "))     # True — atstarpe ir simbols NAV tukša
# print(bool("0"))     # True — netukša virkne, "0" ir teksts, nevis skaitlis
# print(bool(0))       # False — nulle ir skaitlis
# print(bool([]))      # False — tukšs saraksts
# print(bool(None))    # False — None vienmēr ir False

# ===== TIEŠĀ DATU TIPU PĀRVEIDOŠANA (EXPLICIT CONVERSION) =====

# print("5" + "3")        # "53" — virkņu savienošana (nav skaitļu saskaitīšana, TIKAI teksta apvienošana)
# print(int("5") + 3)     # 8 — teksts "5" pārvērsts par skaitli un 5+3=8
# print(float("3.14"))    # 3.14 — teksts pārvērsts par skaitli ar komatu
# print(float("3.14") + 5.98)    # 9.120000000000001 — 3.14 teksts pārvērsts par skaitli ar komatu un saskaitīts kopā 3.14+5.98=9.12
# print(float("92"))    # 92.0 — teksts pārvērsts par skaitli ar komatu
# print(float(92))      # 92.0 — skaitlis pārvērsts par skaitli ar komatu

# ===== ROBEŽGADĪJUMI =====
# print("5" + 3)          # TypeError: can only concatenate str (not "int") to str. Pyton neļauj šādi rakstīt bez int.
# print(int("abc"))     # ValueError: invalid literal for int() with base 10: 'abc' — burti nevar kļūt par skaitli
# print(int("3.14"))    # ValueError: invalid literal for int() with base 10: '3.14' - veselam skaitlim nevar būt komats

# ===== SKAITĻU PĀRVEIDOŠANA =====
print(int(3.86))              # 3 - pārverš veselā skaitlī, 'nogriežot' aiz komata
# print(int("3.14")).           # ValueError: invalid literal for int() with base 10: '3.14' - int nesaprot punktu
print(int(float("3.14")))     # 3 - jānorāda, ka tas ir skaitlis ar komatu
print(float("1e3"))           # 1000.0 - zinātniskais pieraksts
