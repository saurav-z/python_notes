# add=lambda a,b: a+b
# print(add(2,3))

# multiply=lambda a,b,c: a*b*c
# print(multiply(2,3,4))

# hello=lambda :print("Hello World")
# hello()

sub_string=lambda string: string in "Welcome to python function tutorial"
print(sub_string(input("Enter a string: ")))

add=lambda *args : sum(args)
print(add(2,3,23,213,231321))