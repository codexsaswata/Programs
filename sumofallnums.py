def sum_natural(n):
    sum = 0
    i=1
    while(i<=n):
        sum=sum+i
        i=i+1
    return sum
n = int(input("Enter a number: "))
print(sum_natural(n))