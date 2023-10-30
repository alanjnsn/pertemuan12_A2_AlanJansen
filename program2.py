from matematika import luas_persegi
from matematika import luas_lingkaran
from matematika import luas_segitiga

#Mencetak Menu
def menu():
    while True: 
        print('Pilih Bentuk 2D')
        print()
        print('1. Persegi Panjang')
        print('2. Lingkaran')
        print('3. Segitiga')
        print('4. Keluar')
        pilihan= int(input('pilih berdasarkan nomor: '))
        if pilihan==1:
            luas_persegi.persegi()
        elif pilihan==2:
            luas_lingkaran.lingkaran()
        elif pilihan==3:
            luas_segitiga.segitiga()
        elif pilihan==4:
            break

menu()