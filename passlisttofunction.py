
# def count(lst):
#     even = 0
#     odd = 0
#     for i in lst:
#         if i % 2 == 0:
#             even+=1
#         else:
#             odd+=1
#     return even,odd




# lst = [20,25,14,19,16,24,28,47,26]

# even,odd = count(lst)
# print(even)
# print(odd)
# print("Even : {} and Odd : {}".format(even,odd))
# def count(lst):
def count(lst):
    cnt = 0
    for i in lst:
        if len(i) > 5:
            cnt+=1
    return cnt


lst = []
for i in range(10):
    name = input("enter name")
    lst.append(name)

total = count(lst)
print("total number of names having more than 5 characters in their name :", total)