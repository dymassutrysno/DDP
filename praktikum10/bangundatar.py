# persegi
def peresegi(sisi):
    luas = sisi*sisi
    keliling = 4*sisi
    print("hasil dari Luas persegi yang sisinya", sisi, "adalah", luas)
    print("hasil dari Keliling persegi yang sisinya", sisi, "adalah", keliling)

# persegi panjang
def persegip(panjang,lebar):
    luas = panjang*lebar
    keliling = (panjang+lebar)*2
    print("hasil dari Luas persegi panjang yang panjangnya", panjang, "dan lebarnya", lebar, "adalah", luas)
    print("hasil dari Keliling persegi panjang yang panjangnya", panjang, "dan lebarnya", lebar, "adalah", keliling)

# segitiga
def segitiga(alas,tinggi,sisi1,sisi2,sisi3):
    luas = alas*tinggi
    keliling = sisi1+sisi2+sisi3
    print("hasil dari Luas segitiga yang alasnya", alas, "dan tingginya", tinggi, "adalah", luas)
    print("hasil dari Keliling segitiga yang sisinya", sisi1, sisi2, sisi3, "adalah", keliling)

# jajargenjang
def jajargenjang(alas,tinggi,b):
    luas = alas*tinggi
    keliling = (alas+b)*2
    print("hasil dari Luas jajargenjang yang alasnya", alas, "dan tingginya", tinggi, "adalah", luas)
    print("hasil dari Keliling jajargenjang yang alasnya", alas, "dan b", b, "adalah", keliling)

# layang-layang
def layang(d1,d2,a,b,c,d):
    luas = (d1*d2)/2
    keliling = a+b+c+d
    print("hasil dari luas layang-layang yang diagonal 1 nya", d1, "dan diagonal 2 nya", d2, "adalah", luas)
    print("hasil dari keliling layang-layang yang sisi 1 nya", a, "sisi 2", b, "sisi 3", c, "sisi 4", d, "adalah", keliling)

# lingkaran
def lingkaran(d):
    luas = (3.14*d**2)/4
    keliling = 3.14*d
    print("hasil dari luas lingkaran yang diameternya", d, "adalah", luas)
    print("hasil dari keliling lingkaran yang diameternya", d,"adalah", keliling)

# belah ketupat
def ketupat(d1,d2,sisi):
    luas = (d1*d2)/2
    keliling = sisi*4
    print("hasil dari luas belah ketupat yang diagonal 1 nya", d1, "dan diagonal 2 nya", d2, "adalah", luas)
    print("hasil dari keliling belah ketupat yang sisinya", sisi, "adalah", luas)