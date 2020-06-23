lst = [1,2,3,4]
# print(lst[7])
for i in lst:
    print(i)

print('**********************************')
it = iter(lst)
print(it.__next__())
print('**********************************')

print(next(it))
print('**********************************')