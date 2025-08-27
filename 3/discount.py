#part 1
def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
      final_price = price - (price * discount_percent / 100)
      return final_price
    else:
       return price

#part 2    
price = float(input("What is the price? "))
discount_percent = float(input("What is the discount? "))

final_price = calculate_discount(price, discount_percent)

print("Final price is: " ,final_price)