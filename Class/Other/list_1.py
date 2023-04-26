# from subprocess import list2cmdline


# list=["Banana","Apple","Cat"]

# list.sort()
# #reverse alphabetically
# print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse()
# #reverse index values
# print(list)

# list.remove("Banana")
# print(list)

# del list[1]
# print(list)
# list.clear()















# list_1=[1,2,3,4]

# #.copy makes different copy of list1 otherwise both list would have same value
# list_2=list_1.copy()
# list_2[0]=4
# print(list_1,list_2)

# list_3=list_1+list_2
# print(list_3)

# #print from 0-9
list_of_number=list(range(10))
print(list_of_number)

#convert string to character list
_string="Hello World"
character_list=list(_string)
print(character_list)

#split string and make list
splitted_string=_string.split(" ")
print(splitted_string)
print(_string)

joined_list="".join(character_list)
print(joined_list)