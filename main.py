MAX_KELIME_UZUNLUGU = 70  # Türkçede bir kelimenin alabileceği max kelime uzunluğu
MIN_KELIME_UZUNLUGU = 0   # Türkçede bir kelimenin alabileceği min kelime uzunluğunun bir eksiği


def noktalamayi_kaldir(metin_par):  # kullanıcıdan alınan metindeki özel karakterlerin ve noktalama işaretlerinin kaldırılması
    ozel_karakterler = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''  # özel karakterler ve noktalama işaretleri
    noktalamasiz_metin = ""
    for kar in metin_par:  # metindeki her bir karakterin tek tek kontrol edilmesi
        if kar not in ozel_karakterler:   # bulunan karakter özel karakter veya noktalama işareti değilse boş metine sırayla eklenir
            noktalamasiz_metin = noktalamasiz_metin + kar  # uygun karakterin yeni metine aktarılması
    return noktalamasiz_metin  # metnin geriye döndürülmesi


def kucuk_harfe_cevir(metin_par):  # metindeki harflerin küçük harfe çevrilmesi
    return metin_par.replace("İ", "i").replace("I", "ı").lower()  # metnin geriye döndürülmesi
    # I ve İ harfleri Türkçenin özel durumundan dolayı özel olarak küçük harfe çevrilir.


def gereksiz_kelimeleri_al():  # dokümanda verilen linkten indirilen txt dosyasındaki gereksiz kelimelerin okutulması
    try:  # dosyanın açılıp açılmadığının kontrol edilmesi
        kelime_dos = open("stop_words_turkish.txt", "r", encoding="utf-8")  # dosyanın açılması
        gereksiz_kelimeler = kelime_dos.readlines()  # dosyanın satır satır okunup listeye atılması
        for i in range(len(gereksiz_kelimeler)):  # gereksiz kelimelerin tek tek dolaşılması
            gereksiz_kelimeler[i] = gereksiz_kelimeler[i].rstrip()  # gereksiz kelimelerin sonlarındaki boşluk karakterinin silinmesi
        kelime_dos.close()  # dosyanın kapatılması
        return gereksiz_kelimeler  # gereksiz kelime listesinin geri döndürülmesi
    except IOError:  # dosya açılmazsa çalışan blok
        print("dosya açılamadı!")


def gereksiz_kelimeleri_cikar(yeni_metin_par, gereksiz_kelimeler_par):  # metinden gereksiz kelimelerin çıkarılması
    kelimeler = yeni_metin_par.split()  # metindeki her bir kelimenin listeye atılması
    for kelime in kelimeler:  # metindeki her bir kelimenin dolaşılması
        if kelime in gereksiz_kelimeler_par or len(kelime) > MAX_KELIME_UZUNLUGU:  # kelimenin gereksiz kelime veya 70 harften büyük olmasının konrolü
            kelimeler.remove(kelime)  # kelimenin gereksiz bir kelimeyse ya da 70 harften büyükse listeden çıkarılması
    return kelimeler  # kelime listesinin döndürülmesi


def kelime_sayilarini_bul(kelime_say_par, kelimeler_par):  # kelime listesindeki her bir elemanın tekrar sayısının bulunması
    for kelime in kelimeler_par:  # kelimelerin tek tek dolaşılarak sözlüğe atılması
        if kelime in kelime_say_par:   # kelimenin sözlüğün içinde olma durumunun kontrolü
            kelime_say_par[kelime] += 1  # kelime sözlüğün içindeyse valuesi 1 arttırılır
        else:
            kelime_say_par[kelime] = 1  # kelime sözlükte yoksa yeni key,value oluşturulur


def kelime_uzunlugu_bul(kelime_say_par, kelime_uzunlugu_par):  # her bir kelimenin uzunluğunun bulunması
    for kelime in kelime_say_par:  # her bir kelimenin liste içerisinde dolaşılması
        kelime_index = len(kelime)  # her bir kelimenin uzunluğunun bulunması
        kelime_uzunlugu_par[kelime_index-1] += kelime_say_par[kelime]  # uzunluğu bulunan kelimenin boş listeye indexine göre atılması


