nama = "sartika"
NIM = "58"

username = input("Maukkan username: ")
password = input("Maukkan password: ")

if username == nama :
    if password == NIM:
        print("Login berhasil! Selamat datang", username)

        total_point = int(input("Masukkan total point: "))

        if total_point < 0:
            print("peringatan: total point tidak boleh kurang dari 0!")

        else:
            if total_point < 100:
                rank = "Rokie"
                sisa_point = 100 - total_point

            elif total_point < 300:
                rank = "Warrior"
                sisa_point = 300 - total_point

            elif total_point < 1000:
                rank = "Master"
                sisa_point = 1000 - total_point
            elif total_point < 5000:
                rank = "Grand Master"
                sisa_point = 5000 - total_point
            else:
                rank = "Legend"

            print("username:", username )
            print("rank:", rank)

            if rank == "Legend" :
                print("Selamat! kamu telah mencapai rank tertinggi!")
            else:   
                print("sisa point :", sisa_point)

    else:
        print("login gagal! Password salah.")

else:
    print("login gagal! Username salah.")


    
        

    

