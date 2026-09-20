


class StockItem:
  def __init__(self,name, amount):
   self.name = name
   self.amount = amount


class Stock:
  def __init__(self):
    self.items = []
  def add_product(self, product):
    self.items.append(product)

  def take_a_product(self, product, amount):
      print("Produkt:", product) # Felsökning då jag fick problem med koden
      print("Items:", self.items)
      print("Finns produkten?", product in self.items)

      if product in self.items:
         product.amount -= amount
