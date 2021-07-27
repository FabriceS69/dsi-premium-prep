set1 = {1,2,3}
set2 = {2,3,4}

# print(set1.union(set2) == set2.union(set1))
# print(set1.intersection(set2) == set2.intersection(set1))

a, b, c = True, False, True

# print((a or b) == (b or a))
# print((a and b) == (b and a))



set1 = {1,2,3}
set2 = {2,3,4}
set3 = {1,4,6}

print((set1.union(set2)).union(set3) == (set3.union(set2)).union(set1))
print((set1.intersection(set2)).intersection(set3) == (set3.intersection(set2)).intersection(set1))