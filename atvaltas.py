mertekegyseg = str(input("Milyen mértékegységben adod meg: "))
atvaltando_szam = int(input("Írd be az átváltandó számot: "))

if mertekegyseg.lower() == "mb":
    print(f"Az eredmény: {atvaltando_szam/1024:.1f} GB")
else:
    print(f"Az eredmény: {atvaltando_szam*1024} MB")