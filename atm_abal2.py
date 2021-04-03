# PROGRAM ATM
print()
print(10*"=","SELAMAT DATANG DI ATM BANK XXX",10*"=")
penarikan = int(input("Berapa jumlah penarikan yang akan dilakukan : "))
pecahan = int(input("""
1. Seratus ribu
2. Lima puluh ribu
3. Dua puluh ribu
4. Sepuluh ribu
Pilih pecahan yang diinginkan : """))
if pecahan == 1:
   if penarikan < 100000:
      print("\nMohon maaf jumlah penarikan lebih kecil dari pecahan yang dipilih")
   else:
      jumlah = penarikan // 100000
      print("\nSelamat anda berhasil melakukan penarikan sebesar", jumlah * 100000,
            "dengan pecahan 100 ribu sebanyak", jumlah, "lembar")

elif pecahan == 2:
   if penarikan < 50000:
      print("\nMohon maaf jumlah penarikan lebih kecil dari pecahan yang dipilih")
   else:
      jumlah = penarikan // 50000
      print("\nSelamat anda berhasil melakukan penarikan sebesar", jumlah * 50000,
            "dengan pecahan 50 ribu sebanyak", jumlah, "lembar")

elif pecahan == 3:
   if penarikan < 20000:
      print("\nMohon maaf jumlah penarikan lebih kecil dari pecahan yang dipilih")
   else:
      jumlah = penarikan // 20000
      print("\nSelamat anda berhasil melakukan penarikan sebesar", jumlah * 20000,
            "dengan pecahan 20 ribu sebanyak", jumlah, "lembar")

elif pecahan == 4:
   if penarikan < 10000:
      print("\nMohon maaf jumlah penarikan lebih kecil dari pecahan yang dipilih")
   else:
      jumlah = penarikan // 10000
      print("\nSelamat anda berhasil melakukan penarikan sebesar", jumlah * 10000,
            "dengan pecahan 10 ribu sebanyak", jumlah, "lembar")

else:
   print("\nMohon untuk memilih pecahan sesuai dengan menu")
