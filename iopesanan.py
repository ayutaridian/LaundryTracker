import datetime
import inputvalidation
import pandas as pd
import csv

# inisialisasi jumlah pesanan
jumlahPesanan = 0

'''def buatDataPesanan():
    # Inisialisasi data pesanan
    fieldnames = ['orderID', 'customerID', 'berat', 'cucian', 'status', 'hargaBayar', 'statusBayar', 'jenisLayanan', 'tanggalMasukPesanan', 'tanggalPesananSelesai', 'caraPenyerahan']
    writer = csv.DictWriter(datapesanan, fieldnames=fieldnames)
    writer.writeheader()'''

def readCSV():
    # membaca csv
    rdatapesanan =  open('pesanan.csv', 'r')
    rdatapesanan.close()

def tambahPesanan(customerID, berat, cucian, status, hargaBayar, statusBayar, jenisLayanan, tanggalMasukPesanan, caraPenyerahan):
    # menulis csv
    wdatapesanan = open('pesanan.csv','a')
    writer = csv.writer(wdatapesanan)

    global jumlahPesanan

    # Menerima data pesanan baru dan dimasukkan ke pesanan.csv
    writer = csv.writer(wdatapesanan, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([jumlahPesanan+1, customerID, berat, cucian, status, hargaBayar, statusBayar, jenisLayanan, tanggalMasukPesanan, 'NULL', caraPenyerahan])

    # Mengubah variabel global jumlahPesanan
    jumlahPesanan += 1

    print("Pesanan berhasil ditambahkan.")

    # Menutup csv
    wdatapesanan.close()
def ubahPesanan(orderID1, status1, statusBayar1):
    datap = []
    #fungsi search untuk memanggil baris pesanan.csv yang sesuai
    bacacsv = open('pesanan.csv', mode='r')
    pesanan_reader = csv.DictReader(bacacsv)
    for row in pesanan_reader:
        datap.append(row) 
    data_found = []

    index = 0
    for data in datap:
        if (data['orderID'] == orderID1):
            data_found = datap[index]
        #fungsi mengubah pesanan
        if (data['orderID'] == orderID1):
            datap[index]['status'] = status1
            datap[index]['statusBayar'] = statusBayar1
            if (data['statusBayar'] == "Lunas"):
                datap[index]['tanggalPesananSelesai'] = datetime.datetime.now().strftime("%x") #otomatis set waktu hari ini
        index = index + 1 

    fieldnames = ['orderID', 'customerID', 'berat', 'cucian', 'status', 'hargaBayar', 'statusBayar', 'jenisLayanan', 'tanggalMasukPesanan', 'tanggalPesananSelesai', 'caraPenyerahan']
    updatecsv = open('pesanan.csv', mode='w')
    pesanan_update = csv.DictWriter(updatecsv, fieldnames=fieldnames)
    pesanan_update.writeheader()
    for data_baru in datap:
        pesanan_update.writerow({'orderID': data_baru['orderID'], 'customerID': data_baru['customerID'], 'berat': data_baru['berat'], 'cucian': data_baru['cucian'], 'status': data_baru['status'], 'hargaBayar': data_baru['hargaBayar'], 'statusBayar': data_baru['statusBayar'], 'jenisLayanan': data_baru['jenisLayanan'], 'tanggalMasukPesanan': data_baru['tanggalMasukPesanan'], 'tanggalPesananSelesai': data_baru['tanggalPesananSelesai'], 'caraPenyerahan': data_baru['caraPenyerahan']})

    updatecsv.close()
    
# Mengubah Pesanan
def mainUbahPesanan():
    datap = []
    #fungsi search untuk memanggil baris pesanan.csv yang sesuai
    bacacsv = open('pesanan.csv', mode='r')
    pesanan_reader = csv.DictReader(bacacsv)
    for row in pesanan_reader:
        datap.append(row) 
    idord = input("Masukkan ID Order yang akan diubah:")
    data_found = []

    index = 0
    for data in datap:
        if (data['orderID'] == idord):
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
        #fungsi mengubah pesanan
        if (data['orderID'] == idord):
            keputusan = input("Ingin mengubah status proses laundry? [Y/N]")
            if(keputusan=="Y"):
                print("Pilihan: ")
                print("1. Dicuci")
                print("2. Dikeringkan")
                print("3. Disetrika")
                print("4. Siap diambil")
                print("5. Dalam Pengantaran")
                statusint = inputvalidation.inputInt("Status")
                if (statusint == 1):
                    datap[index]['status'] = "Dicuci"
                elif (statusint == 2):
                    datap[index]['status'] = "Dikeringkan" 
                elif (statusint == 3):
                    datap[index]['status'] = "Disetrika"
                elif (statusint == 4):
                    datap[index]['status'] = "Siap diambil"
                elif (statusint == 5):
                    datap[index]['status'] = "Dalam Pengantaran"
                else:
                    print("Input salah. Silakan coba lagi")

            keputusan2 = input("Ingin mengubah status pembayaran? [Y/N]")
            if(keputusan2=="Y"):
                datap[index]['tanggalPesananSelesai'] = datetime.datetime.now().strftime("%x") #otomatis set waktu hari ini
                datap[index]['statusBayar'] = "Lunas"
        index = index + 1 

    fieldnames = ['orderID', 'customerID', 'berat', 'cucian', 'status', 'hargaBayar', 'statusBayar', 'jenisLayanan', 'tanggalMasukPesanan', 'tanggalPesananSelesai', 'caraPenyerahan']
    updatecsv = open('pesanan.csv', mode='w')
    pesanan_update = csv.DictWriter(updatecsv, fieldnames=fieldnames)
    pesanan_update.writeheader()
    for data_baru in datap:
        pesanan_update.writerow({'orderID': data_baru['orderID'], 'customerID': data_baru['customerID'], 'berat': data_baru['berat'], 'cucian': data_baru['cucian'], 'status': data_baru['status'], 'hargaBayar': data_baru['hargaBayar'], 'statusBayar': data_baru['statusBayar'], 'jenisLayanan': data_baru['jenisLayanan'], 'tanggalMasukPesanan': data_baru['tanggalMasukPesanan'], 'tanggalPesananSelesai': data_baru['tanggalPesananSelesai'], 'caraPenyerahan': data_baru['caraPenyerahan']})

    updatecsv.close()
# DIGUNAKAN DI MAIN KARYAWAN
def mainJenisLayanan():
    print("Pilihan jenis layanan:")
    print("1. Lavender")
    print("2. Rose")
    print("3. Vanilla")
    jenislayananint = inputvalidation.inputInt("Jenis layanan")
    if (jenislayananint == 1):
        return 'Lavender'
    elif (jenislayananint == 2):
        return 'Rose'
    elif (jenislayananint == 3):
        return 'Vanilla'
    else:
        print("Input salah. Silakan coba lagi")

def mainCaraPenyerahan():
    print("Pilihan cara penyerahan:")
    print("1. Diambil")
    print("2. Diantar")
    carapenyerahanint = inputvalidation.inputInt("Cara penyerahan")
    if (carapenyerahanint == 1):
        return 'Diambil'
    elif (carapenyerahanint == 2):
        return 'Diantar'
    else:
        print("Input salah. Silakan coba lagi")

def mainTambahPesanan():
    print("Masukkan data pesanan yang ingin ditambahkan.")

    # Biaya cucian per kg
    hargaperkg = 7000

    # Input customer ID yang memesan
    customerid = inputvalidation.inputInt("Customer ID")

    # Input berat dari cucian
    beratcucian = inputvalidation.inputFloat("Berat cucian (kg)")

    # Input jenis pakaian yang dicuci
    jumlahcucian = inputvalidation.inputInt("Jumlah cucian")
    print("Masukkan jenis pakaian yang dicuci.")
    print("Contoh: Kemeja, Jaket, Kaos, Rok, dll.")
    isicucian = inputvalidation.inputList(jumlahcucian)
    
    # Menghitung biaya cucian
    hargabayar = int(round(beratcucian * hargaperkg))

    # Input jenis layanan
    jenislayanan = mainJenisLayanan()
    while not (jenislayanan == 'Lavender' or jenislayanan == 'Rose' or jenislayanan == 'Vanilla'):
        jenislayanan = mainJenisLayanan()
    
    # Input cara penyerahan setelah laundry selesai
    carapenyerahan = mainCaraPenyerahan()
    while not (carapenyerahan == 'Diambil' or carapenyerahan == 'Diantar'):
        carapenyerahan = mainCaraPenyerahan()

    # Tanggal mulai pesanan otomatis tanggal hari ini
    tanggalmulai = datetime.datetime.now().strftime("%x") # otomatis tanggal hari ini

    # Input data pesanan ke pesanan.csv
    tambahPesanan(customerid, beratcucian, isicucian, 'Dalam antrean', hargabayar, 'Belum lunas', jenislayanan, tanggalmulai, carapenyerahan)

def harga(tglSelesai):
    df = pd.read_csv (r'pesanan.csv')
    #gsum1 = df.groupby(['caraPenyerahan']).sum('hargaBayar')
    #print ('Pendapatan per tanggal: ' + str(gsum1)+"\n")
    sum1 = sum(df[df['tanggalPesananSelesai']==tglSelesai]['hargaBayar'])
    print ('\nPendapatan: ' + str(sum1))
    return (sum1)

def jmlPesanan(dateSelesai):
    df = pd.read_csv (r'pesanan.csv')
    #gsum1 = df.groupby(['caraPenyerahan']).sum('hargaBayar')
    #print ('Pendapatan per tanggal: ' + str(gsum1)+"\n")
    count = len(df[df['tanggalPesananSelesai'] == dateSelesai])
    print ('Jumlah Pesanan: ' + str(count)+"\n")
    return (count)
         
def allRekap(inputtgl) :
    harga(inputtgl)
    jmlPesanan(inputtgl)

def hasil() :
    tanggalSelesai = input("Masukkan tanggal yang ingin dicari:")
    allRekap(tanggalSelesai)
