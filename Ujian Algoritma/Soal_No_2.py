import pandas as pd

data = {
    'Nama': ['Mahasiswa 1', 'Mahasiswa 2', 'Mahasiswa 3'],
    'Algoritma dan Struktur Data 2': [90, 50, 65],
    'Matematika Numerik': [80, 60, 70]
}

df = pd.DataFrame(data)

print("Data Mahasiswa:")
print(df)

rata_rata_mata_kuliah = df.mean(axis=0, numeric_only=True)
print("\nRata-rata nilai untuk setiap mata kuliah:")
print(rata_rata_mata_kuliah)

df['Rata-rata Mahasiswa'] = df.mean(axis=1, numeric_only=True)
print("\nData Mahasiswa dengan rata-rata nilai:")
print(df[['Nama', 'Rata-rata Mahasiswa']])
