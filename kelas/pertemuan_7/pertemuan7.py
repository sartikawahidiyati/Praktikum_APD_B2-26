def sapa():
    print("Halooo Rendy")
    return "Halooo Rendy"

teks_sapaan = sapa()
print (teks_sapaan)

def hitung():
    5 * 3

print(hitung())

def persegi(sisi):
    hasil = sisi*sisi
    return 

def sapa(nama="kansa"):
    return f"Halooo {nama}"

print(sapa("sartika"))

def menu():
    print("1. create")
    print("2. read")
    print("3. update")
    print("4. delete")

    pilihan = input("pilih menu: ")

#variabel global
nama = "larry"
prodi = "informatika"

def data1():
    #variabel lokal
    nama = "Alfi"
    prodi = "Kedokteran Lanjut"
    
    print("Nama:", nama)
    print("Prodi:", prodi)

def data2():
    #variabel lokal
    nama = "Alfi"
    prodi = "Kedokteran Lanjut"
    
    print("Nama:", nama)
    print("Prodi:", prodi)

data2()


def sapa():
    print("Halooo Rendy")
    sapa()

sapa()


def faktorial(n):
#Base Case: Kondisi fungsi berhenti
    if n == 0 or n ==  1:
        return 1
#Rekursive Case: Fungsi memanggil dirinya sendiri
    else:
        return n * faktorial(n - 1)

#Memanggil fungsi
hasil_faktorial = faktorial(4)
print(f"Hasil dari 4! {hasil_faktorial}")
#Output
Hasil dari faktorial 4! adalah 24






