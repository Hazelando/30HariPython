# Fungsi untuk menginput data
def input_data():
    data = {}
    data['Nama'] = input("Masukkan Nama: ")
    data['Tempat Tanggal Lahir'] = input("Masukkan Tempat dan Tanggal Lahir (contoh: Jakarta, 1 Januari 2000): ")
    data['Agama'] = input("Masukkan Agama: ")
    data['Alamat'] = input("Masukkan Alamat: ")
    data['Gender'] = input("Masukkan Gender (L/P): ")
    return data

# Fungsi untuk menampilkan data
def tampilkan_data(data_list):
    for i, data in enumerate(data_list):
        print(f"\nData ke-{i+1}")
        for key, value in data.items():
            print(f"{key}: {value}")

def main():
    data_list = []
    while True:
        print("\n1. Input Data")
        print("2. Tampilkan Data")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            data_list.append(input_data())
        elif pilihan == '2':
            tampilkan_data(data_list)
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()