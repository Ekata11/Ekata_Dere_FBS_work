## fencing the field with barbed wire

radius = input("Enter radius of circle : 20m ")
length = input("Enter length of rectangle : 50m ")
breadth = input("Enter breadth of rectangle : 40m ")

area_of_rect = 50 * 40
area_of_half_circle = (3.14 * 20 * 20) / 2

area_of_field = (area_of_rect) + (area_of_half_circle)
print(f"The area of field is : {area_of_field}")

cost_of_wire = 35

total_cost = (cost_of_wire) * 5 * (area_of_field)
print(f"Total cost of fencing the field is : {total_cost}")
    