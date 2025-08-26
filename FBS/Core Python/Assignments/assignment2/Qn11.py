## accept amt and tell min no of notes for that amt.

notes = [2000,500,200,100,50,20,10,5]

amount=int(input("Enter the amount: "))
n2000 = amount // 2000
amount = amount % 2000

n500 = amount // 500
amount = amount % 500

n200 = amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10

n5 = amount // 5
amount = amount % 5

n2 = amount // 2
amount = amount % 2

n1 = amount // 1
amount = amount % 1

print(f'Minimum number of notes required-2000:{n2000},500:{n500},200:{n200},100:{n100},50:{n50},20:{n20},10:{n10},5:{n5},2:{n2},1:{n1}')

