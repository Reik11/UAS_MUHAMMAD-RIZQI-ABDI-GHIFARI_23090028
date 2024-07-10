# main.py
from restaurant_queue import RestaurantQueue

def main():
    restaurant_queue = RestaurantQueue()
    
    while True:
        print("\nMenu:")
        print("1. Tambahkan Pesanan")
        print("2. Hapus Pesanan")
        print("3. Tampilkan Pesanan Saat Ini")
        print("4. Keluar")
        
        choice = input("Masukan Pilihan (1-4): ")

        if choice == '1':
            order = input("Masukan pesanan untuk ditambahkan: ")
            restaurant_queue.enqueue(order)
        elif choice == '2':
            restaurant_queue.dequeue()
        elif choice == '3':
            restaurant_queue.display_queue()
        elif choice == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan salah, tolong pilih antara 1 sampai 4.")

if __name__ == "__main__":
    main()
