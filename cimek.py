#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""2014.majus.13 Informatika emelt szintu erretsegi megoldas Python programozasi nyelven."""
"""1. feladat: szoveg beimportalasa amit en szotarba gondoltam megoldani.Ami a kovetkezo keppen nezne ki.:
ip={
hanyadik cim:{
"Beolvasot ip":2001:0db8:03cd:0000:0000:ef45:0006:0123
"elso rovidites":2001:db8:3cd:0:0:ef45:6:123 #bevezeto 0-llak elhagyasa.
"kettes rovidetes":2001:db8:3cd::ef45:6:123 #kettovel vagy tobb nulla eseten le lehet egyszerusiteni ket egymas mellet allo kettospont kozotti ures reszre.
az elozo modszert csak egyszer lehet hasznalni a kodban.

 }
}
"""
def egyszerusito(sor):
    s = sor.split(":")
    vissza = []
    for a in s:
        if a[0:3] == "000":
            vissza.append(a[3:])
        elif a[0:2] == "00":
            vissza.append(a[2:])
        elif a[0:1] == "0":
            vissza.append(a[1:])
        elif a == '0000':
            vissza.append("0")
        else:
            vissza.append(a)
    if sor == ":".join(vissza):
        visszaad = 'Nem roviditheto tovabb'
    else:
        visszaad = ":".join(vissza)
    return visszaad

def rovidebb(egy):
    
    if ':0:0:0:0:0:0:' in egy:
        return egy[:egy.index(':0:0:0:0:0:0:')]+'::'+egy[egy.index(':0:0:0:0:0:0:')+13:]
    elif ':0:0:0:0:0:' in egy:
        return egy[:egy.index(':0:0:0:0:0:')]+'::'+egy[egy.index(':0:0:0:0:0:')+11:]
    elif ':0:0:0:0:' in egy:
        return egy[:egy.index(':0:0:0:0:')]+'::'+egy[egy.index(':0:0:0:0:')+9:]
    elif ':0:0:0:' in egy:
        return egy[:egy.index(':0:0:0:')]+'::'+egy[egy.index(':0:0:0:')+7:]
    elif ':0:0:' in egy:
        return egy[:egy.index(':0:0:')]+'::'+egy[egy.index(':0:0:')+5:]
    
    return "Nem roviditheto tovabb"

def fajta(sor):
    if sor[0:9] == "2001:0db8":
        vissza = 'dokumentacios cim'
    elif sor[0:7] == "2001:0e":
        vissza = 'globalis egyedi'
    elif sor[0:2] == 'fc' or sor[0:2] == 'fd':
        vissza = 'helyi egyedi'
    return vissza
    
ip = {}
n = 0
with open("ip.txt","rt+", encoding="utf-8") as f:
    for s in f:
        n+=1
        sor = s.replace("\n", "")
        ip[n] = {}
        ip[n]["Beolvasott ip"] = sor
        ip[n]["elso rovidetes"] = egyszerusito(sor)
        ip[n]['masodik'] = rovidebb(egyszerusito(sor))
        ip[n]['fajta'] = fajta(sor)
        ip[n]['nullak szama'] = sor.count("0")
#print(ip)
"""
with open("sem.txt", "wt", encoding='utf-8') as g:
    for k,v in ip.items():
        g.write("{0}:{1} \n".format(k,v))
"""        
print("2. feladat")
"""Ki kell iratni hogy hany adatrorvan az allomanyban."""
print("Az allomanyban {} darab adatsor van.\n".format(len(ip)))

print("3. feladat")
"""Legalacsonyabb Ip cimat ki kell iratni. """
print("A legalacsonyabb tarolt IP-cim:\n{}\n".format(min([k["Beolvasott ip"]for k in ip.values()])))

print("4. feladat")
"""Meg kell szamolni hogy hany dokumentacios cim hany hely es hany globalis egyebet nem kell kiiratni. """
egy = 0
ketto = 0
harom = 0
for a in ip.values():
    if a["fajta"] == 'dokumentacios cim':
        egy+=1
    elif a["fajta"] == 'globalis egyedi':
        ketto+=1
    elif a["fajta"] == 'helyi egyedi':
        harom+=1
print("Dokumentacios cim: {0}\nGlobalis egyedi cim:{1}\nHelyi egyedi cim:{2}\n".format(egy, ketto, harom))


#print("5. feladat")
"""ki kell gyujteni a sok.txt alomanyba azokat az ip cimeket mik legalabb 18 nullat tartalmaznak. """
with open("sok.txt", "wt", encoding='utf-8') as g:
    for k,v in ip.items():
        if v["nullak szama"] >= 18:
            g.write("{0}:{1} \n".format(k,v['Beolvasott ip']))

print("6. feladat")
"""sorszamot be kell kerni a felhasznalotol """
sorszam = int(input("Kerek egy sorszamot: "))
print("{0}\n{1}\n".format(ip[sorszam]['Beolvasott ip'],ip[sorszam]["elso rovidetes"]))

print("7. feladat")
"""Elozo bekeret ip cimet tovabb roviditeni."""
print("{0}\n".format(ip[sorszam]['masodik']))

#print(rovidebb(ip[sorszam]["elso rovidetes"]))
