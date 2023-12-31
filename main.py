from dataclasses import dataclass
from prettytable import PrettyTable
    
@dataclass
class OutputHarga:
    no: int
    jenisRoti: str
    variantRoti: str
    jumlahBeli: int
    hargaSatuan: int
    jumlahHarga: int
    
# Create Data Transfer Object for Response Text
@dataclass
class OutputData:
    name: str
    noTelp: str
    totalHarga: int
    diskon: int
    totalBayar: int

head = PrettyTable(["No", "Jenis Roti", "Variant Rasa", "Jumlah Beli", "Harga Satuan", "Total Harga"])

def headerStyle() -> None:
    """
    # Description
    Fungsi ini bertugas untuk
    menampilkan list jenis roti
    di awal tampilan atau dipaling atas
    """
    print("\t\tToko Roti")
    print("=========================================")
    header = PrettyTable(["Kode", "Jenis Roti", "Jumlah Variant"])
    header.add_row(["1", "Roti Tawar", "3"])
    header.add_row(["2", "Roti Panada", "2"])
    header.add_row(["3", "Roti Buaya", "2"])
    header.add_row(["4", "Roti Odading", "3"])
    header.add_row(["5", "Roti Sisir", "2"])
    header.add_row(["6", "Roti Ganjel Rel", "2"])
    header.align = "l"
    print(header)
  
def printOutVariant(kode: int) -> None:
    """
    # Description
    Fungsi ini bertugas untuk
    menampilkan list jenis variant dan harga
    ketika sudah memilih jenis roti
    """

    if kode == 1:    
        print("Kode     Jenis Variant           Harga")
        print("1.       Roti Tawar Coklat       Rp. 10.000")
        print("2.       Roti Tawar Original     Rp. 7.000")
        print("3.       Roti Tawar Pandan       Rp. 8.000")
    elif kode == 2:
        print("Kode     Jenis Variant           Harga")        
        print("1.       Roti Panada Coklat      Rp. 3.000")
        print("2.       Roti Panada Keju        Rp. 3.000")
    elif kode == 3:
        print("Kode     Jenis Variant           Harga")
        print("1.       Roti Buaya Daging       Rp. 500.000")
        print("2.       Roti Buaya Original     Rp. 300.000")
    elif kode == 4:
        print("Kode     Jenis Variant           Harga")
        print("1.       Roti Odading Coklat     Rp. 2.000")
        print("2.       Roti Odading Original   Rp. 1.000")
        print("3.       Roti Odading Pandan     Rp. 2.000")
    elif kode == 5:
        print("Kode     Jenis Variant           Harga")
        print("1.       Roti Sisir Keju         Rp. 2.000")
        print("2.       Roti Sisir Coklat       Rp. 2.000")
    else:
        print("Kode     Jenis Variant               Harga")    
        print("1.       Roti Ganjel Rel Coklat      Rp. 35.000")
        print("2.       Roti Ganjel Rel Original    Rp. 20.000")
        print("3.       Roti Ganjel Rel Keju        Rp. 30.000")

def logicBuy( kode: int, variant: int, banyakbeli: int) -> any:
    """
    # Description
    Fungsi ini untuk membuat logic
    dari pembelian, yang dibutuhkan parameter
    kode (jenis roti) dan variant

    Args:
        kode (int): input value untuk jenis roti / kode roti
        variant (int): input value untuk variant roti

    Returns:
        any: return 3 data, nama roti, nama variant, dan harga
    """
    if kode == 1:
        jenisRoti = "Roti Tawar"
        if variant == 1:
            jenisVariant = "Coklat"
            harga = 10000
            total_harga = harga * banyakbeli
            
        elif variant == 2:
            jenisVariant = "Original"
            harga = 7000
            total_harga = harga * banyakbeli
        else:
            jenisVariant = "Pandan"
            harga = 8000
            total_harga = harga * banyakbeli
    elif kode == 2:
        jenisRoti = "Roti Panada"
        if variant == 1:
            jenisVariant = "Coklat"
            harga = 3000
            total_harga = harga * banyakbeli
        else:
            jenisVariant = "Keju"
            harga = 3000
            total_harga = harga * banyakbeli
    elif kode == 3:
        jenisRoti = "Roti Buaya"
        if variant == 1:
            jenisVariant = "Daging"
            harga = 500000
            total_harga = harga * banyakbeli
        else:
            jenisVariant = "Original"
            harga = 300000
            total_harga = harga * banyakbeli
    elif kode == 4:
        jenisRoti = "Roti Odading"
        if variant == 1:
            jenisVariant = "Coklat"
            harga = 2000
            total_harga = harga * banyakbeli
        elif variant == 2:
            jenisVariant = "Original"
            harga = 1000
            total_harga = harga * banyakbeli
        else:
            jenisVariant = "Pandan"
            harga = 2000
            total_harga = harga * banyakbeli
    elif kode == 5:
        jenisRoti = "Roti Sisir"
        if variant == 1:
            jenisVariant = "Keju"
            harga = 2000
            total_harga = harga * banyakbeli
        else:
            jenisVariant = "Coklat"
            harga = 2000
            total_harga = harga * banyakbeli
    else:
        jenisRoti = "Roti Ganjel Rel"
        if variant == 1:
            jenisVariant = "Coklat"
            harga = 35000
            total_harga = harga * banyakbeli
        elif variant == 2:
            jenisVariant = "Original"
            harga = 20000
            total_harga = harga * banyakbeli
        else:
            jenisVariant = "Keju"
            harga = 30000
            total_harga = harga * banyakbeli
    
    
    return jenisVariant, harga, jenisRoti, total_harga

