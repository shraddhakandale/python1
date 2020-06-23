#f1 = open('mydata','r')
# print(f1.readline(),end="")
# print(f1.readline())
#for data in f1:
 #   print(data)


# f1 = open('mydata2','w')
# f1.write("hello")
# f1 = open('mydata2','a')
# f1.write("hi")

f2 = open('image.jpg','rb')
f3 = open('image2.jpg','wb')
for data in f2:
    f3.write(data)



