def hitung_mobil():
    jumlah_mobil = {'Solo': 0, 'Surabaya': 0, 'Jogja': 0, 'Magelang': 0}
    
    while True:
        data = input("Masukkan asal mobil (Solo, Surabaya, Jogja, atau Magelang) atau ketik 'done' jika selesai: ").capitalize()
        
        if data == 'Done':
            break
        
        if data in jumlah_mobil:
            jumlah_mobil[data] += 1
        else:
            print("Asal mobil tidak valid!")
    
    [print(f"Jumlah mobil dari {kota}\t: {jumlah}") for kota, jumlah in jumlah_mobil.items()]

hitung_mobil()