
# program CRUD "Manajemen Listing Properti"
# Nama : Rendy
# NIM : 2509106069

import os
import time
from prettytable import PrettyTable
import pwinput

# {username, password, level_akses}
data_pengguna = {
    "rendy": {"password": "admin123", "level": "admin"},
    "user1": {"password": "user123", "level": "user"}
}

# {id, nama, lokasi, tipe listing, harga}
daftar_properti = {
    "R001": {
        "nama": "Krusty Krab", 
        "lokasi": "Bikini Bottom", 
        "tipe": "Restoran", 
        "harga": 5000000
    },
    "R002": {
        "nama": "Rumah Upin & Ipin", 
        "lokasi": "Kampung Durian Runtuh",
        "tipe": "Rumah", 
        "harga": 350000
    },
    "R003": {
        "nama": "Superlab Gustavo Fring", 
        "lokasi": "Albuquerque, New Mexico", 
        "tipe": "Laboratorium", 
        "harga": 12000000
    }
}

while True:
    os.system("cls || clear")
    print("🏠  SISTEM MANAJEMEN LISTING PROPERTI  🏠.")
    tabel_menu = PrettyTable()
    tabel_menu.field_names = ["No", "🧭 Menu Utama"]
    tabel_menu.align = "l" 
    tabel_menu.hrules = 1
    tabel_menu.add_row(["1", "🔑 Login"])
    tabel_menu.add_row(["2", "📝 Register"])
    tabel_menu.add_row(["3", "🚪 Keluar"])
    print(tabel_menu)

    opsi = input("Pilih Menu : ")

    # Kesempatan Login 3x
    if opsi == "1":
        os.system("cls || clear")
        print("=== LOGIN ===")
        percobaan = 0
        berhasil = False

        while percobaan < 3 and not berhasil:
            username = input("Masukkan Username: ").lower()
            password = pwinput.pwinput(prompt="Masukkan Password: ",mask="*")

            level_akses = None
            if username in data_pengguna and password == data_pengguna[username]["password"]:
                level_akses = data_pengguna[username]["level"]

            if level_akses:  # login berhasil
                berhasil = True
            else:
                percobaan += 1
                sisa = 3 - percobaan
                if sisa > 0:
                    print(f"Username atau password salah! Sisa percobaan: {sisa}")
                else:
                    print("Username atau password salah 3 kali. Silakan tunggu 5 menit sebelum mencoba lagi.")
                    time.sleep(300)

        if berhasil:
            #ADMIN
            if level_akses == "admin":
                while True:
                    os.system("cls || clear")

                    print("=" * 60)
                    print("  MENU ADMIN ".center(60))
                    print("=" * 60)

                    tabel_admin = PrettyTable()
                    tabel_admin.field_names = ["No", "Pilihan Menu"]
                    tabel_admin.align = "l"
                    tabel_admin.hrules = 1
                    tabel_admin.add_row(["1", "Lihat Semua Properti"])
                    tabel_admin.add_row(["2", "Tambah Properti"])
                    tabel_admin.add_row(["3", "Update Properti"])
                    tabel_admin.add_row(["4", "Hapus Properti"])
                    tabel_admin.add_row(["5", "Logout"])
                    
                    print(tabel_admin)

                    opsi_admin = input("Pilih menu: ")

                    # Read
                    if opsi_admin == "1":
                        os.system("cls || clear")
                        print("=== Daftar Properti ===")
                        if len(daftar_properti) == 0:
                            print("Belum ada Properti")
                        else:
                            tabel = PrettyTable()
                            tabel.field_names = ["No", "ID", "Nama", "Lokasi", "Tipe Listing", "Harga (Rp)"]
                            tabel.hrules = 1
                            for i, (id, data) in enumerate(daftar_properti.items(), start=1):
                                tabel.add_row([i, id, data["nama"], data["lokasi"], data["tipe"], f"{data['harga']:,}"])
                            print(tabel)
                        input("\nTekan Enter untuk kembali...")

                    # Create
                    elif opsi_admin == "2":
                        os.system("cls || clear")
                        print("=== TAMBAH PROPERTI ===")

                        # mencegah bug duplikasi id
                        id_baru = "R001"
                        for key in daftar_properti:
                            id_baru = "R" + str(int(key[1:]) + 1).zfill(3)
                        
                        nama = input("Nama Properti: ")
                        lokasi = input("Lokasi: ")
                        tipe_listing = input("Tipe listing: ")
                        harga = input("Harga (angka): ")

                        if harga.isdigit():
                            daftar_properti[id_baru] = {
                                "nama": nama,
                                "lokasi": lokasi,
                                "tipe": tipe_listing,
                                "harga": int(harga)
                            }
                            print("Properti berhasil ditambahkan!")
                        else:
                            print("Harga harus berupa angka!")
                        input("Tekan Enter untuk kembali...")

                    # Update
                    elif opsi_admin == "3":
                        os.system("cls || clear")
                        print("=== UPDATE DATA PROPERTI ===")
                        tabel_update = PrettyTable()
                        tabel_update.field_names = ["No", "ID", "Nama Properti", "Lokasi", "Tipe Listing", "Harga (Rp)"]
                        tabel_update.align = "l"
                        tabel_update.hrules = 1

                        for i, (id, data) in enumerate(daftar_properti.items(), start=1):
                            tabel_update.add_row([i, id, data["nama"], data["lokasi"], data["tipe"], f"{data['harga']:,}"])
                        print(tabel_update)

                        pilih = input("Nomor properti yang ingin diupdate: ")

                        if pilih.isdigit() and 1 <= int(pilih) <= len(daftar_properti):
                            key = list(daftar_properti.keys())[int(pilih) - 1]
                            properti_dipilih = daftar_properti[key]
                            print("Kosongkan jika tidak ingin mengubah.")
                            
                            nama_lama = properti_dipilih["nama"]
                            lokasi_lama = properti_dipilih["lokasi"]
                            tipe_listing_lama = properti_dipilih["tipe"]
                            harga_lama = properti_dipilih["harga"]

                            nama_baru = input(f"Nama baru ({nama_lama}): ")
                            lokasi_baru = input(f"Lokasi baru ({lokasi_lama}): ")
                            tipe_listing_baru = input(f"Tipe listing baru ({tipe_listing_lama}): ")
                            harga_baru = input(f"Harga baru ({harga_lama}): ")

                            if nama_baru:
                                properti_dipilih["nama"] = nama_baru
                            if lokasi_baru:
                                properti_dipilih["lokasi"] = lokasi_baru
                            if tipe_listing_baru:
                                properti_dipilih["tipe"] = tipe_listing_baru
                            if harga_baru != "":
                                if harga_baru.isdigit():
                                    properti_dipilih["harga"] = int(harga_baru)
                                else:
                                    print("Harga harus angka, tidak diubah.")
                            print("Data berhasil diperbarui.")
                        else:
                            print("Nomor tidak valid!")
                        input("Tekan Enter untuk kembali...")

                    # Delete
                    elif opsi_admin == "4":
                        os.system("cls || clear")
                        print("=== HAPUS PROPERTI ===")
                        tabel_hapus = PrettyTable()
                        tabel_hapus.field_names = ["No", "ID", "Nama Properti", "Lokasi", "Tipe Listing", "Harga (Rp)"]
                        tabel_hapus.align = "l"
                        tabel_hapus.hrules = 1

                        for i, (id, data) in enumerate(daftar_properti.items(), start=1):
                            tabel_hapus.add_row([i, id, data["nama"], data["lokasi"], data["tipe"], f"{data['harga']:,}"])
                        print(tabel_hapus)

                        pilih = input("Nomor properti yang ingin dihapus: ")

                        if pilih.isdigit() and 1 <= int(pilih) <= len(daftar_properti):
                            key = list(daftar_properti.keys())[int(pilih) - 1]
                            del daftar_properti[key]
                            print("Data berhasil dihapus.")
                        else:
                            print("Nomor tidak valid!")
                        input("Tekan Enter untuk kembali...")

                    # Logout
                    elif opsi_admin == "5":
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter untuk lanjut...")

            # USER
            elif level_akses == "user":
                while True:
                    os.system("cls || clear")
                    print("=== MENU USER ===")

                    tabel_user = PrettyTable()
                    tabel_user.field_names = ["No", "Pilihan Menu"]
                    tabel_user.align = "l"
                    tabel_user.hrules = 1

                    tabel_user.add_row(["1", "Lihat Semua Properti"])
                    tabel_user.add_row(["2", "Logout"])
                    print(tabel_user)

                    pilih_user = input("Pilih menu: ")

                    if pilih_user == "1":
                        os.system("cls || clear")
                        print("=== DAFTAR PROPERTI ===")
                        if len(daftar_properti) == 0:
                            print("Belum ada properti.")
                        else:
                            tabel_user_properti = PrettyTable()
                            tabel_user_properti.field_names = ["No", "ID", "Nama Properti", "Lokasi", "Tipe Listing", "Harga (Rp)"]
                            tabel_user_properti.align = "l"
                            tabel_user_properti.hrules = 1

                            for i, (id, data) in enumerate(daftar_properti.items(), start=1):
                                tabel_user_properti.add_row([i, id, data["nama"], data["lokasi"], data["tipe"], f"{data['harga']:,}"])
                            print(tabel_user_properti)
                        input("\nTekan Enter untuk kembali...")

                    elif pilih_user == "2":  
                        break

    # Register
    elif opsi == "2":
        os.system("cls || clear")
        print("=== REGISTER PENGGUNA BARU ===")
        username = input("Masukkan username: ").lower()
        password = pwinput.pwinput(prompt="Masukkan Password: ",mask="*")

        if username in data_pengguna:
            print("Username sudah digunakan!")
        else:
            data_pengguna[username] = {"password": password, "level": "user"}
            print("Registrasi berhasil! Silakan login.")


    # keluar program
    elif opsi == "3":
        print("Terima kasih telah menggunakan Program ini!")
        break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut...")