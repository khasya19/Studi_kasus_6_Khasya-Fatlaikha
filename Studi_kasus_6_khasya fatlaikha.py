import json
path = r"C:\Users\Khasya\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.11\praktikum\inventaris.json\inventaris.json"

with open(path, "r", encoding = "utf-8") as f:
    data = json.load(f)

def tambah_data(kode, nama, stok, harga):
    data.append({
        "nama": nama,
        "kode": kode,
        "stok": stok,
        "harga": harga
    })

    return "data ditambah"

def tampilkan_data():
    if len(data) == 0:
        return "belum ada barang digudang"

    print ("=" * 60)
    print(f"{'No':<4}{'kode':<10}{'nama barang':<22}{'stok':<8}{'harga':>12}")
    print ("=" * 60)
    for i, b in enumerate(data, start = 1):
        print(f"{i:<4}{b['kode']:<10}{b['nama']:<22}{b['stok']:<8}{b['harga']:>12}")
    print("=" * 60)
    return f"total jenis barang: {len(data)}"

def simpan_file():
    with open(path, "w", encoding = "utf-8") as f:
        json.dump(data, f, indent = 4)
        return"tersimpan barang ke path"

while True:
    print("\n======= SISTEM MANEJEMEN INVENTARIS BARANG =======")
    print("1. tampilkan semua barang")
    print("2. tambahkan barang baru")
    print("3. keluar")
    pilihan = input("pilih menu (1-3): ")

    if pilihan == "1":
        print()
        tampilkan_data()

    elif pilihan == "2":
        kode = input("kode barang: ")
        nama = input("nama barang: ")
        stok = int(input("jumlah stok: "))
        harga = int(input("harga satuan: "))

        print("\n", tambah_data(kode, nama, stok, harga))
        print("\n", simpan_file())

    elif pilihan == "3":
        print("Terima kasih....")
        break
    else:
        print("pilihan tidak valid, coba lagi")