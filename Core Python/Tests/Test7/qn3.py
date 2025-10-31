#.generate li of odd no from 1-50 using li comp and filters out the even

odd_numbers=[x for x in range(1,51) if x%2 !=0 ]
print("Odd Numbers(1-50): ", odd_numbers)