pos = -1


def search(list, key):
    low = 0
    up = len(list) - 1
    while low <= up:
        mid = (low + up) // 2
        if list[mid] == key:
            globals()['pos'] = mid
            return True
        elif list[mid] < key:
            low = mid+1
        else:
            up = mid-1
    return False          # if element is not fouund

list = []
n = int(input("enter the size"))
for i in range(n):
    list.append(int(input("enter sorted values either increasing or decreasing order")))
key = int(input("enter the number that you want to search :"))

if search(list, key):
    print("found at position :", pos + 1)
else:
    print("may be the value is not in the list")
