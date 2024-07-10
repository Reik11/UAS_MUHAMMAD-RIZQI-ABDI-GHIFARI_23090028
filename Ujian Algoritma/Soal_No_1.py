def main():
    mahasiswa = []
    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        mahasiswa.append({"NIM": nim, "Nama": nama})
        
        tambah_lagi = input("Ingin Tambah Lagi? (YA/TIDAK): ")
        if tambah_lagi.lower() != "ya":
            break
    
    print("\nData Mahasiswa:")
    for data in mahasiswa:
        print(f"NIM: {data['NIM']}, Nama: {data['Nama']}")

if __name__ == "__main__":
    main()
