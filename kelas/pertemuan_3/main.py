 cuaca = "hujan"

if cuaca == "hujan":
    print("bawa payung/jas hujan")
    print("telat dikit")

print("otw ke kampus")   


budget = 2000
cuaca = "hujan"

if budget > 30000 and cuaca == "cerah":
    print("beli yoshinoya")
else:
    print("masak indomie")

kendaraan = input("masukkan jenis kendaraan: ").lower().strip()

if kendaraan == "mobil":
    tarif_parkir = 10_000 
elif kendaraan == "motor":
    tarif_parkir = 5_000
else:
    tarif_parkir = 15_000

print("tarif parkir yang harus dibayar: ", tarif_parkir)



bilangan = -5

status = "bilangan negatif" if bilangan < 0 else "bilangan positif"

print("bilangan adalah", status)

username = input("masuk username: ").lower().strip()
password = input("Masukkan password: ").lower.strip()

if username == "sartika":
    if password == "058":
        print("login berhasil")
    else:
        print("password salah")
else:
    print("username salah")

angka = 10 / 6
print(f"angka{angka:.02f}")







