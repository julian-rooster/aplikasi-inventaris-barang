# src/utils/helper.py

def validate_number(value):
    """
    Validasi input agar berupa angka positif.
    """
    if value is None or value == "":
        raise ValueError("Input tidak boleh kosong")

    try:
        number = int(value)
    except ValueError:
        raise ValueError("Input harus berupa angka")

    if number < 0:
        raise ValueError("Angka tidak boleh negatif")

    return number


def format_currency(value):
    """
    Format angka menjadi Rupiah.
    """
    return f"Rp {value:,}"


def search_items(keyword, items):
    """
    Mencari item berdasarkan keyword (case insensitive).
    items berupa list dictionary dengan key 'name'
    """
    keyword = keyword.lower()

    return [
        item for item in items
        if keyword in item["name"].lower()
    ]