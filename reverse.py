def reverse_number(n):
    if(n<9 and n>0):
        return n
    rev = 0
    while(n>0):
        rev = rev*10
        rev = rev + (n%10)
        n=n//10
    return rev
x = int(input("Enter a no: "))
print("reverse is: ",reverse_number(x))
