## age of 5 people and per person ticket amount and calculate total amt to ticket to travel.

total = 0
ticket = int(input("Enter ticket amount per person:"))

for i in range(5):
    age = int(input(f"Enter age of person {i+1}:"))
    if age < 12:
        total += ticket * 0.7
    elif age> 59:
        total += ticket * 0.5
    else:
        total += ticket
print("Total tcicket amount", total)


