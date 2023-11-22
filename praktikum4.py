#yang false

a = "saya"
jajan = 60000

if (jajan == 40000):
     keterangan = "jajan cukup"
else:
     keterangan = "jajan berlebih"
print(a,"jajan hari ini sebesar Rp.", jajan, keterangan)

#yang true

a = "saya"
beratbadan = 68

if (beratbadan == 68):
     keterangan = "berat badan cukup"
else:
     keterangan = "olahraga bang"
print(a,"memiliki", beratbadan,"Kg" ,keterangan)

#top up game

a = input('masukan nama')
topup = 20000

if (topup < 20000):
    keterangan = "alhamdulillah banyak"
elif (topup == 20000):
    keterangan = "ngepas bet ngepas"
else:
    keterangan = "dikira banyak top up segini"
print(a,"top up game", topup, keterangan)

#menentukan nilai

nama = "Dymas Sutrysno"
prodi = "SI"
nim = "0110123055"
matkul = "DDP"
nilai = 90

if (nilai >= 90):
    keterangan = "A"
elif (nilai >= 80):
    keterangan = "B"
elif (nilai >= 70 ):
    keterangan = "C"
else:
    keterangan = "D"

print ("nama saya", nama, "prodi saya", prodi, "nim saya", nim, "dan nilai matkul", matkul, "saya", keterangan)