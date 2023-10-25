#Append dan Insert

kendaraan = ["Kawasaki Ninja","Motor","636cc","Hijau","Roda Dua"]

print(kendaraan)

kendaraan.append("Rp 340.000.000")
kendaraan.append("Ninja ZX-6R")

kendaraan.insert(2,"Kawasaki")
print(kendaraan)

#program python match case

ket = '''selamatdatang di aplikasi menghitung bangun datar
masukan pilihan :
1. untuk menghitung luas persegi
2. untuk menghitung luas lingkaran
3. untuk menghitung luas segitiga
'''

pilih = input(ket)

match pilih:
    case "1":
        print("kamu memilih 1 untuk menghitung luas persegi")
        sisi :int(input("masukan sisi? "))
        luasP : sisi*sisi
        print("luas persegi yang sisinya ",sisi,"adalah" ,luasP)
    case "2":
        print("kamu memilih 2 untuk menghitung luas lingkaran")
        jari2 = float(input("masukan jari-jari? "))
        luasL = 3.14*jari2*jari2
        print("luas lingkaran yang jari - jarinya ", jari2, "adalah", int(luasL))
    case "3":
        print("kamu memil;ih 3 untuk menghitung luas segitiga")
        alas = int(input ("masukan alas?"))
        tinggi = int(input("maasukan tinggi?"))
        luasS = 0.5 * alas * tinggi
        print("luas segitiga yang alasnya", alas, "dan tingginya", tinggi, "adalah", int(luasS))
    case _:
        print("salah memilih pilihan")