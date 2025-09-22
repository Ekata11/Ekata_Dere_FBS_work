# accept no from user and check if this ele is present in list or not .also tell how many time it present in list


def check_number(li,num):
    count = 0
    for i in li:
        if i == num:
            count+=1
    if count>0:
        print(num, "is present", count, "times")
    else:
        print(num, "is not present")        
        
li = [0,10,20,30,40,50,40,40] 
num = int(input("Enter a number : "))   
check_number(li,num)