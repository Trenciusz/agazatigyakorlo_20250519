mennyi_penz = int(input("Írd be, hogy mennyi pénzed van: "))

while True:
    mennyit_kolteni = int(input("Mennyit szeretnél költeni belőle: "))
    if mennyi_penz - mennyit_kolteni>=0:
        mennyi_penz -= mennyit_kolteni
        print(f"Ennyi pénzed maradt: {mennyi_penz}")
        if mennyi_penz == 0:
            break
    else:
        print("Ennyit nem költhetsz, nincs ennyi pénzed!")

#Hibás a feladatlapon a minta, csak azért töltöttem el vele ennyi időt