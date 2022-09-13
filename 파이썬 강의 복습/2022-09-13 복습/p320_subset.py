# 부분집합
A = {"apple", "banana", "grape"}
B = {"apple", "banana", "grape", "kiwi"}

if A < B:                               
    print("A는 B의 부분 집합입니다.")

if A.issubset(B):
    print("A는 B의 부분 집합입니다.")