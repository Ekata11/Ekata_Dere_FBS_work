## selling price of book based on cost and discount

c_p = int(input("Enter cost price : "))
discount = int(input("Enter discount : "))

s_p = c_p - (discount*c_p/100)

print(f'Selling Price is : Rs. {s_p}')