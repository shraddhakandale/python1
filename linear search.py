
pos = -1
def search(list,key):
    for i in range(len(list)):
        if list[i]==key:
            globals()['pos']=i
            return True
    return False




n = int(input("enter size"))
list = []
for i in range(n):
    list.append(int(input("enter value")))
key = int(input("enter element to search"))

if search(list,key):
    print("Found at position :",pos+1)
else:
    print("May be the required element is not in the list")