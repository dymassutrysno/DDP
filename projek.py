import tkinter as tk

def hitung_hasil():
    nama = str(entry_nama.get())
    nomor = int(entry_nomor.get())
    kota = str(entry_kota.get())
    kecamatan = str(entry_kecamatan.get())
    pos = int(entry_pos.get())
    rt = int(entry_rt.get())
    rumah = entry_rumah.get()
    detail = entry_detail.get()
    barang = int(entry_barang.get())
    berat = int(entry_berat.get())

    if barang == 1:
        hasil = 15000 * berat
    elif barang == 2:
        hasil = 600 * berat
    elif barang == 3:
        hasil = 4000 * berat
    elif barang == 4:
        hasil = 2500 * berat
    elif barang == 5:
        hasil = 13000 * berat
    elif barang == 6:
        hasil = 1300 * berat
    elif barang == 7:
        hasil = 2000 * berat
    elif barang == 8:
        hasil = 1500 * berat
    elif barang == 9:
        hasil = 35000 * berat
    elif barang == 10:
        hasil = 1000 * berat
    else:
        hasil = "Tidak memilih barang"

    result_label.config(text=f"Nama : {nama}, Nomor Handphone : {nomor}, Kota/Kabupaten : {kota}, Kecamatan : {kecamatan}, Kode Pos : {pos}, Rt/Rw : {rt}, Nomor Rumah : {rumah}, Detail Lainnya : {detail}, Barang : {barang}, Berat : {berat}, Hasil : {hasil}")

root = tk.Tk()
root.title("Aplikasi Penjualan Sampah Daur Ulang")

label_nama = tk.Label(root,text ="Nama")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

label_nomor = tk.Label(root,text ="Nomor Handphone")
label_nomor.pack()
entry_nomor = tk.Entry(root)
entry_nomor.pack()

label_kota = tk.Label(root,text ="Kota/Kabupaten")
label_kota.pack()
entry_kota = tk.Entry(root)
entry_kota.pack()

label_kecamatan = tk.Label(root,text ="Kecamatan")
label_kecamatan.pack()
entry_kecamatan = tk.Entry(root)
entry_kecamatan.pack()

label_pos = tk.Label(root,text ="Kode Pos")
label_pos.pack()
entry_pos = tk.Entry(root)
entry_pos.pack()

label_rt = tk.Label(root,text ="Rt/Rw")
label_rt.pack()
entry_rt = tk.Entry(root)
entry_rt.pack()

label_rumah = tk.Label(root,text ="Nomor Rumah")
label_rumah.pack()
entry_rumah = tk.Entry(root)
entry_rumah.pack()

label_detail = tk.Label(root,text ="Detail Rumah")
label_detail.pack()
entry_detail = tk.Entry(root)
entry_detail.pack()

label_barang = tk.Label(root,text ="""
    1. Alumunium Rp 15.000,-/kg
    2. Beling Rp 600,-/kg
    3. Besi tua Rp 4.000,-/kg
    4. Botol plastik Rp 2.500,-/kg
    5. Minyak Jelantah Rp 13.000,-
    6. Kaleng Rp 1.300,-/kg
    7. Kardus Rp 2.000,-/kg
    8. Kertas Buku, Majalah dan Koran Rp 1.500,-/kg
    9. Kuningan Rp. 35.000,-/kg
    10. Seng Rp 1.000,-/kg
        Pilih Sesuai Nomor""")
label_barang.pack()
entry_barang = tk.Entry(root)
entry_barang.pack()

label_berat = tk.Label(root,text ="Berat")
label_berat.pack()
entry_berat = tk.Entry(root)
entry_berat.pack()

hitung_button = tk.Button(root, text="Submit", command=hitung_hasil)
hitung_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()