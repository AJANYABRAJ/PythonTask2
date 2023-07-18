# 1.Unique and Duplcate

a=[1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
u=[]
d=[]
for i in a:
    if i not in u:
        u.append(i)
    elif i not in d:
        d.append(i)
print("Duplicate",d)
print("Unique",u)

################################################
# 2. Check entered no

# a=int(input("enter the number"))
# if a>=100 and a<=700 or a>=700 and a<=900:
#     print("Number is between 100 and 900")
# else:
#     print("Number is not in the range")

################################################
# 3.Sum of 3 nos

# a=int(input("enter first no"))
# b=int(input("enter second no"))
# c=int(input("enter third no"))
# s=a+b+c
# print("sum of 3 nos is",s)
# if a==b==c:
#     s=s*3
#     print("sum",s)

################################################
# 4.Count

# a=[1,2,3,4,5,6,4,7,3,4]
# b=4
# count=0
# for i in a:
#     if i==b:
#         count=count+1
# print(count,"times 4 occuring")

################################################
# 5.Vowels

# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# s=input("enter a letter")
# for vowel in s:
#     if vowel in vowels:
#         print("It is a vowel")
#     else:
#         print("it is not vowel")

################################################
# 6. Filename

# fname= input("Enter Filename: ")
# f = fname.split(".")
# print ("Extension of the file is : " + f[-1])