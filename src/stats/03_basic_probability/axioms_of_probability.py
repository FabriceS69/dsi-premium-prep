set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2) == set2.union(set1))
print(set1.intersection(set2) == set2.intersection(set1))