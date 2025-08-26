area_of_one_wall = int(input("Enter area of one wall : "))
cost_of_interior = int(input("Enter cost of painting interior per sq.m: "))
cost_of_exterior = int(input("Enter cost of painting exterior per sq.m: "))

total_area = 2 * 4 * area_of_one_wall

interior_cost = total_area * cost_of_interior
exterior_cost = total_area * cost_of_exterior

print(f'Total interior cost of painting is {interior_cost} per sq.m')
print(f'Total exterior cost of painting is {exterior_cost} per sq.m')