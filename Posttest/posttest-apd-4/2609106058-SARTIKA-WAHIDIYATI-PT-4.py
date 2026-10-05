Username_benar = "Sartika"
Password_benar = "2609106058"

Maks_percobaan = 3

print("Los Pollos Hrmanos - Program Sosial")
print("Distribusi Makanan Bergizi Gratis")

percobaan = 0
login_berhasil = False

while percobaan < Maks_percobaan:
    username = input("username : "). strip()
    while username == "":
        print("Username tidak boleh kosong!")
        username = input("Username : ").strip()

    password =input("Password: ").strip()
    while password == "":
        print("Password tidak boleh kosong!")
        password = input("Password :").strip()

    percobaan += 1
    username_cocok = username.lower()==Username_benar.lower()
    password_cocok = password == Password_benar

    if username_cocok and password_cocok:
        login_berhasil = True
        break
    elif not username_cocok and not password_cocok:
        print("Login gagal: username dan password salah!")
    elif not username_cocok:
        print("Login gagal: username salah!")
    else:
        print("Login gagal: password salah!")

    sisa = Maks_percobaan - percobaan
    if sisa > 0:
        print(f"Sisa percobaan: {sisa}")

if not login_berhasil:
    print("Login gagal 3 kali. Program dihentikan.")
else:
    print(f"Login berhasil! Selamat datang, {Username_benar.title()}.")

    while True:
        print(" 1. Paket Reguler (1 porsi)")
        print(" 2. Paket Anak (1 porsi)")
        print(" 3. Paket Keluarga (4 porsi)")
        print(" 4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "":
            print("Input tidak boleh kosong!")
            continue
        if not pilihan.isdigit():
            continue
        pilihan = int(pilihan)

        if pilihan < 1 or pilihan > 4:
            print("opsi tidak valid")
            continue
 
        if pilihan == 4:
            print("Terima kasih telah berbagi kebaikan. Sampai jumpa!")
            break

        if pilihan == 1:
            jenis_paket = "Paket Reguler"
            porsi_per_paket = 1
        elif pilihan == 2:
            jenis_paket = "Paket Anak"
            porsi_per_paket = 1
        else:
            jenis_paket = "Paket Keluarga"
            porsi_per_paket = 4


        while True:
            jumlah_input = input("Jumlah paket yang dibagikan: ").strip()
            if jumlah_input == "":
                  print("input tidak boleh kosong!")
            elif not jumlah_input.isdigit():
                  print("Input harus berupa angka!")
            elif int(jumlah_input) == 0:
                  print("Jumlah paket harus lebih dari 0!")
            else:
                jumlah_paket = int(jumlah_input)
            break

    
        total_porsi = 0
        for i in range(jumlah_paket):
            total_porsi += porsi_per_paket

     
        if total_porsi >= 20:
            bonus = "5 paket buah"
        elif total_porsi >= 10:
            bonus = "3 botol susu"
        elif total_porsi >= 5:
            bonus = "1 paket vitamin"
        else:
            bonus = "Tidak ada bonus"
 
        penerima_manfaat = total_porsi  
 
        
        print("              HASIL DISTRIBUSI")
        
        print(f"  Jenis paket        : {jenis_paket}")
        print(f"  Jumlah paket       : {jumlah_paket}")
        print(f"  Total porsi        : {total_porsi} porsi")
        print(f"  Penerima manfaat   : {penerima_manfaat} orang")
        print(f"  Bonus              : {bonus}")
        print("  Makanan dibagikan GRATIS, tanpa pembayaran, SEMOGA BERMANFAAT.")
        
        
        





                
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  



