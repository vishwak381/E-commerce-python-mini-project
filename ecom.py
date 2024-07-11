class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

inventory = [
    Product("Laptop", 1000),
    Product("Mouse", 50),
    Product("Keyboard", 80),
    Product("Monitor", 300)
]

cart = []

def display_products():
    print("Available Products:")
    for i, product in enumerate(inventory):
        print(f"{i+1}. {product.name} - ${product.price}")

def add_to_cart(product_index):
    cart.append(inventory[product_index])
    print(f"{inventory[product_index].name} added to cart.")

def calculate_total():
    total = sum(product.price for product in cart)
    return total

def checkout():
    total = calculate_total()
    print(f"Total: ${total}")

def main():
    while True:
        display_products()
        choice = input("Enter product number to add to cart (q to quit, c to checkout): ")
        if choice.lower() == 'q':
            break
        elif choice.lower() == 'c':
            checkout()
            break
        else:
            try:
                product_index = int(choice) - 1
                if 0 <= product_index < len(inventory):
                    add_to_cart(product_index)
                else:
                    print("Invalid product number.")
            except ValueError:
                print("Invalid input. Please enter a valid product number.")

if __name__ == "__main__":
    main()