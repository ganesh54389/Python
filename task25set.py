#--------------------------set intersection--------------------------
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set_intersection=set1.intersection(set2)
print(set_intersection)
#-----------------------set union--------------------------------------
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set_union=set1.union(set2)
print(set_union)
#---------------------------set difference-------------------------
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
dif=set1.difference(set2)
print(dif)
#-------------------------symmetric differnece --------------------
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
sym_dif=set1.symmetric_difference(set2)
print(sym_dif)
#--------------------------set membership_------------------------
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(5 in set1)