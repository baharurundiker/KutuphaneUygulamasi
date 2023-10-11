import sys

kitap_listesi = ["Kürk Mantolu Madonna","Şeker Portakalı","Dönüşüm"]
menü = """

1)Kitap Ekle

2)Kitap Çıkar

3)Kitapları Görüntüle

Q)Uygulamadan Çıkış

"""
def kitapEkle(liste,kitap):
    liste.append(kitap)
    print("Kitap başarıyla eklendi!")
    input('Ana menüye geri dönmek için enter\'a basınız.')

def kitapCikar(liste,kitap):
    if kitap in liste:
        liste.remove(kitap)
        print("Kitap başarıyla çıkarıldı!")
    else:
        print("Kitap listede bulunamadı!")
    input("Ana menüye geri dönmek için Enter'a basınız.")


def kitapGoster(liste):
    for a in liste:
        print("Kitap Listesi ------\n",a)

def cikis():
    print("Uygulamadan çıkış yapılıyor...\n")
    sys.exit()

while True:
    print(menü)
    secim = input("Seçiminizi giriniz\n")
    if secim == "1":
        kitapAdi = input("Kitap adını giriniz\n")
        kitapEkle(kitap_listesi,kitapAdi)
    elif secim == "2":
        kitapAdi = input("Kitap adını giriniz\n")
        kitapCikar(kitap_listesi, kitapAdi)
    elif secim == "3":
        kitapGoster(kitap_listesi)
    elif secim == "Q" or secim == "q":
      cikis()
    else:
        print("Hatalı giriş yaptınız lütfen tekrar deneyin!")
        input("Ana menüye dönmek için enter'a basınız...")

























