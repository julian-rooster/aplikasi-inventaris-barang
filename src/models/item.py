class Item:
    def __init__(self, name, quantity, price):

        if not name or not isinstance(name, str):
            raise ValueError("Nama barang harus berupa teks dan tidak boleh kosong")

        if not isinstance(quantity, int):
            raise TypeError("Quantity harus berupa angka bulat")
        if quantity < 0:
            raise ValueError("Quantity tidak boleh negatif")

        if not isinstance(price, (int, float)):
            raise TypeError("Price harus berupa angka")
        if price < 0:
            raise ValueError("Price tidak boleh negatif")

        self.name = name
        self.quantity = quantity
        self.price = price

    def total_value(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.name} | Stok: {self.quantity} | Harga: {self.price}"