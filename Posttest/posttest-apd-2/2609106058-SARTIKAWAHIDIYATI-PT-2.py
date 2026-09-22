skincare_1 = 35000
skincare_2 = 42000
skincare_3 = 50000
skincare_4 = 55000
skincare_5 = 68000
skincare_6 = 70000

ongkos_kirim = 12000

harga_skincare = [skincare_1, skincare_2, skincare_3, skincare_4, skincare_5, skincare_6]

total_pengeluaran = harga_skincare [0] + harga_skincare [1] + harga_skincare [2] + harga_skincare [3] + harga_skincare [4] + harga_skincare [5] + ongkos_kirim

rata_rata = total_pengeluaran / len(harga_skincare)

nim = 58
bolean = nim < rata_rata

kurs_yen = 113.67
total_pengeluaran_yen = total_pengeluaran / kurs_yen

skincare_3_sampai_5 = harga_skincare[-4:-1]

print("skincare 1: Rp", skincare_1)
print("skincare 2: Rp", skincare_2)
print("skincare 3: Rp", skincare_3)
print("skincare 4: Rp", skincare_4)
print("skimcare 5: Rp", skincare_5)
print("skincare 6: Rp", skincare_6)

print("total pengeluaran: Rp", total_pengeluaran)
print("rata rata: Rp", rata_rata)
print("nim:", nim)
print("bolean:", bolean)
print("kurs yen:", kurs_yen)
print("total pengeluaran yen: ¥", total_pengeluaran_yen)
print("skincare 3 sampai 5:", skincare_3_sampai_5)
