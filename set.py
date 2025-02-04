

#-----------------------------sets----------------------------------------

my_set={1,2,3}
print(my_set)
another_set=set()
print(type(another_set))
my_set={1,"ramana",3}
my_set.add("vasu")
my_set.remove("vasu")
my_set.discard("8")
print(my_set)
set_01={1,2,3}
set02={3,4,5}
union_of_sets=set_01.union(set02)
intersection_of_sets=set_01.intersection(set02)
difference_of_two_sets=set_01.difference(set02)
symmetric_difference_of_twosets=set_01.symmetric_difference(set02)
result=set_01.isdisjoint(set02)
print(union_of_sets)
print(intersection_of_sets)
print(difference_of_two_sets)
print(symmetric_difference_of_twosets)
print(result)
set_01={1,2,3}
set_02={1,2,3,4}
subset=set_01.issubset(set_02)
print(subset)
super_set=set_02.issuperset(set_01)
print(super_set)


