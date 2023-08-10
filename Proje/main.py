import pandas as pd
import numpy as np
from random import randint

urunadi = ""
gram = 0
stok = 0
fiyat = 0
urunlistesi = []
urungramaj = []
urunstok = []
urunfiyat = []

sayac = 0
eklenenmalzeme = []
silinenmalzeme = []


def Menu():
    print("\n\t\t\tHosgeldiniz...\na)Depo islemleri:\n\t1)Urun ekle\n\t2)Urun sil\n\t3)Urunleri goster")
    print("b)Yemek islemleri\n\t4)Yemek ekle\n\t5)Yemek sil\n\t6)Yemekleri goster\n\t7)Malzemeleri goster")
    print("c)Yemek secme islemi\n\t8)Yemekleri goster\n\t9)Yemek secme ve secilen yemegin bilgilerini gosterme")
    print("Cikis icin herhangi bir tus giriniz")

def ft_Depo():  #   Verileri dataframe'e çevirip txt dosyasına aktarma (YAZDIRMA)
    veriler = {
        "Urun adi": urunlistesi,
        "Agirlik(gr)": urungramaj,
        "Stok": urunstok,
        "Fiyat": urunfiyat
        }
    df = pd.DataFrame(veriler)
    with open("depo.txt","w") as depo:
        depo.write(str(df))

#       ÜRÜN EKLE
def urunekle():
    sayac = int(input("Kac urun eklemek istediginizi girin : "))
    while (sayac > 0):
        urunadi = input("Urun adi giriniz : ")
        urunlistesi.append(urunadi)
        gram = int(input("Kac gram oldugunu giriniz : "))
        urungramaj.append(gram)
        stok = int(input("Stok adedi giriniz :"))
        urunstok.append(stok)
        fiyat = int(input("Fiyat bilgisi giriniz :"))
        urunfiyat.append(fiyat)
        sayac -= 1

#       ÜRÜN GÖSTER
def urunleriGoster():
    with open("depo.txt","r") as rdepo:
        rdepo = rdepo.read()
        print("\n" + rdepo)

#       ÜRÜN SİLME
def urunSil():
    urunleriGoster()
    indexsil = input("Silmek istediginiz urunun ismini giriniz...")
    df = pd.read_csv("depo.txt")
    indexnum = urunlistesi.index(indexsil)
    urunlistesi.pop(indexnum)
    urunfiyat.pop(indexnum)
    urungramaj.pop(indexnum)
    urunstok.pop(indexnum)
    ft_Depo()
    urunleriGoster()

def malzemeEkleSil():
    pass

def yemekEkle():
    appendyemek = input("Eklemek istediginiz yemegin adini giriniz :\n")
    with open("yemekcesit.txt","a") as yemek:
        yemek.write("\n")
        yemek.write(appendyemek)
    print(" *** Guncel yemek listesi ***\n")
    with open("yemekcesit.txt","r") as yemekl:
        yemekl = yemekl.read()
        print(yemekl)

def yemekSil():
    secimyemek = input("Silmek istediginiz yemegin adini giriniz :")
    with open("yemekcesit.txt","r") as yemek:
        b = yemek.readlines()
    with open("yemekcesit.txt","w") as yemek:
        for c in b:
            if (c.strip("\n")) != secimyemek:
                yemek.write(c)

def yemeklerGoster():
    with open("yemekcesit.txt","r") as yemek:
        yemek = yemek.read()
        print(yemek)

def malzemeGoster():
    with open("malzeme.txt","r") as mlz:
        mlz = mlz.read()
        print(mlz)

def syMalzemeler(stryemek):
    pass

secim = ""
while True:
    Menu()
    secim = input("Secim :")
    if secim == "1":
        urunekle()
        ft_Depo()
    elif secim == "2":
        urunSil()
    elif secim == "3":
        urunleriGoster()
    elif secim == "4":
        yemekEkle()
    elif secim == "5":
        yemekSil()
    elif secim == "6":
        yemeklerGoster()
    elif secim == "7":
        malzemeGoster()
    elif secim == "8":
        yemeklerGoster()
    elif secim == "9":
        yemeklerGoster()
        secilenyemek = input("Secmek istediginiz yemegi giriniz :")
        print(f"\n\nSecilen yemek {secilenyemek} \n")
        syMalzemeler()
    else:
        break
