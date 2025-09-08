## accept int amt and tell min notes 

amt = int(input("Enter Amount : "))
notes = [2000,1000,500,200,100,50,20,10,5,2,1]

for n in notes:
    if amt >= n:
        count = amt // n
        print(n, 'x' , count)
        