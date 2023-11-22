#NO 1
a = input("Nama Kendaraan ?")
b = input("jenis bensin ?")
c = input("kota yang dituju ?")

if b == ("pertalite"):
    harga = 10.000
    jarak = 12
elif b == ("pertamax"):
    harga = 14.000
    jarak = 13
elif b == ("pertamax turbo"):
    harga = 17.000
    jarak = 13.5
#kota tuju
if c == ("jakarta"):
    j = 20
elif c == ("bekasi"):
    j = 35.7
elif c == ("depok"):
    j = 5
elif c == ("tanggerang"):
    j = 99
elif c == ("bogor"):
    j = 120.6
else:
    ('tidak ada tujuan yang dipilih')

hasil = j/jarak
h = hasil*harga
print("jenis bensin", b,"harganya", harga,"jaraknya", jarak,"KM", "Kota tujuan", c, "berjarak", j, "KM", "pemakaian bensin", hasil, "total harga bensin", h)

#NO 2
j = input("Nama Pembeli")
k = input("Nomor HP pembeli")
l = input("pesan menu apa")
m = input("masukan pesan")
n = input("jumlah pesanan")

if l == ("makanan"):
    ng = "nasi goreng"
    mg = "mie goreng"
    ag = "ayam goreng"

#NO3
