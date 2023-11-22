# Soal No 1
# JARAK TEMPUH
# lower mengubah alfabet pada sebuah kata atau kalimat menjadi huruf kecil(tidak berpengaruh huruf kecil atau besar).
nama_kendaraan = input ('masukan nama kendaraan ? ')
jenis_bensin = input ('masukan jenis bensin ? ').lower()
kota = input ('masukan kota ? ').lower()

if jenis_bensin == 'pertalite':
    harga = 10000
    jarak_tempuh = 12
elif jenis_bensin == 'pertamax':
    harga = 14000
    jarak_tempuh = 13 
elif jenis_bensin == 'pertamax turbo':
    harga = 17000
    jarak_tempuh = 13.5
else :
    print('salah masukan bahan bakar')


if kota == 'jakarta':
    jarak = 20
elif kota == 'bekasi':
    jarak = 35.7
elif kota == 'depok':
    jarak = 5
elif kota == 'tangerang':
    jarak = 99
elif kota == 'bogor':
    jarak = 120.6
else :
    print('salah masukan kota')

pemakaian_bensin = jarak / jarak_tempuh
total_harga = pemakaian_bensin * harga

print('nama kendaraan ',nama_kendaraan)
print('jenis bensin ', jenis_bensin)
print('kota yang dituju ',kota)
print('pemakaian bensin ', (pemakaian_bensin), 'liter')
print('total harga bensin ', (total_harga), 'rupiah')

#Soal No 2
# MENU MAKANAN
# lower mengubah alfabet pada sebuah kata atau kalimat menjadi huruf kecil(tidak berpengaruh huruf kecil atau besar).
nama = input ('masukan nama pembeli? ')
nohp = input ('masukan nohp pembeli? ')
pesanMenu = input ('masukan menu makanan atau minuman ? ').lower()

if pesanMenu == 'makanan':
    print('''menu makanan 
    ===========================
    1. nasi goreng harga 15.000
    2. mie goreng harga 12.000
    3. ayam geprek harga 18.000
    ''')
elif pesanMenu == 'minuman':
    print('''menu mimuman 
    ===========================
    1. aneka jus harga 15.000
    2. soft drink harga 10.000
    3. sweet ice tea harga 5.000
    ''')
else :
    print('salah masukan menu')

pesanan = input ('masukan pesanan ? ').lower()
jumlah = int (input ('masukan jumlah pesanan ? '))

if pesanan == 'nasi goreng':
    harga = 15000
elif pesanan == 'mie goreng':
    harga = 12000
elif pesanan == 'ayam geprek':
    harga = 18000
elif pesanan == 'aneka jus':
    harga = 15000
elif pesanan == 'soft drink':
    harga = 10000
elif pesanan == 'sweet ice tea':
    harga = 5000
else :
    print('salah masukan pesanan')

total = harga * jumlah

print('nama pembeli ',nama)
print('no Hp ',nohp)
print('menu yang di pesan ', pesanan)
print('jumlah pesanan ',jumlah)
print('total harga yang harus di bayar ', '{:,.0f}'.format(total), ' rupiah')

# Soal Kuiz 3
for i in range(1, 21):
    if i % 3 == 0:
        print("STT Nurul Fikri")
    else:
        print(i)

