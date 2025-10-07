
def my_range(start,stop,step=1):
    while start < stop:
        yield start
        start+=step
print(list(my_range(2,20,3)))       