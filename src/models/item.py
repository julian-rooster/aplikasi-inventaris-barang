class Item:
    def __init__(self, name, quantity, price):

        # Validasi name
        if not name or not isinstance(name, str):
            raise ValueError("Nama barang harus berupa teks dan tidak boleh kosong")

        # Validasi quantity
        if not isinstance(quantity, int):
            raise TypeError("Quantity harus berupa angka bulat")
        if quantity < 0:
            raise ValueError("Quantity tidak boleh negatif")

        # Validasi price
        if not isinstance(price, (int, float)):
            raise TypeError("Price harus berupa angka")
        if price < 0:
            raise ValueError("Price tidak boleh negatif")

        self.name = name
        self.quantity = quantity
        self.price = price