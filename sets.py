#Sets
 
my_set = set()

print(type(my_set))

items = {"apple","banana","orange","banana"}

print(items)

items.add("orange")
items.add("grapes")
items.discard("orange")
items.discard("kiwi")

#___.discard doesn't throw an error when there isn't the data to remove, unlike ___.remove

print(items)

number_set_1 = {12,34,56,78,90,35}
number_set_2 = {13,24,35,46,57,68,79,80,90}


#Set Operations

# 1) Union
# 2) Intersection
# 3) Difference
# 4) Symmetric Difference

# union offsets
# number_set_1 U number_set_2 = {12,34,56,78,90,35,13,24,46,57,68,79,80}

print(number_set_1.union(number_set_2))

# Intersection
# {35,90}

print(number_set_1.intersection(number_set_2))

# Difference
# {56, 34, 12, 78}

print(number_set_1.difference(number_set_2))

# Symmetric Difference
# Symmetric difference is (union of sets - intersection of sets)

print(number_set_1.symmetric_difference(number_set_2))