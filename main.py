n = int(input("Masukkan n barang"))

daftar_barang = []
for i in range(1,n+1):
    barang = input(f"barang ke-{i}")
    daftar_barang.append(barang)

print(daftar_barang)
