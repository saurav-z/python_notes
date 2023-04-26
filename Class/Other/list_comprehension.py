a=[1,2,3,4,5,6,7,8]
b=[]
for n in a:
    if n % 2 == 0:
        b.append(n)
print(b)



# List Comprehension
even=[x for x in a if x%2==0]
print(even)