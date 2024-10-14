print(' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
print('      Nama :   Deny Candra Kasuma       ')
print('      Kelas:   Sistem Informasi A       ')
print('      Nim  :   2409116024               ')
print(' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')

# Database barang
barang_database = {}

# Menambahkan barang ke dalam database
def tambah_barang_baru(nomor_barang, nama_barang, harga_per_hari):
    barang_database[nomor_barang] = {'nama': nama_barang, 'harga_per_hari': harga_per_hari}

# Menambahkan barang-barang awal ke dalam database barang
barang_tersedia = [
    ("1", "Iphone 12 128GB", 300000),
    ("2", "Iphone 13 128GB", 370000),
    ("3", "Iphone 13 258GB", 340000),
    ("4", "Iphone 14 128GB", 500000),
    ("5", "Iphone 15 128GB", 650000), 
    ("6", "Iphone 15 258GB", 700000),
]

# Menambahkan barang-barang awal ke dalam database
for barang in barang_tersedia:
    tambah_barang_baru(*barang)

# Login
def login():
    while True:
        print("\n========================================================")
        print("\n      Selamat Datang Di Toko Deny Penyewaan Iphone      ")
        print("\n========================================================")
        print("[1] Admin")
        print("[2] Penyewa")
        print("[3] Keluar")
        pilihan = input("Silakan Pilih Mode Login: ")
        
        if pilihan == "1":
            penjual()
        elif pilihan == "2":
            penyewa()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini :)")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Admin (pemilik)
def penjual():
    while True:
        print("\n================================")
        print("\n      Selamat Datang Admin      ")
        print("\n================================")
        print("[1] Tambah Stok Barang")
        print("[2] Hapus Stok Barang")
        print("[3] Lihat Stok Barang")
        print("[4] Perbarui Stok Barang")
        print("[5] Kembali ke Menu Login")
        pilihan = input("Silakan Pilih Pilihan Yang diinginkan: ")

        if pilihan == "1":
            tambah_barang_penjual()
        elif pilihan == "2":
            hapus_stok_barang()
        elif pilihan == "3":
            lihat_stok_barang()
        elif pilihan == "4":
            perbarui_barang()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")

# Admin menambah barang (Creat)
def tambah_barang_penjual():
    lihat_stok_barang()
    nomor_barang = input("Masukan Nomor Barang: ")
    if nomor_barang in barang_database:
        print("Barang dengan nomor tersebut sudah ada.")
        return
    nama_barang = input("Masukan Nama Barang: ")
    while True:
        try:
            harga_barang = int(input("Masukan Harga Barang per hari: "))
            break
        except ValueError:
            print("Masukkan harga yang valid.")
    tambah_barang_baru(nomor_barang, nama_barang, harga_barang)
    print(f"Barang [{nama_barang}] berhasil ditambahkan.")

# Admin menghapus barang (Delete)
def hapus_stok_barang():
    lihat_stok_barang()
    nomor_barang = input("Masukan Nomor Barang yang ingin dihapus: ")
    if nomor_barang in barang_database:
        del barang_database[nomor_barang]
        print(f"Barang dengan nomor {nomor_barang} berhasil dihapus.")
    else:
        print("Barang dengan nomor tersebut tidak ditemukan.")

# Admin melihat barang (Read)
def lihat_stok_barang():
    if barang_database:
        print("\nDaftar Barang:")
        for nomor_barang, data in barang_database.items():
            print(f"Nomor: {nomor_barang}, Nama: {data['nama']}, Harga per hari: Rp.{data['harga_per_hari']:,}")
    else:
        print("Belum ada barang di dalam daftar.")

# Admin memperbarui barang (Update)
def perbarui_barang():
    lihat_stok_barang()
    nomor_barang = input("Masukan Nomor Barang yang ingin diubah: ")
    if nomor_barang in barang_database:
        pilihan = input("Pilih yang akan diubah (Nama/Harga): ").capitalize()
        if pilihan == "Nama":
            nama_baru = input("Masukkan Nama Barang Baru: ")
            barang_database[nomor_barang]['nama'] = nama_baru
            print(f"Nama barang dengan Nomor {nomor_barang} berhasil diperbarui menjadi {nama_baru}.")
        elif pilihan == "Harga":
            while True:
                try:
                    harga_baru = int(input("Masukkan Harga baru: "))
                    barang_database[nomor_barang]['harga_per_hari'] = harga_baru
                    print(f"Harga barang dengan Nomor {nomor_barang} berhasil diperbarui menjadi Rp.{harga_baru:,}.")
                    break
                except ValueError:
                    print("Masukkan harga yang valid.")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Barang dengan nomor tersebut tidak ditemukan.")

from datetime import datetime, timedelta

# Penyewa
def penyewa():
    print("\n==================================")
    print("\n      Selamat Datang Penyewa      ")
    print("\n==================================")
    nama_penyewa = input("Masukan Nama Anda: ")
    print("==============================================================================")
    print(f"      Halo Selamat datang {nama_penyewa} di Toko Deny Penyewaan Iphone       ")
    print("==============================================================================")
    
    while True:
        lihat_stok_barang()
        nomor_barang = input("Masukan Nomor Barang yang ingin disewa: ")
        
        # Memasukkan jumlah hari penyewaan
        if nomor_barang in barang_database:
            while True:
                try:
                    jumlah_hari = int(input("Masukkan Berapa Hari Anda Menyewa: "))
                    if jumlah_hari > 0:
                        break
                    else:
                        print("Jumlah hari harus lebih dari 0.")
                except ValueError:
                    print("Masukkan jumlah hari yang valid.")

            # Memasukkan tanggal mulai penyewaan
            attempts = 3
            while attempts > 0:
                try:
                    tanggal_mulai_str = input("Masukkan Tanggal Mulai Penyewaan (format: DD-MM-YYYY): ")
                    tanggal_mulai = datetime.strptime(tanggal_mulai_str, "%d-%m-%Y")
                    break
                except ValueError:
                    attempts -= 1
                    print(f"Format tanggal salah. Anda memiliki {attempts} percobaan tersisa.")
                    if attempts == 0:
                        print("Gagal memasukkan tanggal. Kembali ke menu sebelumnya.")
                        return

            # Menghitung tanggal pengembalian
            tanggal_selesai = tanggal_mulai + timedelta(days=jumlah_hari)

            # Ambil harga per hari dari barang
            harga_per_hari = barang_database[nomor_barang]['harga_per_hari']

            # Hitung total harga berdasarkan jumlah hari
            total_harga = jumlah_hari * harga_per_hari

            print(f"\nDetail Penyewaan:")
            print(f"Nama Penyewa: {nama_penyewa}")
            print(f"Nama Barang: {barang_database[nomor_barang]['nama']}")
            print(f"Jumlah Hari Sewa: {jumlah_hari} hari")
            print(f"Tanggal Mulai: {tanggal_mulai_str}")
            print(f"Tanggal Pengembalian: {tanggal_selesai.strftime('%d-%m-%Y')}")
            print(f"Total Harga: Rp.{total_harga:,}")

            confirm = input("Apakah Anda ingin melanjutkan penyewaan? (iya/tidak): ")
            if confirm.lower() != "iya":
                print("Penyewaan dibatalkan.")
                return
            else:
                print("Penyewaan berhasil disimpan!")
            return
        else:
            print("Nomor Barang tidak valid. Silakan coba lagi.")

# Memulai program dengan login
login()
