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
<<<<<<< HEAD
        return None
    
def update_item(self, item_id, new_name=None, new_quantity=None, new_price=None):
    item = self.find_item(item_id)
    if item:
        if new_name:
            item.name = new_name
        if new_quantity is not None:
            item.quantity = new_quantity
        if new_price is not None:
            item.price = new_price
        return True
    return False

def total_stock(self):
    return sum(item.quantity for item in self.items)

def total_asset_value(self):
    return sum(item.quantity * item.price for item in self.items)
=======
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
>>>>>>> 9fc4b607030a04f9d4c15fe2b5ebd2e82495b9bb
