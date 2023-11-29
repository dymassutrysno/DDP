#Nomor 1

hasil_akhir = [
    {"nama":"Reza", "nilai":70},
    {"nama":"Ciut", "nilai":63},
    {"nama":"Dian", "nilai":80},
    {"nama":"Badu", "nilai":40}
]

def predikatlulus(data):
    lulus = [mahasiswa["nama"]
             for mahasiswa in data
             if mahasiswa["nilai"] > 65]
    return lulus
hasil = predikatlulus(hasil_akhir)
print("Siswa yang lulus :", hasil)

#Nomor 2

buah = ["pepaya", "pisang", "durian", "jambu"]

def list_buah(buah):
    list_terbalik = []
    for a in range(len(buah) -1,-1,-1):
        list_terbalik.append(buah[a])
    return list_terbalik
hasil = list_buah(buah)
print(hasil)

#Nomor 3

buah = ["pepaya", "pisang", "durian", "jambu"]

def duplikat(buah):
    duplikat = []
    for a in buah:
        duplikat.append(a)
        duplikat.append(a)
    return duplikat
hasil = duplikat(buah)
print(hasil)

#Nomor 4

kalimat = "Nurul Fikri"

def konsonan(kalimat):
    konsonan = "" # "" harus sama dengan variabel yang atas, selain dengan "" bisa juga dengan []
    for a in kalimat:
        if a not in "aiueo":
            konsonan += a
    return konsonan
hasil = konsonan(kalimat)
print(hasil)