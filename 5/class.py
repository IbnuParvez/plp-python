class Book:
  def __init__(self, buyer, author, publisher):
    self.buyer = buyer
    self.author = author
    self.publisher = publisher

  #method
  def buy(self):
    print(f"{self.buyer} is buying a book written by {self.author} published by {self.publisher}")

myBook = Book("Abubakr", "J.Rowling", "Harry Ltd")

myBook.buy()

#inheritance part boss

class Ebook(Book):
  def __init__(self, buyer, author, publisher, price):
    super().__init__(buyer, author, publisher,)
    self.price = price
    
  def describe(self):
    print(f"{self.buyer} is buying a book written by {self.author} published by {self.publisher} whose price is {self.price}")

myEbook = Ebook("Harry", "Rick Riordan", "UNlimited" ,"$50")
myEbook.buy()
myEbook.describe() 