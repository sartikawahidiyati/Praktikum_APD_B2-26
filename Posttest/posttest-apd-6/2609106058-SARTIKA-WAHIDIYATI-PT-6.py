import os
from datetime import date
 
# ===== DATA (NESTED DICTIONARY) =====
# users     : {username : {"password", "level"}}
# transaksi : {kode_transaksi : {"pemilik", "tanggal", "keterangan", "jenis", "nominal"}}
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
nomor_terakhir = 1  # untuk membuat kode transaksi otomatis (TRX002, TRX003,...)
 
while True:
    # ===== MENU UTAMA =====
    os.system("cls" if os.name == "nt" else "clear")
    print("=== PROGRAM PENGELOLAAN DATA TABUNGAN ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")
 
    # ===== REGISTER =====
    if pilihan == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== REGISTER ===")
        username_baru = input("Username baru: ").strip()
        password_baru = input("Password (min. 4 karakter): ").strip()
 
        if username_baru == "" or password_baru == "":
            print("Username atau password tidak boleh kosong!")
        elif users.get(username_baru) != None:
            print("Username sudah dipakai!")
        elif len(password_baru) < 4:
            print("Password minimal 4 karakter!")
        else:
            # menambah item secara langsung
            users[username_baru] = {
                "password" : password_baru,
                "level" : "user"
            }
            print("Register berhasil, silahkan login.")
        input("Tekan Enter untuk lanjut...")
 
    # ===== LOGIN =====
    elif pilihan == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
 
        level = ""
        data_user = users.get(username)  # .get() -> None jika key tidak ada
        if data_user != None and data_user["password"] == password:
            level = data_user["level"]
 
        if level == "":
            print("Username atau Password salah!")
            input("Tekan Enter untuk lanjut...")
            continue
 
        # ===== MENU SETELAH LOGIN =====
        login = True
        while login:
            os.system("cls" if os.name == "nt" else "clear")
 
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
                os.system("cls" if os.name == "nt" else "clear")
                print("=== TAMBAH TRANSAKSI ===")
                if level == "admin":
                    pemilik = input("Username pemilik: ").strip()
                    data_pemilik = users.get(pemilik)
                    if data_pemilik == None or data_pemilik["level"] != "user":
                        print("Pemilik tidak ditemukan!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                else:
                    pemilik = username
 
                keterangan = input("Keterangan: ").strip()
                print("Jenis transaksi: 1. Setor 2. Tarik")
                jenis_pilih = input("Pilih jenis: ").strip()
                nominal = input("Nominal (Rp): ").strip()
 
                # hitung saldo pemilik saat ini
                saldo = 0
                for t in transaksi.values():
                    if t["pemilik"] == pemilik:
                        if t["jenis"] == "Setor":
                            saldo += t["nominal"]
                        else:
                            saldo -= t["nominal"]
 
                if keterangan == "":
                    print("Keterangan tidak boleh kosong!")
                elif jenis_pilih != "1" and jenis_pilih != "2":
                    print("Jenis transaksi tidak valid!")
                elif not nominal.isdigit() or int(nominal) <= 0:
                    print("Nominal harus angka lebih dari 0!")
                elif jenis_pilih == "2" and int(nominal) > saldo:
                    print(f"Saldo tidak cukup! Saldo saat ini Rp{saldo:,}")
                else:
                    nomor_terakhir += 1
                    kode = "TRX" + str(nomor_terakhir).zfill(3)
                    jenis = "Setor" if jenis_pilih == "1" else "Tarik"
                    # menambah item menggunakan .update()
                    transaksi.update({
                        kode : {
                            "pemilik" : pemilik,
                            "tanggal" : str(date.today()),
                            "keterangan" : keterangan,
                            "jenis" : jenis,
                            "nominal" : int(nominal)
                        }
                    })
                    print(f"Transaksi {kode} berhasil ditambahkan.")
                input("Tekan Enter untuk lanjut...")
 
            # ----- READ -----
            elif menu == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== DATA TRANSAKSI ===")
                if len(tampil) == 0:
                    print("Belum ada data transaksi.")
                else:
                    total = 0
                    no = 0
                    for kode, t in transaksi.items():
                        if kode in tampil:
                            no += 1
                            print(f"{no}. Kode: {kode} | Pemilik: {t['pemilik']} | Tanggal: {t['tanggal']}")
                            print(f"   Keterangan: {t['keterangan']} | Jenis: {t['jenis']} | Nominal: Rp{t['nominal']:,}")
                            if t["jenis"] == "Setor":
                                total += t["nominal"]
                            else:
                                total -= t["nominal"]
                    print(f"\nTotal saldo: Rp{total:,}")
                input("Tekan Enter untuk lanjut...")
 
            # ----- UPDATE -----
            elif menu == "3":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== UBAH TRANSAKSI ===")
                if len(tampil) == 0:
                    print("Belum ada data transaksi.")
                else:
                    no = 0
                    for kode, t in transaksi.items():
                        if kode in tampil:
                            no += 1
                            print(f"{no}. {kode} | {t['tanggal']} | {t['keterangan']} | {t['jenis']} | Rp{t['nominal']:,}")
                    nomor = input("Nomor transaksi yang diubah: ").strip()
                    if not nomor.isdigit() or int(nomor) < 1 or int(nomor) > len(tampil):
                        print("Nomor tidak valid")
                    else:
                        kode_ubah = tampil[int(nomor) - 1]
                        print("1. Ubah keterangan")
                        print("2. Ubah jenis transaksi")
                        print("3. Ubah nominal")
                        sub = input("Pilih: ").strip()
                        lama = transaksi[kode_ubah].copy()  # salinan data lama
 
                        if sub == "1":
                            baru = input("Keterangan baru: ").strip()
                            if baru == "":
                                print("Keterangan tidak boleh kosong!")
                            else:
                                transaksi[kode_ubah].update({"keterangan" : baru})
                                print("Keterangan berhasil diubah.")
                        elif sub == "2" or sub == "3":
                            if sub == "2":
                                print("1. Setor 2. Tarik")
                                j = input("Jenis baru: ").strip()
                                valid = (j == "1" or j == "2")
                                if valid:
                                    transaksi[kode_ubah].update({"jenis" : "Setor" if j == "1" else "Tarik"})
                            else:
                                n = input("Nominal baru (Rp): ").strip()
                                valid = n.isdigit() and int(n) > 0
                                if valid:
                                    transaksi[kode_ubah].update({"nominal" : int(n)})
 
                            if not valid:
                                print("Input tidak valid")
                            else:
                                # cek saldo pemilik tidak boleh minus
                                saldo = 0
                                for t in transaksi.values():
                                    if t["pemilik"] == lama["pemilik"]:
                                        if t["jenis"] == "Setor":
                                            saldo += t["nominal"]
                                        else:
                                            saldo -= t["nominal"]
 
                                if saldo < 0:
                                    transaksi[kode_ubah] = lama
                                    print("Perubahan dibatalkan, saldo akan menjadi minus!")
                                else:
                                    print("Data berhasil diubah.")
                        else:
                            print("Pilihan tidak valid!")
                input("Tekan Enter untuk lanjut...")
 
            # ----- DELETE -----
            elif menu == "4":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== HAPUS TRANSAKSI ===")
                if len(tampil) == 0:
                    print("Belum ada data transaksi.")
                else:
                    no = 0
                    for kode, t in transaksi.items():
                        if kode in tampil:
                            no += 1
                            print(f"{no}. {kode} | {t['tanggal']} | {t['keterangan']} | {t['jenis']} | Rp{t['nominal']:,}")
                    nomor = input("Nomor transaksi yang dihapus: ").strip()
                    if not nomor.isdigit() or int(nomor) < 1 or int(nomor) > len(tampil):
                        print("Nomor tidak valid!")
                    else:
                        yakin = input("Yakin hapus? (y/n): ").lower()
                        if yakin == "y":
                            kode_hapus = tampil[int(nomor) - 1]
                            pemilik_hapus = transaksi[kode_hapus]["pemilik"]
                            # cek saldo pemilik jika transaksi ini dihapus
                            saldo = 0
                            for kode, t in transaksi.items():
                                if kode != kode_hapus and t["pemilik"] == pemilik_hapus:
                                    if t["jenis"] == "Setor":
                                        saldo += t["nominal"]
                                    else:
                                        saldo -= t["nominal"]
                            if saldo < 0:
                                print("Penghapusan dibatalkan, saldo akan menjadi minus!")
                            else:
                                cache = transaksi.pop(kode_hapus)
                                print(f"Data {kode_hapus} ({cache['keterangan']}) berhasil dihapus.")
                        else:
                            print("Penghapusan dibatalkan.")
                input("Tekan Enter untuk lanjut...")
 
            # ----- LOGOUT -----
            elif menu == "5":
                login = False
 
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