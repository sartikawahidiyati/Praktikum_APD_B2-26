formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
print(formula1)

print(formula1[0])

for index, elemen in enumerate (formula1, start=1):
    print(index, elemen)

sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
print(sirkuit)

sirkuit.append("daniel")
print(sirkuit)

sirkuit.append("nando")
print("nando")

sirkuit.extend(["larry", "rendy"])
print(sirkuit)

sirkuit.insert(2, "alfi")
print(sirkuit)

sirkuit[3] = "apip"
print(sirkuit)

sirkuit[0:1] = ["naufal", "rizky"]
print(sirkuit)

# nama_list[start:stop:stop]
sirkuit[0:5:2] = ["naufal", "rizki", "rahman"]
print(sirkuit)

del sirkuit[4]
print(sirkuit)



nama_dihapus = sirkuit.pop(5)
print(sirkuit)
print(nama_dihapus)

print(sirkuit[0:4:2])

matkul_1 = ["kalkulus", "logmat", "apd"]
matkul_2 = ["basis data", ""]

angka_gabung = angka1 + angka2
print(angka_gabung)

matkul_1 = matkul_1 * 5
print(matkul_1)


line_up = [
["Ferrari", "Leclerc", 16],
["Mercedes", "Hamilton", 44],
["Red Bull", "Verstappen", 1],
["McLaren", "Norris", 4]
]
print(line_up[2][1])

print(line_up[3:0])

for i in line_up:
    for j in i:
        print(j)


chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
listchara = list(chara)
print(type(listchara))

del listchara[6]

listchara.remove("Yukari")

listchara.append9("naruto")
print

chara = ("Yukari", "Yukino", "Odette", "Senku")
(Persona, Oregairu, Genshin, DrStone) = chara
print(Persona)
print(Oregairu)
