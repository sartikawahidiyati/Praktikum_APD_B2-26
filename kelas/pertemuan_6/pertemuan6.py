kartu = {"merah", "merah", "biru", "hijau"}

print(kartu)

# set menggunakan list
matkul = ["apd", "orsikom", "apd", "kalkulus"]
sks = set(matkul)
print(sks)

#set menggunakan tuple
buah = set(("apel", "jeruk", "mangga", "apel"))
print(buah)

angka_ganjil = {1, 3, 5, 7, 9}

for angka in angka_ganjil:
    print (angka)

buah = {"apel", "mangga", "jeruk"}
buah.remove("mangga")
print(buah)

aslab1 = {"fina", "shasha", "risma"}
aslab2 = {"larry", "attar", "haekal"}
aslab3 ={"rafi", "rendi", "yoga"}

gabung = aslab1.union(aslab2)
print(gabung)
gabungan_lengkap = gabung.union(aslab3)

setHasiluUpdate = aslab1.update(aslab2)

print(f"nilai aslab1 : {aslab1}")
irisan_aslab1_aslab2 = aslab1.intersection(aslab2)
print(irisan_aslab1_aslab2)

print(f"nilai aslab1 : {aslab1}")
irisan_aslab1_aslab2 = aslab1.difference(aslab2)
print(irisan_aslab1_aslab2)

Matkul = {
    "Matkul_ganjil" : "kalkulus",
"Matkul_genap" : "statistik"
}
print(Matkul["Matkul_ganjil"])
print(Matkul)

print(Matkul.get("Matkul_genap", "key tidak ada"))
game = {
"pou" : "chill",
"genshin impact" : "action",
"valorant" : "fps",
"minecraft" : "sandbox",
"mobile legend" : "moba"
}

print(len(game))

game_copy = game.copy

del game_copy["valorant"]
del game_copy["Mobile legend"]

print(game)
print(game_copy)




for i in game.values():
    print(i)

for i in game.keys():
    print(i)

for key, value in game.items():
    print(key, value)

game["valorant"] = "Action"
print(game)

game.update({"minecraft" : "horror"})

item = game.setdefault("pou", "Battle Royale")
print(item)

for key,value in game.items():
    print(key,value)
 
del game["valorant"]

print(game)

item_dihapus = game.pop("minecraft")

print(game)
print(item_dihapus)

game.clear()
print(game)

key = "ayam geprek", "ayam goreng", "ayam bakar",
value = 12000
menu = dict.fromkeys(key, value)

print(menu)

menu = {
    "ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
    "nasi" : ["nasi goreng", "nasi uduk"],
    "mie" : ["mie goreng rendang", "mie goreng aceh"],
    "kuah" : ["soto", "rawon", "sop iga"]
}

print(menu.get("ayam")[2])

mahasiswa = {
    "054": 
}