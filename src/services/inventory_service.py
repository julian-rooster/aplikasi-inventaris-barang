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
        return None