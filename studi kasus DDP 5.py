def biaya_masuk_parkir_kendaraan (jenis_kendaraan, durasi) :
    if jenis_kendaraan == "mobil" :
        tarif_per_jam = 5000
    elif jenis_kendaraan == "motor" :
        tarif_per_jam = 3000

    total_tarif = tarif_per_jam * durasi 
    return total_tarif

while True :
    print ("Tarif parkir :")
    print ("1. parkir mobil")
    print ("2. parkir motor")
    print ("3. memberhentikan program")

    pilihan = input ("pilih menu 1-3 :")

    if pilihan == "1" or pilihan == "2" :
        if pilihan == "1" :
            jenis = "mobil"
        elif pilihan == "2" :
            jenis = "motor"
        jam_masuk = int(input ("masukan jam masuk kendaraan :"))
        jam_keluar = int(input ("masukan jam keluar kendaraan :"))
        lama_parkir = jam_keluar - jam_masuk
        biaya_total = biaya_masuk_parkir_kendaraan (jenis, lama_parkir)

        print("---Struk Parkir---")
        print("Jenis Kendaraan :", jenis)
        print("Jam Masuk       :", jam_masuk)
        print("Jam Keluar      :", jam_keluar)
        print("Lama Parkir     :", lama_parkir, "jam")
        print("Total Biaya     : Rp", biaya_total)

    elif pilihan == "3" :
        print ("program berhenti.")
        break

    else :
        print ("nomor tidak valid")