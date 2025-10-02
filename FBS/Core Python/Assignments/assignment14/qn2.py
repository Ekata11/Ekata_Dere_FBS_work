# remove intersection of second set with a first set

def remove_intersection(s1,s2):
    return s1-(s1&s2)

print(remove_intersection({1,2,3,4},{2,4,5,6}))
    