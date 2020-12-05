import iopesanan
import inputvalidation
import datetime


# PROGRAM UTAMA
iopesanan.readCSV()

print("Selamat Datang di Laundry Tracker!")

command = "1"
while (command != "4"):
    print("Silakan pilih command ID di bawah")
    print("1. Tambah pesanan")
    print("2. Ubah pesanan")
    print("3. Rekapitulasi penjualan")
    print("4. Keluar")
    command = input("Masukkan command: ")
    if (command == "1"):
        print()
        iopesanan.mainTambahPesanan()
    elif (command == "2"):
        print()
        iopesanan.mainUbahPesanan()
    elif (command == "3"):
        print()
        iopesanan.hasil()
    elif (command == "4"):
        print("Terima kasih sudah menggunakan Laundy Tracker!")
        exit()
    else:
        print("Command tidak tersedia, silakan masukkan command yang sesuai.\n") 
