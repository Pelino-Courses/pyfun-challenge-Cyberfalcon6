class Product:
    def __init__(self, name, price, quantity):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_inventory(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount to add must be a positive integer.")
        self.quantity += amount

    def remove_inventory(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount to remove must be a positive integer.")
        if amount > self.quantity:
            raise ValueError("Cannot remove more than available inventory.")
        self.quantity -= amount

    def total_value(self):
        return self.price * self.quantity

    def display_info(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Total Value: {self.total_value()}"