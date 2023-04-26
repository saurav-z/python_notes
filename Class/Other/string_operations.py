from re import A


a="  Neshan , Meshan"
print(a.upper())

#Remove whitespace

print(a.strip())

print(a.replace("N","M"))

data=(a.split(","))

print(data)


#Escape Character
txt="Hello guys how are you \"Hacke\" is my name"
print(txt)

#new line
a="Hello This is \n Line Break"
print(a)

#TAB SPACE
a="Hello This is \t TAB"
print(a)



#Booleans
print(10>9)
print(1==2)
print(10>8)


x="Hello"
y=16
print(x,bool(x))
print(bool(y))



#check datatype
d=1
e=A
print(isinstance(d,int))

print(isinstance(d,str))