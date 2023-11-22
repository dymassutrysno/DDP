#UTS No 5
a = int(input("masukan angka 1 = "))
b = int(input("masukan angka 2 = "))
c = ('''
        pilih salah satu operator dibawah
     =======================================
          + = tambah
          - = kurang
          * = kali
          / = bagi
          ** = pangkat
''')
print(c)
d = str(input("pilih operator diatas = ").lower())
if d == "tambah":
    hasil = a + b
elif d == "kurang":
    hasil = a - b
elif d == "kali":
    hasil = a * b
elif d == "bagi":
    hasil = a / b
elif d == "pangkat":
    hasil = a ** b
else :
    print("salah masukan operator")

print("angka pertama = ", a)
print("angka kedua = ", b)
print("pilihan operator = ", d)
print("hasil operator = ", hasil)