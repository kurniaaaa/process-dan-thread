import multiprocessing

def persegi(num):
    print("Luas Persegi      : {}\n".format(num * num))

def kubus(num):
    print("Keliling Persegi  : {}".format(num * 4))
  
  
if __name__ == "__main__":
    # Membuat Process
    panjang = int(input("Masukkan Angka Untuk Kalkukasi Luas Persegi dan Keliling : "))
    p1 = multiprocessing.Process(target=persegi, args=(panjang, ))
    p2 = multiprocessing.Process(target=kubus, args=(panjang, ))

    # Menjalankan Process
    p1.start()

    p2.start()
  
    # Menunggu Process Selesai
    p1.join()
    p2.join()
  
    # Process Selesai
    print("Process Selesai!")