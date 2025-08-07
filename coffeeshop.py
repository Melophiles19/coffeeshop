class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Order:
     def __init__(self):
        self.items = []
     def add_item(self, coffee):
         self.items.append(coffee)
         print(f"Added {coffee.name} to your order.")
     def total(self):
         return sum(item.price for item in self.items)
     def show_order(self):
        if not self.items:
            print("no items in order")
            return
        print("\n your order:")
        for i ,item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price}")
        print(f"total: ${self.total()}\n")
     def checkout(self):
         if not self.items:
             print("your cart is empty")
             return
         self.show_order()
         confirm = input("proceed to checkout? (yes/no): ").strip().lower()
         if confirm == 'yes':
             print("order confirmed! thanks you.")
             self.items.clear()
             
         else:
             print("checkout cancelled.")
def main():
    menu = [
        Coffee("espresso",2.5),
        Coffee("latte",3.5),
        Coffee("cappuccino",3.0),
        Coffee("americano",3.0)
    ]    
    order = Order()
    while True:
        print("\n---coffee menu ---")
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} -${coffee.price}")
        print("5. view order")
        print("6. checkout")
        print("7. exit")
        choise = input("choose an option: ")
        if choise in ['1', '2', '3', '4']:
            order.add_item(menu[int(choise) - 1])
        elif choise == '5':
            order.show_order()
        elif choise == '6':
            order.checkout()
        elif choise == '7':
            print("thanks for visiting. goodbye!")
            break
        else:
            print("invalid choice. try again.")
if  __name__ == "__main__":
    main()                            