from services.inventory_service import InventoryService
from models.item import Item


def show_menu():
    print("\n=== APLIKASI INVENTARIS BARANG ===")
    print("0. Keluar")
    print("1. Tambah Barang")
    print("2. Edit Barang")
    print("3. Hapus Barang")
    print("4. Lihat Semua Barang")
    print("5. Cari Barang")
    print("6. Hitung Total Stok")


def main():
    service = InventoryService()

    while True:
        show_menu()
        choice = input("Pilih menu: ")

        if choice == "1":
            nama = input("Nama barang: ")
            harga = int(input("Harga barang: "))
            stok = int(input("Jumlah stok: "))

            # urutan: name, quantity, price
            item = Item(nama, stok, harga)

            service.add_item(item)

            print("Barang berhasil ditambahkan.")

        elif choice == "2":
            nama = input("Masukkan nama barang yang ingin diedit: ")
            item = service.find_item(nama)

            if item:
                harga_baru = int(input("Harga baru: "))
                stok_baru = int(input("Stok baru: "))
                service.update_item(nama, stok_baru, harga_baru)
                print("Barang berhasil diupdate.")
            else:
                print("Barang tidak ditemukan.")

        elif choice == "3":
            nama = input("Masukkan nama barang yang ingin dihapus: ")
            service.delete_item(nama)
            print("Barang berhasil dihapus (jika ada).")

        elif choice == "4":
            items = service.get_all_items()

            if not items:
                print("Belum ada barang.")
            else:
                print("\n=== DAFTAR BARANG ===")
                for item in items:
                    print(f"Nama: {item.name}")
                    print(f"Harga: {item.price}")
                    print(f"Stok: {item.quantity}")
                    print("----------------------")
        
        elif choice == "5":
            nama = input("Masukkan nama barang yang ingin dicari: ")
            item = service.find_item(nama)

            if item:
                    print("\n=== HASIL PENCARIAN ===")
                    print(f"Nama: {item.name}")
                    print(f"Harga: {item.price}")
                    print(f"Stok: {item.quantity}")
            else:
                    print("Barang tidak ditemukan.")

        elif choice == "6":
            total = service.calculate_total_stock()
            print(f"Total stok semua barang: {total}")

        elif choice == "0":
            print("Keluar dari program...")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()