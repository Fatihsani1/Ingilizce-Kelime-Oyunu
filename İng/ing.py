import random
import time
import unicodedata

print("İngilizce oyunumuza hoşgeldiniz")
time.sleep(1)

skor = 0

kelimeler = {
    "candid": "samimi",
    "ridiculous": "gülünç",
    "progress": "ilerleme",
    "barely": "zar zor",
    "raise": "arttırmak",
    "introduce": "tanıtmak",
    "drown": "boğulmak",
    "invading": "saldırmak",
    "interfere": "müdahale",
    "approach": "yaklaşmak"
}


ingkelime = list(kelimeler.keys())


random.shuffle(ingkelime)



def temizle(metin):
    metin = metin.casefold().strip()


    metin = metin.replace("ı", "i")
    metin = metin.replace("i̇", "i")


    metin = unicodedata.normalize("NFKD", metin)
    metin = "".join([c for c in metin if not unicodedata.combining(c)])

    return metin



for i in ingkelime:

    cevap = input(i + " kelimesinin türkçesini yazınız: ")

    if temizle(cevap) == temizle(kelimeler[i]):
        skor += 10
        print("Tebrikler doğru bildiniz! Skorunuz:", skor)
    else:
        skor -= 10
        print("Cevabınız yanlış!")
        print("Doğru cevap:", kelimeler[i])
        print("Skorunuz:", skor)

    time.sleep(1.5)


print("\nOyun bitti!")
print("Toplam skorunuz:", skor)

