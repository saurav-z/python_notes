mytuple=("apple","ball","cat")  #it is unchangeable

print(type(mytuple))

print(len(mytuple))


if "apple" in mytuple:
    print('yes')

y=list(mytuple)
y.append("dog")
mytuple=tuple(y)


