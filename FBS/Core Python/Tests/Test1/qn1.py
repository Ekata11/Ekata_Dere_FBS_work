length = int(input("Enter the length :"))
breadth = int(input("Enter the breadth :"))
radius = int(input("Enter the radius :"))

area_of_rect = length * breadth
area_of_half_circle = (3.14 * radius * radius) / 2
area_of_fig = (area_of_rect) + (area_of_half_circle)
peri_of_rect = 2 * (length + breadth)
peri_of_half_circle = ( 3.14 * radius) 
peri_of_fig = peri_of_rect + peri_of_half_circle
                                                        
print(f'Area of given figure is {area_of_fig} ')
print(f'Perimeter of given figure is {peri_of_fig} ')
