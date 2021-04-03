# PROGRAM DISKON UMUR GANJIL
print(10*"=","SELAMAT DATANG DI TOKO POJOKSARI",10*"=")
total_belanja = (int(input("Masukkan total belanja anda: ")))
umur = (int(input("Masukkan umur anda: ")))
if umur %2 != 0:
    total_belanja = total_belanja - total_belanja * 10/100
    print("Selamat anda mendapatkan diskon sebesar 10%")
    print("Total yang harus dibayar:",total_belanja)
    bayar = int(input("Masukkan uang anda: "))
    if bayar > total_belanja:
        kembalian = bayar - total_belanja
        print("Kembalian anda sebesar:",kembalian,"rupiah, Terima kasih sunda belanja!")
    elif bayar == total_belanja:
        print("Uang anda pas, Terima kasih sudah belanja!")
    else:
        print("Maaf uang anda kurang")
else:
    print("Total yang harus dibayar:",total_belanja)
    bayar = int(input("Masukkan uang anda: "))
    if bayar > total_belanja:
        kembalian = bayar - total_belanja
        print("Kembalian anda sebesar:",kembalian,"rupiah, Terima kasih sunda belanja!")
    elif bayar == total_belanja:
        print("Uang anda pas, Terima kasih sudah belanja!")
    else:
        print("Maaf uang anda kurang")
