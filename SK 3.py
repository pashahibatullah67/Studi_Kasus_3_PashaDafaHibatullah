buku = ("Rumus kimia anak TK", "TKA untuk anak TK", "Cara menjadi cewek sadboy", "Kehidupan si Asep", "Budi, ini arahnya kemana?")
list_peminjaman = []
print(buku)

while True:
    nama_buku = input("Masukkan aja nama buku yang pengen dipinjam dan kalo udah selesai ketik aja selesai boss : ")
    if nama_buku.lower() == "selesai":
        break
    if nama_buku in buku:
        print ("buku bisa dipinjam bosku")
        list_peminjaman.append(nama_buku)
    else:
        print("bukunya ga ada bosku")

hapus_buku = input("Ada mau menghapus buku dari list kah bos? Masukkan aja namanya, kalau gaada ketik aja (ga ada) : ")

if hapus_buku.lower() == "ga ada":
    print("Oke bos, ga ada yang dihapus ya jadinya")
elif hapus_buku in list_peminjaman:
    list_peminjaman.remove(hapus_buku)
    print("buku berhasil dihapus dari list bosku")
else:
    print("bukunya ga ada di list peminjaman atau belum dipinjam bosku")
print(list_peminjaman)