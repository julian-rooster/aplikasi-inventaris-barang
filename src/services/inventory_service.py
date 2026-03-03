class InventoryService:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_all_items(self):
        return self.items

    def delete_item(self, name):
        self.items = [item for item in self.items if item.name != name]

    def find_item(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None  # kalau tidak ditemukan

    def calculate_total_stock(self):
        total = 0
        for item in self.items:
            total += item.quantity
        return total
    
    def update_item(self, name, new_quantity, new_price):
        item = self.find_item(name)
        if item:
            item.quantity = new_quantity
            item.price = new_price
            return True
        return False