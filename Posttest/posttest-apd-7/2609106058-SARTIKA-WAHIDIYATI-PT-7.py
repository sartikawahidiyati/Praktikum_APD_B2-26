import os
from datetime import date

# ===== VARIABEL GLOBAL (4 buah) =====
# users          : {username : {"password", "level"}}
# transaksi      : {kode_transaksi : {"pemilik", "tanggal", "keterangan", "jenis", "nominal"}}
# nomor_terakhir : untuk membuat kode transaksi otomatis (TRX002, TRX003,...)
# MIN_PASSWORD   : panjang minimal password
users = {
    "admin" : {
        "password" : "admin123",
        "level" : "admin"
    },
    "sartika" : {
        "password" : "1234",
        "level" : "user"
    }
}
transaksi = {
    "TRX001" : {
        "pemilik" : "sartika",
        "tanggal" : "2026-10-14",
        "keterangan" : "Setoran awal",
        "jenis" : "Setor",
        "nominal" : 1250000
    }
}
nomor_terakhir = 1
MIN_PASSWORD = 4


# ===== PROSEDUR (2 buah, tanpa return) =====

# Prosedur 1 : tanpa parameter
def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


# Prosedur 2 : dengan parameter
def tampilkan_daftar(daftar_kode):
    nomor = 0
    for kode in daftar_kode:
        t = transaksi[kode]
        nomor += 1
        print(f"{nomor}. Kode: {kode} | Pemilik: {t['pemilik']} | Tanggal: {t['tanggal']}")
        print(f"   Keterangan: {t['keterangan']} | Jenis: {t['jenis']} | Nominal: Rp{t['nominal']:,}")


# ===== FUNGSI TANPA PARAMETER (2 buah) =====

# Fungsi 1 : membuat kode transaksi otomatis
def buat_kode_transaksi():
    global nomor_terakhir
    nomor_terakhir += 1
    kode_baru = "TRX" + str(nomor_terakhir).zfill(3)
    return kode_baru


