import numpy as np

print("<<<<< KALKULATOR INVERS DAN DETERMINAN MATRIKS >>>>>")
isi_list = ()
isi_matriks = []
elemen = int(input("Masukkan dimensi matriks: "))
for i in range(elemen):
    isi_list = [int(item) for item in input("Masukkan baris ke-{}: ".format(i+1)).split()]
    isi_matriks.append(isi_list)

x = np.array(isi_matriks)
print()
print("Matriks kamu:")
print(x)

print("\nPengen ngitung apa?\n","1. Determinan\n","2. Invers")
menu = int(input("Masukkan pilihan kamu (1/2): "))
if menu == 1:
    try:
        det_x = np.linalg.det(x)
        print()
        print("Determinan:",int(det_x))
        if det_x == 0:
            print("Matriks tersebut merupakan matriks singular")
    except:
        print("Matriks tersebut bukan matriks persegi!")

elif menu == 2:
    try: 
        inv_x = np.linalg.inv(x)
        print()
        print("Invers:")
        print(inv_x)
    except:
        print("Matriks tidak memiliki solusi")

else:
    print("Masukkan pilihan yang benar! (1/2)")
