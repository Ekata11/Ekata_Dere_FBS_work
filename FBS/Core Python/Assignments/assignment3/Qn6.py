## to calculate profit or loss

cost_price = int(input("Enter cost price : "))
selling_price = int(input("Enter selling price : ")) 

profit = selling_price - cost_price
loss = cost_price - selling_price


if(selling_price > cost_price):
    print(f'Profit is : {profit} ')
elif(selling_price < cost_price):
    print(f'Loss is : {loss}')