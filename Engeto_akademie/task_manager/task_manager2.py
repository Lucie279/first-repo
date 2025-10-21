# Projekt 1: "Task Manager"
# Autor: Lucie Mendlíková
# Kurz: Testing Akademie
# Datum: 24.10.2025

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

        volba = input("Vyberte možnost (1-4): ")
        print() # Přidá prázdný řádek

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else: print("Neplatná volba, zkuste to znovu.")

# --- Přidat nový úkol ---
# Zadejte název úkolu: Úkol 1
# Zadejte popis úkolu: Popis pro úkol 1
# Výstup: Úkol ´Úkol 1´ byl přidán. 
nazev = "Úkol 1"
popis = "Popis pro úkol 1"

def pridat_ukol():
    while True: 
        nazev = input("Zadejte název úkolu: ")
        popis = input("Zadejte popis úkolu: ")

        if nazev and popis: 
            ukoly.append({"nazev": nazev, "popis": popis})
            print(f"Úkol ´{nazev}´ byl přidán.")
            break
        else: 
            print("Název i popis úkolu musí být zadány. Zkuste to znovu.")

# --- Zobrazit všechny úkoly ---
def zobrazit_ukoly():
    if not ukoly: 
        print("Žádné úkoly k zobrazení. ")
    else: 
        print("Seznam úkolů:")
        for index, ukol in enumerate(ukoly, start=1):
            print(f"{index}. {ukol['nazev']} - {ukol['popis']}")

# --- Odstranit úkol ---
def odstranit_ukol():
    if not ukoly: 
        print("Žádné úkoly k odstranění.")
        return
    zobrazit_ukoly()
    while True:
        try:
            index = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            if 1 <= index <= len(ukoly):
                odstraneny_ukol = ukoly.pop(index - 1)
                print(f"Úkol ´{odstraneny_ukol['nazev']}´ byl odstraněn.")
                break
            else: 
                print("Neplatné číslo úkolu. Zkuste to znovu.")
        except ValueError: 
            print("Prosím zadejte platné číslo.")

# --- Spuštění programu ---
hlavni_menu()

    




       