def outputHarga(response: OutputHarga) -> None:
    """
    # Description
    Fungsi ini bertugas untuk 
    menampilkan output dari hasil pembelian
    ke dalam bentuk tabel
    
    Args:
        response (Response): input value dto Response
    """
    head.add_row([response.no, response.jenisRoti, response.variantRoti, response.jumlahBeli, response.hargaSatuan, response.jumlahHarga])

def output(response: OutputData) -> None:
    """
    # Description
    Fungsi ini untuk menampikan 
    print output dari hasil input
    yang telah dilakukan

    Args:
        response (Output): input value dto output
    """
    print("=========================================")
    print(f"Nama Pembeli        : {response.name}")
    print(f"No Telepon          : {response.noTelp}")
    print(f"{head}")
    print("==========================================")
    print(f"Total Harga         : Rp. {response.totalHarga}")
    print(f"Diskon              : Rp. {response.diskon}")
    print(f"Total Bayar         : Rp. {response.totalBayar}")
    print("==========================================")


def main() -> None:
    """
    # Description
    Fungsi ini untuk semua logic
    pemrograman dari Toko Roti
    """
    headerStyle()
    print("==========================================")
    nama = input("Nama Pembeli  : ")
    noTelp = input("No Telepon  : ")
    banyakBeli = int(input("Mau Beli Berapa Jenis ? : "))
    
    listJumlaHarga = []
    listJenisRoti = []
    totalPrice = 0  
    
    for i in range(banyakBeli):
        i = i + 1
        print('\n' + f"Pembelian ke {i}")
        kodeRoti = int(input("Pilih Jenis Roti [ 1/2/3/4/5/6 ]: "))
        printOutVariant(kodeRoti)
        kodeVariant = int(input("Pilih Jenis Variant [ ex. 1 ]: "))
        jumlahBeli = int(input("Masukan Jumlah Beli : "))
        jenisVariant, harga, jenisRoti, total_harga = logicBuy(kodeRoti, kodeVariant, jumlahBeli)
        
        # result Response
        result = OutputHarga(
            no=i,
            jenisRoti=jenisRoti,
            variantRoti=jenisVariant,
            jumlahBeli=jumlahBeli,
            hargaSatuan=harga,
            jumlahHarga=total_harga,
        )
        
        # result to tabel
        outputHarga(response=result)
        listJumlaHarga.append(total_harga)
        listJenisRoti.append(jenisRoti)
    
    for resultPembayaran in listJumlaHarga:
        totalPrice += resultPembayaran
    
    if totalPrice > 100000:
        diskon = 0.1 * totalPrice
    else:
        diskon = 0
    
    total_bayar = totalPrice - diskon
    print('\n' + "\tTotal dan Hasil Pembelian")
    
    responses = OutputData(
        name=nama,
        noTelp=noTelp,
        totalHarga=totalPrice,
        diskon=diskon,
        totalBayar=total_bayar,
    )
    output(response=responses)
    
    print("==========================================")
    uangBayar = int(input("Uang Bayar          : Rp. "))
    uangKembali = uangBayar - total_bayar
    print(f"Total Kembalian     : Rp. {uangKembali}")
    print("==========================================")
    print("\tTerimakasih Telah Membeli")
    print("\n")

# Running function main 
if __name__ == "__main__":
    while True:
        addData = input("Ingin beli roti ? (y/n): ")
        if addData == "y":
            main()
        else:
            break