def metni_yazdir(kelimeler_par):  # metnin yazdırılması
    print("Noktalama işaretleri ve gereksiz kelimeler çıkarıldıktan sonra küçük harflerle kalan metin:")
    print(" ".join(kelimeler_par))  # listedeki kelimelerin birleştirilmesi ve yazdırılması


def tekrar_sayisini_yazdir(kelime_say_par):  # kelimelerin ve tekrar sayılarının yazdırılması
    print("Kalan metindeki kelimeler ve tekrar sayıları:")
    print("Kelime".ljust(74), "Tekrar Say")  # tablonun şekillendirilmesi
    print("-------------------------------------------------------------------------  ----------")
    for kelime in kelime_say_par:  # liste içindeki her bir kelimenin dolaşılması
        print(format(kelime, "80"), end="")  # her bir kelimenin yazdırılması
        print(kelime_say_par[kelime])  # her bir kelimenin tekrar sayılarının yazdırılması


def kelime_uzunlugunu_yazdir(kelime_uzunlugu_par):  # her bir farklı kelimenin uzunluğunu ve o uzunluktaki kelime sayılarının yazdırılması
    print("Kalan metindeki her uzunluktaki kelime sayıları:")
    print("Uzunluk".ljust(10), "Kelime Say")
    print("-------    ----------")
    for i in range(len(kelime_uzunlugu_par)):  # her bir kelime sayısı kadar listenin dolaşılması
        if kelime_uzunlugu_par[i] > MIN_KELIME_UZUNLUGU:  # kelime uzunluğu listesindeki 0 değerlerinin kontrolü
            print(str(i+1).ljust(15), end="")  # kelimenin uzunluğunun yazdırılması
            print(kelime_uzunlugu_par[i])  # o uzunluktaki kelime sayılarının yazdırılması


def main():  # ana fonksiyon
    metin = input("Türkçe bir metin giriniz:\n")  # kullanıcıdan Türkçe metin alınması
    noktalamasiz_metin = noktalamayi_kaldir(metin)  # noktalama işaretlerini kaldıran fonksiyonun çağırılması
    yeni_metin = kucuk_harfe_cevir(noktalamasiz_metin)  # metnin her harfini küçük harfe çeviren fonksiyonun çağırılması
    gereksiz_kelimeler = gereksiz_kelimeleri_al()  # txt dosyasında gereksiz kelimeleri alan fonksiyonun çağırılması
    kelimeler = gereksiz_kelimeleri_cikar(yeni_metin, gereksiz_kelimeler)  # metninden gereksiz kelimeleri ve 70 harften uzun kelimeleri çıkaran fonksiyonun çağırılması
    kelime_say = {}  # kelimelerin ve tekrar sayılarının içinde bulunduğu sözlüğün oluşturulması
    kelime_sayilarini_bul(kelime_say, kelimeler)  # her bir kelimeyi ve tekrar sayısını bulan ve sözlüğe atan fonksiyonun çağırılması
    kelime_uzunlugu = [0]*MAX_KELIME_UZUNLUGU  # kelime uzunluğuna göre indexlenen listenin oluşturulması
    kelime_uzunlugu_bul(kelime_say, kelime_uzunlugu)  # her bir kelimenin uzunluğunu bulup o indexe göre index değerini arttıran fonksiyonun çağırılması
    metni_yazdir(kelimeler)  # noktalamasız, küçük harfe çevrilmiş ve gereksiz kelimeler atılmış olan metnin yazdırılması
    print("")
    tekrar_sayisini_yazdir(kelime_say)  # her bir kelimeyi ve tekrar sayısını yazdıran fonksiyonun çağırılması
    print("")
    kelime_uzunlugunu_yazdir(kelime_uzunlugu)  # her bir kelimenin uzunluğuna göre sayılarını yazdıran fonskiyonun çağırılması


main()  # ana fonksiyonun çağırılması
