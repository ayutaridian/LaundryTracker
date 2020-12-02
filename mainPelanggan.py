# import pesanan
import iopesanan
import csv

# Mencari dan menampilkan pesanan
def showPesanan():
    datap = []
    #earch untuk memanggil baris pesanan.csv yang sesuai
    bacacsv = open('pesanan.csv', mode='r')
    pesanan_reader = csv.DictReader(bacacsv)
    for row in pesanan_reader:
        datap.append(row) 
    idcust = input("Masukkan ID pesanan:")
    data_found = []

    index = 0
    for data in datap:
        if (data['customerID'] == idcust):
            data_found = datap[index]

        if len(data_found) > 0:
            print (f"Order ID: {data_found['orderID']}")
            print (f"Customer ID: {data_found['customerID']}")
            print (f"Berat: {data_found['berat']}")
            print (f"Jenis Cucian: {data_found['cucian']}")
            print (f"Status: {data_found['status']}")
            print (f"Harga: {data_found['hargaBayar']}")
            print (f"Status Bayar: {data_found['statusBayar']}")
            print (f"Jenis Layanan: {data_found['jenisLayanan']}")
            print (f"Tanggal Masuk Pesanan: {data_found['tanggalMasukPesanan']}")
            print (f"Tanggal Pesanan Selesai: {data_found['tanggalPesananSelesai']}")
            print (f"Cara Penyerahan: {data_found['caraPenyerahan']}")
        else:
            print("Data tidak ditemukan")


print("Selamat Datang di Laundry Tracker!")

command = "1"
while (command != "2"):
    print("Silakan pilih command ID di bawah")
    print("1. Lihat status pesanan")
    print("2. Keluar")
    command = input("Masukkan command: ")
    if (command == "1"):
        print("Untuk melihat status pesanan, silakan masukkan kode pesanan Anda.")
        # Fungsi menampilkan pesanan, input ID di dalam fungsi
        showPesanan()
    elif (command == "2"):
        print("Terima kasih sudah menggunakan Laundy Tracker!")
        exit()
    else:
        print("Command tidak tersedia, silakan masukkan command yang sesuai.\n") 