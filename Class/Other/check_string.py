# txt="The best thing in life are free!"
# print("free" in txt)
# print('Neshan' in txt)

# #print(variable[index])
# print(txt[1])
# #sliceing
# print(txt[2:8])

# print(txt[:9])

# print(txt[4:])

# print(txt[-5:6])



# Write a function that takes a string and returns the first vowel from that string.

# def vowel(str):
#     for v in str:
#         if v=='a'or v=='e' or v=='i' or v=='o' or v=='u':
#             print(v)
#             break
# vowel('Hello')

# Write a function that takes a string and returns no of vowel from that string.



# def vowel(str):
#     i=0
#     for v in str:
#         if v=='a'or v=='e' or v=='i' or v=='o' or v=='u':
#             i=i+1
#     return i        
# print(vowel('Hello'))



# s='umesh'
# b=[]
# for a in s:
#     if a in 'aeiou':
#         b.append(a)
# print(b)


s='umesh'
l=[x for x in s if x in 'aeiou']
print(l)
