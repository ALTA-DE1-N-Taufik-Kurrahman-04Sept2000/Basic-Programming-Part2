'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''
Diskon      = 15
Harga_Awal  = 370000

Harga_Diskon    = (Diskon/100) * Harga_Awal
Harga_Akhir     = Harga_Awal - Harga_Diskon

print("Harga yang harus dibayar adalah Rp.", Harga_Akhir)