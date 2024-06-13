#Aplikasi To-Do List
to_do_list = []

while True:
    print("1. Tambah Tugas")
    print("2. Tandai Selesai")
    print("3. Keluar")
    pilihan = input("Pilih tindakan: ")

    if pilihan == '1':
        tugas_baru = input("Masukkan tugas baru: ")
        to_do_list.append(tugas_baru)
    elif pilihan == '2':
        print("Tugas yang belum selesai:")
        for tugas in to_do_list:
            print("-", tugas)
        tugas_selesai = input("Masukkan tugas yang selesai: ")
        if tugas_selesai in to_do_list:
            to_do_list.remove(tugas_selesai)
        else:
            print("Tugas tidak ditemukan dalam daftar.")
    elif pilihan == '3':
        break
    else:
        print("Pilihan tidak valid.")