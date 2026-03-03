class InventoryService:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_all_items(self):
        return self.items