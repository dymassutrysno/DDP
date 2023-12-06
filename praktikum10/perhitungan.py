import math

# tambah
def tambah(bil1, bil2):
    hasil = bil1+bil2
    print("hasil tambah dari",bil1,"+",bil2,"=",hasil)

# kurang
def kurang(bil1, bil2):
    hasil = bil1-bil2
    print("hasil pengurangan dari",bil1,"-",bil2,"=",hasil)

# kali
def kali(bil1, bil2):
    hasil = bil1*bil2
    print("hasil perkalian dari",bil1,"*",bil2,"=",hasil)

# bagi
def bagi(bil1, bil2):
    hasil = bil1/bil2
    print("hasil pembagian dari",bil1,"/",bil2,"=",hasil)

# pangkat
def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print("hasil pemangkatan dari",bil1,"^",bil2,"=",hasil)

    # akar
def akar(bil1):
    hasil = math.sqrt(bil1)
    print("hasil akar dari", bil1, "=", hasil)

# sin cos tan
# a= sisi alas/sisi samping
# b= sisi depan/sisi tinggi
# c= sisi miring
def sin(b, c):
    hasil = b/c
    print("hasil sin a", b, "/", c, "=", hasil) 

def cos(a, c):
    hasil = a/c
    print("hasil cos a", a, "/", c, "=", hasil)    

def tan(a, b):
    hasil = b/a
    print("hasil tan a", b, "/", a, "=", hasil)

# log
def log(bil1):
    hasil = math.log(bil1)
    print("hasil dari log", bil1, "=", hasil)