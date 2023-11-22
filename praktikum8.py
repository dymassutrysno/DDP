#Nomor 1
def profil():
    print("nama saya adalah", nama, 
          "\nalamat saya adalah", alamat, 
          "\ngender saya adalah", gender,
          "\numur saya adalah", umur,
          "\nhobi saya adalah", hobi)

nama = "Dymas Sutrysno"
alamat = "Bogor"
gender = "Pria"
umur = "20 Tahun"
hobi = "Bermain gitar"

profil()

#Nomor 2
def grade(nilai):
    if nilai <= 60:
        return "Gagal"
    elif 61<= nilai <= 70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat baik"
    elif 81 <= nilai <= 100:
        return "Sempurna"
    else :
        return "tidak ada keterangan nilai"
nilai = 60
print(grade(nilai))

#Nomor 3
def bilangan_ganjil(i):
    for i in range (1, i+1, 2):
        print(i)
bilangan_ganjil(100)