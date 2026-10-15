import os
from datetime import date

# ===== DATA (NESTED LIST) =====
# users     : [username, password, level]
# transaksi : [kode_transaksi, pemilik, tanggal, keterangan, jenis_transaksi, nominal]
users = [
    ["admin", "admin123", "admin"],
    ["sartika", "1234", "user"],
]
transaksi = [
    ["TRX001", "sartika", "2026-10-14", "Setoran awal", "Setor", 1250000],
]
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

        ada = False
        for u in users:
            if u[0] == username_baru:
                ada = True
        if username_baru == "" or password_baru == "":
            print("Username atau password tidak boleh kosong!")
        elif ada:
            print("Username sudah dipakai!")
        elif len(password_baru) < 4:
            print("Password minimal 4 karakter!")
        else:
            users.append([username_baru, password_baru, "user"])
            print("Register berhasil, silahkan login.")
        input("Tekan Enter untuk lanjut...")

    # ===== LOGIN =====
    elif pilihan == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        level = ""
        for u in users:
            if u[0] == username and u[1] == password:
                level = u[2]

        if level == "":
            print("Username atau Password salah!")
            input("Tekan Enter untuk lanjut...")
            continue

        # ===== MENU SETELAH LOGIN =====
        login = True
        while login:
            os.system("cls" if os.name == "nt" else "clear")

            # index transaksi yang boleh dilihat
            # admin = semua, user biasa = miliknya saja
            tampil = []
            for i in range(len(transaksi)):
                if level == "admin" or transaksi[i][1] == username:
                    tampil.append(i)

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
                    terdaftar = False
                    for u in users:
                        if u[0] == pemilik and u[2] == "user":
                            terdaftar = True
                    if not terdaftar:
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
                for t in transaksi:""
                if t[1] == pemilik:
                        if t[4] == "Setor":
                            saldo += t[5]
                        else:
                            saldo -= t[5]

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
                    transaksi.append([kode, pemilik, str(date.today()), keterangan, jenis, int(nominal)])
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
                    for no in range(len(tampil)):
                        t = transaksi[tampil[no]]
                        print(f"{no + 1}. Kode: {t[0]} | Pemilik: {t[1]} | Tanggal: {t[2]}")
                        print(f"   Keterangan: {t[3]} | Jenis: {t[4]} | Nominal: Rp{t[5]:,}")
                        if t[4] == "Setor":
                            total += t[5]
                        else:
                            total -= t[5]
                    print(f"\nTotal saldo: Rp{total:,}")
                input("Tekan Enter untuk lanjut...")

            # ----- UPDATE -----
            elif menu == "3":
                os.system("cls" if os.name == "nt" else "clear")
                print("=== UBAH TRANSAKSI ===")
                if len(tampil) == 0:
                    print("Belum ada data transaksi.")
                else:
                    for no in range(len(tampil)):
                        t = transaksi[tampil[no]]
                        print(f"{no + 1}. {t[0]} | {t[2]} | {t[3]} | {t[4]} | Rp{t[5]:,}")
                    nomor = input("Nomor transaksi yang diubah: ").strip()
                    if not nomor.isdigit() or int(nomor) < 1 or int(nomor) > len(tampil):
                        print("Nomor tidak valid")
                    else:
                        idx = tampil[int(nomor) - 1]
                        print("1. Ubah keterangan")
                        print("2. Ubah jenis transaksi")
                        print("3. Ubah nominal")
                        sub = input("Pilih: ").strip()
                        lama = transaksi[idx][:]  # salinan data lama

                        if sub == "1":
                            baru = input("Keterangan baru: ").strip()
                            if baru == "":
                                print("Keterangan tidak boleh kosong!")
                            else:
                                transaksi[idx][3] = baru
                                print("Keterangan berhasil diubah.")
                        elif sub == "2" or sub == "3":
                            if sub == "2":
                                print("1. Setor 2. Tarik")
                                j = input("Jenis baru: ").strip()
                                valid = (j == "1" or j == "2")
                                if valid:
                                    transaksi[idx][4] = "Setor" if j == "1" else "Tarik"
                            else:
                                n = input("Nominal baru (Rp): ").strip()
                                valid = n.isdigit() and int(n) > 0
                                if valid: 
                                    transaksi[idx][5] = int(n)

                            if not valid:
                                print("Input tidak valid")
                            else:
                                # cek saldo pemilik tidak boleh minus
                                saldo = 0
                                for t in transaksi:
                                    if t[1] == lama[1]:
                                        if t[4] == "Setor":
                                            saldo += t[5]
                                        else:
                                            saldo -= t[5]

                                if saldo < 0:
                                    transaksi[idx] = lama
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
                    for no in range(len(tampil)):
                        t = transaksi[tampil[no]]
                        print(f"{no + 1}. {t[0]} | {t[2]} | {t[3]} | {t[4]} | Rp{t[5]:,}")
                    nomor = input("Nomor transaksi yang dihapus: ").strip()
                    if not nomor.isdigit() or int(nomor) < 1 or int(nomor) > len(tampil):
                        print("Nomor tidak valid!")
                    else:
                        yakin = input("Yakin hapus? (y/n): ").lower()
                        if yakin == "y":
                            idx = tampil[int(nomor) - 1]
                            data = transaksi.pop(idx)
                            # cek saldo pemilik setelah dihapus
                            saldo = 0
                            for t in transaksi:
                                if t[1] == data[1]:
                                    if t[4] == "Setor":
                                        saldo += t[5]
                                    else:
                                        saldo -= t[5]
                            if saldo < 0:
                                transaksi.insert(idx, data)
                                print("Penghapusan dibatalkan, saldo akan menjadi minus!")
                            else:
                                print("Data berhasil dihapus.")
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






                
                







