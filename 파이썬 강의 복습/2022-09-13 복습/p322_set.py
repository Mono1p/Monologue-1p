list1 = [1,2,3,4,5,1,2,4]
print(len(set(list1)))                  #5


list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
print(set(list1) & set(list2))          #{3, 4, 5}