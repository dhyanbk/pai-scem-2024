num=int(input("Enter number: "))
count=0
i = num
# count the digits
while(i>0):
    count=count+1
    i=i//10
print(f"The number of digits in {num}:",count)