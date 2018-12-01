n, m = int(input("enter input:").split())

sc_ar =int(input("enter input").split())

A = set(int(input("enter input:").split()))
B = set(int(input("enter input:").split()))
print(sum([(i in A) - (i in B) for i in sc_ar]))