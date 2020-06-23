def fact(n):
    val = 1
    for i in range(1,n+1):
        val = val * i
    print("factorial of ",n ,"is ",val)

fact(int(input("entre number :")))
