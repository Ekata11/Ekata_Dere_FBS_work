## 18%GSt  . 

p1 = int(input("Enter price of product 1 : "))
p2 = int(input("Enter price of product 2 : "))
p3 = int(input("Enter price of product 3 : "))
p4 = int(input("Enter price of product 4 : "))
p5 = int(input("Enter price of product 5 : "))

total = p1 + p2 + p3 + p4 + p5
GST = total * (18/100)
total_bill = total + GST           

print(f'Total bill without GST = Rs. {total}')
print(f'Total bill with GST = Rs. {GST}')
print(f'Total bill after adding GST = Rs. {total_bill}')