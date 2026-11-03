class Laptop:
   def __init__(self,brand,price):
        self.brand=brand
        self.price=price

   def show_info(self):
        print(f"laptop brand;{self.brand},price:${self.price}")

laptop1 = Laptop("dell",80000)
laptop2 = Laptop("HP",90000)

laptop1.show_info()
laptop2.show_info()