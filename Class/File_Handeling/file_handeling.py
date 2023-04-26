####Reading

# f=open(r'G:\Python\File_Handeling\abc.txt','r') #File Location

# # print(f.read())                 #Read Whole File
# # print(f.readline())             #Read Line by Line
# # print(f.readline())
# # print(f.readlines())            #Reads All Lines

# lines=f.readlines()
# for line in lines:
#     print(line)

# ####Writing

# f=open(r'G:\\Python\File_Handeling\text.txt','w')  #Creates File if not exist
# f.write('Hello World!')

####Append

# f=open(r'G:\\Python\File_Handeling\text.txt','a')  #Creates File if not exist
# f.write('Hello World!\n')

# f.close()

#IF with used FIle will automatically be closed after execution

with open('abc.txt','r') as f:
	print(f.read())
print(f.read())



#Open a file in read mode in such a way it automatically closes.
#Write Hello world and Hello Deerwalk in 2 lines usinf f.write once. again open same file in readmode and read all the file content in list. and read all content from list 

