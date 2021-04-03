print(7*"<","SELAMAT DATANG DI PROGRAM BUTIK",">"*7)
print("1. Kaos")
print("2. Kemeja")
print("3. Jas")
print("4. Selesai")
kaos = 25000
kemeja = 50000
jas = 100000
total = 0
while True:
    beli = str(input("Masukkan barang yang ingin dibeli (1/2/3/4): "))
    if beli == "1" or beli == "kaos" or beli == "Kaos":
        print("Kaos ditambahkan")
        total += kaos
    elif beli == "2" or beli == "kemeja" or beli == "Kemeja":
        print("Kemeja ditambahkan")
        total += kemeja
    elif beli == "3" or beli == "jas" or beli == "Jas":
        print("Jas ditambahkan")
        total += jas
    elif beli == "4" or beli == "selesai" or beli == "Selesai" :
        print("Total yang harus dibayar:",total)
        break
    else:
        print("Inputan anda salah, opsi yang tersedia adalah (1/2/3/4)")
bayar = int(input("Masukkan uang anda: "))
if bayar == total:
    print("Uang anda sudah pas, Terima kasih sudah belanja!")
elif bayar > total:
    kembalian = bayar - total
    print("Kembalian anda sebesar",kembalian,"Terima kasih sudah belanja!")
elif bayar < total:
    kurang = total - bayar
    print("Mohon maaf uang anda kurang sebesar",kurang)
