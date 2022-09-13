#합집합
A = {"apple", "banana", "grape"}
B = {"apple", "banana", "kiwi"}

print(A | B)
print(A.union(B))


#교집합

print(A & B)
print(A.intersection(B))

#차집합

print(A - B)
print(A.difference(B))