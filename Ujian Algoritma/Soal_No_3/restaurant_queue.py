# restaurant_queue.py
class RestaurantQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Order '{order}' telah ditambahkan ke dalam pesanan.")

    def dequeue(self):
        if len(self.queue) > 0:
            order = self.queue.pop(0)
            print(f"Order '{order}' telah dihilangkan dari pesanan.")
            return order
        else:
            print("Pesanan kosong, tidak ada pesanan untuk dihapus.")
            return None

    def display_queue(self):
        if len(self.queue) > 0:
            print("Pesanan Anda sekarang:")
            for i, order in enumerate(self.queue, 1):
                print(f"{i}. {order}")
        else:
            print("Pesanan kosong.")
