# n = int(input("Masukkan jumlah barang: "))
# daftar_belanja = []
# for i in range(1,n+1):
#     barang = input(f"Nama barang ke-{i}: ")
#     daftar_belanja.append(barang)
# print(f"Daftar Belanja\n {daftar_belanja}")

# nilai = [80, 75, 65, 88]
# print(f" Nilai pertama: {nilai[0]}\n Nilai terakhir: {nilai[-1]}\n Tiga nilai pertama: {nilai[0:3]}\n Total nilai pertama: {sum(nilai)}\n Rata-rata nilai: {sum(nilai)/len(nilai)}")

# n = int(input("Masukkan jumlah data: "))
# nilai = []

# for i in range(1,n+1):
#     input_n = int(input(f" Nilai ke-{i}: "))
#     nilai.append(input_n)

# maks = nilai[0]
# mins = nilai[0]
# for i in range(1, len(nilai)):
#     if nilai[i] > maks:
#         maks = nilai[i]
#     elif input_n < nilai[i]:
#         mins = nilai[i]
        
# print(nilai)
# print(maks)
# print(mins)

# tugas = ['Membaca', 'Olahraga']
# tugas.append("Mengerjakan PR")
# tugas.insert(0, "Sarapan")
# tugas.remove("Olahraga")
# print(tugas)

# n = int(input("Masukkan jumlah barang: "))
# nama = []
# harga = []
# rata_rata = 0
# for i in range(1, n+1):
#     nama_barang = input(f"Nama barang ke-{i}: ")
#     harga_barang = int(input(f"Harga {nama_barang}: "))
#     nama.append(nama_barang)
#     harga.append(harga_barang)
# rata_rata = sum(harga)/len(harga)

# barang_mahal = [] 
# for j in range(len(nama)):
#     if harga[j] > rata_rata:
#         barang_mahal.append(nama[j])

# print(f"Rata-rata: {rata_rata}")
# print(f"Barang di atas rata-rata: {barang_mahal}")

# print("\n=== Latihan 7 ===")
# matriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print("Matriks:")
# for baris in matriks:
#     for elemen in baris:
#         print(elemen, end=" ")
#     print()

print("\n=== Latihan 8 ===")
nilai_siswa = [[80, 75, 90], [65, 70, 72], [88, 92, 95]]
for i in range(len(nilai_siswa)):
    total = 0
    for mapel in nilai_siswa[i]:
        total += mapel
    rata_rata = total / len(nilai_siswa[i])
    print(f"Siswa ke-{i + 1}: total = {total}, rata-rata = {round(rata_rata, 2)}")