# Fungsi 2 : login, mengembalikan (username, level) atau None jika gagal
def login():
    bersihkan_layar()
    print("=== LOGIN ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    try:
        data_user = users[username]                 # KeyError jika username tidak ada
        if data_user["password"] != password:
            raise ValueError("password salah")      # error manual
    except (KeyError, ValueError):
        print("Username atau Password salah!")
        input("Tekan Enter untuk lanjut...")
        return None
    else:
        return (username, data_user["level"])


# ===== FUNGSI DENGAN PARAMETER (2 buah) =====

# Fungsi 3 : menghitung saldo seorang pemilik
def hitung_saldo(pemilik, kecuali_kode=None):
    saldo = 0
    for kode, t in transaksi.items():
        if kode != kecuali_kode and t["pemilik"] == pemilik:
            if t["jenis"] == "Setor":
                saldo += t["nominal"]
            else:
                saldo -= t["nominal"]
    return saldo


# Fungsi 4 (REKURSIF) : menghitung total saldo dari daftar kode transaksi
def hitung_total_rekursif(daftar_kode, indeks=0):
    # Base case : semua transaksi sudah dihitung
    if indeks >= len(daftar_kode):
        return 0
    # Recursive case : nilai transaksi ini + total transaksi berikutnya
    t = transaksi[daftar_kode[indeks]]
    nilai = t["nominal"] if t["jenis"] == "Setor" else -t["nominal"]
    return nilai + hitung_total_rekursif(daftar_kode, indeks + 1)


# ===== PROGRAM UTAMA =====
while True:
    # ===== MENU UTAMA =====
    bersihkan_layar()
    print("=== PROGRAM PENGELOLAAN DATA TABUNGAN ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    # ===== REGISTER =====
    if pilihan == "2":
        bersihkan_layar()
        print("=== REGISTER ===")
        username_baru = input("Username baru: ").strip()
        password_baru = input(f"Password (min. {MIN_PASSWORD} karakter): ").strip()
        try:
            if username_baru == "" or password_baru == "":
                raise ValueError("Username atau password tidak boleh kosong!")
            if username_baru in users:
                raise ValueError("Username sudah dipakai!")
            if len(password_baru) < MIN_PASSWORD:
                raise ValueError(f"Password minimal {MIN_PASSWORD} karakter!")
        except ValueError as e:
            print(f"Register gagal: {e}")
        else:
            users[username_baru] = {
                "password" : password_baru,
                "level" : "user"
            }
            print("Register berhasil, silahkan login.")
        finally:
            input("Tekan Enter untuk lanjut...")

    # ===== LOGIN =====
    elif pilihan == "1":
        hasil_login = login()
        if hasil_login == None:
            continue
        username, level = hasil_login

        # ===== MENU SETELAH LOGIN =====
        sedang_login = True
        while sedang_login:
            bersihkan_layar()

            # kode transaksi yang boleh dilihat
            # admin = semua, user biasa = miliknya saja
            tampil = []
            for kode in transaksi.keys():
                if level == "admin" or transaksi[kode]["pemilik"] == username:
                    tampil.append(kode)

            print(f"=== MENU {level.upper()} | Login: {username} ===")
            print("1. Tambah Transaksi  (Create)")
            print("2. Lihat Transaksi  (Read)")
            print("3. Ubah Transaksi  (Update)")
            print("4. Hapus Transaksi  (Delete)")
            print("5. Logout")
            menu = input("Pilih menu: ")

            # ----- CREATE -----
            if menu == "1":
                bersihkan_layar()
                print("=== TAMBAH TRANSAKSI ===")
                if level == "admin":
                    pemilik = input("Username pemilik: ").strip()
                    try:
                        if users[pemilik]["level"] != "user":
                            raise ValueError("Pemilik harus user biasa!")
                    except KeyError:
                        print("Pemilik tidak ditemukan!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    except ValueError as e:
                        print(e)
                        input("Tekan Enter untuk lanjut...")
                        continue
                else:
                    pemilik = username

                keterangan = input("Keterangan: ").strip()
                print("Jenis transaksi: 1. Setor 2. Tarik")
                jenis_pilih = input("Pilih jenis: ").strip()
                nominal_teks = input("Nominal (Rp): ").strip()

                try:
                    if keterangan == "":
                        raise ValueError("Keterangan tidak boleh kosong!")
                    if jenis_pilih != "1" and jenis_pilih != "2":
                        raise ValueError("Jenis transaksi tidak valid!")
                    if not nominal_teks.isdigit() or int(nominal_teks) <= 0:
                        raise ValueError("Nominal harus angka lebih dari 0!")
                    nominal = int(nominal_teks)
                    saldo = hitung_saldo(pemilik)
                    if jenis_pilih == "2" and nominal > saldo:
                        raise ValueError(f"Saldo tidak cukup! Saldo saat ini Rp{saldo:,}")
                except ValueError as e:
                    print(f"Gagal: {e}")
                else:
                    kode = buat_kode_transaksi()
                    jenis = "Setor" if jenis_pilih == "1" else "Tarik"
                    transaksi.update({
                        kode : {
                            "pemilik" : pemilik,
                            "tanggal" : str(date.today()),
                            "keterangan" : keterangan,
                            "jenis" : jenis,
                            "nominal" : nominal
                        }
                    })
                    print(f"Transaksi {kode} berhasil ditambahkan.")
                finally:
                    input("Tekan Enter untuk lanjut...")

            # ----- READ -----
            elif menu == "2":
                bersihkan_layar()
                print("=== DATA TRANSAKSI ===")
                if len(tampil) == 0:
                    print("Belum ada data transaksi.")
                else:
                    tampilkan_daftar(tampil)
                    total = hitung_total_rekursif(tampil)
                    print(f"\nTotal saldo: Rp{total:,}")
                input("Tekan Enter untuk lanjut...")

            # ----- UPDATE -----
            elif menu == "3":
                bersihkan_layar()
                print("=== UBAH TRANSAKSI ===")
                if len(tampil) == 0:
                    print("Belum ada data transaksi.")
                else:
                    tampilkan_daftar(tampil)
                    try:
                        nomor = int(input("Nomor transaksi yang diubah: "))
                        if nomor < 1:
                            raise ValueError
                        kode_ubah = tampil[nomor - 1]       # IndexError jika di luar daftar
                    except (ValueError, IndexError):
                        print("Nomor tidak valid!")
                    else:
                        print("1. Ubah keterangan")
                        print("2. Ubah jenis transaksi")
                        print("3. Ubah nominal")
                        sub = input("Pilih: ").strip()
                        lama = transaksi[kode_ubah].copy()  # salinan data lama
                        try:
                            if sub == "1":
                                baru = input("Keterangan baru: ").strip()
                                if baru == "":
                                    raise ValueError("Keterangan tidak boleh kosong!")
                                transaksi[kode_ubah].update({"keterangan" : baru})
                            elif sub == "2":
                                print("1. Setor 2. Tarik")
                                j = input("Jenis baru: ").strip()
                                if j != "1" and j != "2":
                                    raise ValueError("Jenis transaksi tidak valid!")
                                transaksi[kode_ubah].update({"jenis" : "Setor" if j == "1" else "Tarik"})
                            elif sub == "3":
                                n = input("Nominal baru (Rp): ").strip()
                                if not n.isdigit() or int(n) <= 0:
                                    raise ValueError("Nominal harus angka lebih dari 0!")
                                transaksi[kode_ubah].update({"nominal" : int(n)})
                            else:
                                raise ValueError("Pilihan tidak valid!")

                            # saldo pemilik tidak boleh minus
                            if hitung_saldo(lama["pemilik"]) < 0:
                                raise ValueError("Perubahan dibatalkan, saldo akan menjadi minus!")
                        except ValueError as e:
                            transaksi[kode_ubah] = lama     # kembalikan data lama
                            print(f"Gagal: {e}")
                        else:
                            print("Data berhasil diubah.")
                input("Tekan Enter untuk lanjut...")

            # ----- DELETE -----
            elif menu == "4":
                bersihkan_layar()
                print("=== HAPUS TRANSAKSI ===")
                if len(tampil) == 0:
                    print("Belum ada data transaksi.")
                else:
                    tampilkan_daftar(tampil)
                    try:
                        nomor = int(input("Nomor transaksi yang dihapus: "))
                        if nomor < 1:
                            raise ValueError
                        kode_hapus = tampil[nomor - 1]
                    except (ValueError, IndexError):
                        print("Nomor tidak valid!")
                    else:
                        yakin = input("Yakin hapus? (y/n): ").strip().lower()
                        if yakin == "y":
                            pemilik_hapus = transaksi[kode_hapus]["pemilik"]
                            # cek saldo pemilik jika transaksi ini dihapus
                            if hitung_saldo(pemilik_hapus, kode_hapus) < 0:
                                print("Penghapusan dibatalkan, saldo akan menjadi minus!")
                            else:
                                cache = transaksi.pop(kode_hapus)
                                print(f"Data {kode_hapus} ({cache['keterangan']}) berhasil dihapus.")
                        else:
                            print("Penghapusan dibatalkan.")
                input("Tekan Enter untuk lanjut...")

            # ----- LOGOUT -----
            elif menu == "5":
                sedang_login = False

            else:
                print("Menu tidak valid!")
                input("Tekan Enter untuk lanjut...")

    # ===== KELUAR =====
    elif pilihan == "3":
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut...")
