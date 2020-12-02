import iopesanan
import csv

# Mencari dan menampilkan pesanan
def getPesanan(idcust):
    datap = []
    # Search untuk memanggil baris pesanan.csv yang sesuai
    bacacsv = open('pesanan.csv', mode='r')
    pesanan_reader = csv.DictReader(bacacsv)
    for row in pesanan_reader:
        datap.append(row) 
    data_found = []

    index = 0
    for data in datap:
        if (data['customerID'] == idcust):
            data_found = datap[index]

        if len(data_found) > 0:
            orderID = {data_found['orderID']}
            customerID = {data_found['customerID']}
            berat = {data_found['berat']}
            cucian = {data_found['cucian']}
            status = {data_found['status']}
            hargaBayar = {data_found['hargaBayar']}
            statusBayar = {data_found['statusBayar']}
            jenisLayanan = {data_found['jenisLayanan']}
            tanggalMasukPesanan = {data_found['tanggalMasukPesanan']}
            tanggalPesananSelesai = {data_found['tanggalPesananSelesai']}
            caraPenyerahan = {data_found['caraPenyerahan']}

            return (orderID, customerID, berat, cucian, status, hargaBayar, statusBayar, jenisLayanan, tanggalMasukPesanan, tanggalPesananSelesai, caraPenyerahan)
        else:
            print("Data tidak ditemukan")