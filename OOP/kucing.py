class Kucing:
    # atribut class
    nama = ""
    warna = ""
    umur = 0

    # constructor
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur

    # method untuk menampilkan data
    def data_kucing(self):
            print("nama kucing", self.nama)
            print("warna kucing", self.warna)
            print("umur kucing", self.umur)
