def ganti_kata(kalimat, cari, ganti):
    kalimat_baru = ''
    for kata in kalimat.split():
        if kata == cari:
            kalimat_baru += ganti + ' '
        else:
            kalimat_baru += kata + ' '
    return kalimat_baru.strip()

kalimat = input("Masukkan kalimat: ")
cari = input("Masukkan kata yang ingin diganti: ")
ganti = input("Masukkan kata pengganti: ")

kalimat_baru = ganti_kata(kalimat, cari, ganti)
print("Kalimat baru: ", kalimat_baru)
