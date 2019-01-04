"""
s#a = input ("1.sayıyı giriniz :")
#b = input ("2.sayıyı giriniz :")
#c = input ("3.sayıyı giriniz :")
#print ("sayıların toplamı",int(a)+int(b)+int(c))
print("Aile Tablosuna Hoş Geldiniz :) ")
abla=input("Abla Adı Giriniz :")
kardes=input("Kardeş Adı Giriniz :")
print("LODİNG....".readline())

list=[abla,kardes]
print("Yükleme Tamamlandı Enter tuşuna Basınız...")
print("Abla Adı :",abla)
print("Kardeş Adı :",kardes)
print("Teşekkürler")


nott=float(input("Notnuzu Giriniz :"))

if nott>=90:
    print("AA")
elif nott>=75:
    print("BB")
elif nott>=60:
    print("CC")
elif nott>=50:
    print("DD")
elif nott>=35:
    print("FF")
else:

    print("kaldı")
"""
kullanıcıadı="tahir"
sifre="123"
kullanıcıAdı=input("Kullanıcı Adı Giriniz :")
sifree=input("Sifre Giriniz:")
if (kullanıcıadı==kullanıcıAdı)and(sifree==sifre):
    print("Hoş Geldin")
elif (kullanıcıadı!=kullanıcıAdı)and(sifree==sifre):
    print("Kullanıcı Adı Hatalı!!")
elif (kullanıcıadı==kullanıcıAdı)and(sifree!=sifre):
    print("Şifre Hatalı!!")
elif (kullanıcıadı!=kullanıcıAdı)and(sifree!=sifre):
    print("Tekrar Deneyiniz :( ")
