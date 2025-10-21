# Projekt 1: "Task Manager"
# Autor: Lucie Mendlíková
# Kurz: Testing Akademie
# Datum: 18.10.2025

# Seznam úkolů
ukoly = []

# --- Hlavní menu ---
def hlavni_menu():
    while True: 
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnosti (1-4): ")

        print()  # volný řádek po zadání volby
        
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("\nKonec programu")
            break
        else: print(("Neplatná volba, zkuste to znovu."))


# --- Přidat nový úkol ---
# Zadejte název úkolu: Úkol 1
# Zadejte popis úkolu: Popis pro úkol 1
# Úkol "Úkol 1" byl přidán. 
nazev = "Úkol 1"
popis = "Popis pro úkol 1"

def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ")
        popis = input("Zadejte popis úkolu: ")

        if nazev and popis:
            ukoly.append({"název": nazev, "popis": popis})
            print(f"Úkol {nazev} byl přidán.\n")
            break
        else: 
            print("Název i popis úkolu musí být zadány. Zkuste to znovu.")

# Po přidání se vrátí do hlavního menu
            hlavni_menu()

# --- Zobrazit všechny úkoly ---
def zobrazit_ukoly():
    if not ukoly:
        print("Žádné úkoly k zobrazení.")

    else: 
        print("Seznam úkolů:")
        for index, ukol in enumerate(ukoly, start=1):
            print(f"{index}. Název: {ukol['název']}, Popis: {ukol['popis']}")

# Po zobrazení se vrátí do hlavního menu
            hlavni_menu()

# --- Odstranit úkol ---
def odstranit_ukol():
    if not ukoly:
        print("Žádné úkoly k odstranění.")
        return
    zobrazit_ukoly()
    try:
        cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
        if 1 <= cislo <= len(ukoly):
            odstraneny_ukol = ukoly.pop(cislo - 1)
            print(f"Úkol {odstraneny_ukol['název']} byl odstraněn.")
        else:
            print("Neplatné číslo úkolu. Zkuste to znovu.")
    except ValueError:
        print("Zadaná hodnota není platné číslo.")

# Po odstranění se vrátí do hlavního menu
        hlavni_menu()




    
        



    







            





