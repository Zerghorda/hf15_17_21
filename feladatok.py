def fel15():
    print("15.feladat")
    szam1: int = int(input("Adjo egy valos számot!"))
    szam2: int = int(input("Adjon még egy számot!"))
    while szam1 < 0 or szam2 < 0:
        print("Hiba: a téglalap oldalai nem pozitívak!")
        szam1: int = int(input("Adjo egy valos számot!"))
        szam2: int = int(input("Adjon még egy számot!"))
    terulet = szam1 * szam2
    kerulet = (szam1+szam2)*2
    print(f"'A' oldal: {szam1}, 'B' oldal: {szam2}, Téglalap területe: {terulet}, Téglalap kerülete: {kerulet}")


def fel17(szam):
    print("17.feladat")
    if szam < 10:
        print(f"{szam} nem kétjegyű szám")
    elif szam >= 10:
        print(f"{szam} kétjegyű szám")


def fel21(szam1, szam2, szam3):
    print("21.feladat")
    if szam1 < szam2 and szam1 < szam3:
        print(f"{szam1} a legkisebb szám!")
    elif szam2 < szam1 and szam2 < szam3:
        print(f"{szam2} a legkisebb szám!")
    elif szam3 < szam1 and szam3 < szam2:
        print(f"{szam3} a legkisebb szám!")
