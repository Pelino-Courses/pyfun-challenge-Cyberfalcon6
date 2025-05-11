from product import Product
#trying to demonstrate how this inventory management system works
#note that the system is product centric i.e it manages inventory at product level
if __name__ == "__main__":
    inventory = []
    try:
        product = Product("Laptop", 1200.50, 10)
        inventory.append(product)
        print(product.display_info())

        product.add_inventory(5)
        print("After adding inventory:", product.display_info())

        product.remove_inventory(3)
        print("After removing inventory:", product.display_info())

        print("Total value of inventory:", product.total_value())
    except Exception as e:
        print(f"Error: {e}")