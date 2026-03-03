import unittest
from src.models.item import Item


class TestItem(unittest.TestCase):

    def test_item_valid(self):
        """Test membuat item dengan data valid"""
        item = Item("Laptop", 5, 7000000)
        self.assertEqual(item.name, "Laptop")
        self.assertEqual(item.quantity, 5)
        self.assertEqual(item.price, 7000000)

    def test_total_value(self):
        """Test perhitungan total nilai"""
        item = Item("Mouse", 3, 100000)
        self.assertEqual(item.total_value(), 300000)

    def test_name_kosong(self):
        """Test jika nama kosong"""
        with self.assertRaises(ValueError):
            Item("", 5, 100000)

    def test_quantity_negatif(self):
        """Test jika quantity negatif"""
        with self.assertRaises(ValueError):
            Item("Keyboard", -1, 200000)

    def test_price_negatif(self):
        """Test jika price negatif"""
        with self.assertRaises(ValueError):
            Item("Monitor", 2, -500000)


if __name__ == "__main__":
    unittest.main()