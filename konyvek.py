konyvek = []

with open("..//fajlok//konyvek-adatok.txt", "r", encoding="UTF-8") as forrasfajl:
    hanyadik_sor = 1
    for sor in forrasfajl:
        if hanyadik_sor >1: 
            konyvek.append(sor.strip().split(";"))   
        hanyadik_sor += 1

print(f"A listában {len(konyvek)} db könyv található!")

mufaj = str(input("Írj be egy műfajt: "))
hany_mufaj_egyezik = 0

for konyv in konyvek:
    if konyv[1].lower() == mufaj.lower():
        hany_mufaj_egyezik += 1

print(f"{hany_mufaj_egyezik} db könyv tartozik ebbe a műfajba")

van_e_szinmu = False

for konyv in konyvek:
    if int(konyv[3])>=1600 and int(konyv[3])<=1699:
        if konyv[1].lower() == "színmű":
            van_e_szinmu = True

if van_e_szinmu == True:
    print(f"1600 és 1699 között van színű műfajban írt könyv")
else:
    print(f"1600 és 1699 között nincs színmű műfajban írt könyv")

def hossz(lista, konyv_cime):
    rovid = 0
    kozep = 1
    hosszu = 2
    for konyv in lista:
        if konyv[0] == konyv_cime:
            if konyv[2] < 200:
                return rovid
            elif konyv[2] >= 200 and konyv[2] <= 600:
                return kozep
            else:
                return hosszu
            
#Teljesen elfelejtettem hogy kell írni fáljba, úgyhogy az 5. feladat most nem létezik