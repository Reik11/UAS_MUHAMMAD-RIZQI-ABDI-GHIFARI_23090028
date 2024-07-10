# Kelas parent
class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setRasa(self, rasa):
        self.rasa = rasa

    def information(self):
        return f"Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"

# Kelas child 
class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def setVitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        return f"{super().information()}, Vitamin: {self.vitamin}"

mangga1 = Mangga("Mangga Harum Manis", "Hijau", "Manis", "Vitamin C")

print("Atribut dan Metode:")
print(f"Nama: {mangga1.nama}")
print(f"Warna: {mangga1.warna}")
print(f"Rasa: {mangga1.rasa}")
print(f"Vitamin: {mangga1.vitamin}")

print("\nInformasi:")
print(mangga1.information())

mangga1.setNama("Mangga Gadung")
mangga1.setWarna("Kuning")
mangga1.setRasa("Asam Manis")
mangga1.setVitamin("Vitamin A")

print("\nInformasi Setelah Perubahan:")
print(mangga1.information())
