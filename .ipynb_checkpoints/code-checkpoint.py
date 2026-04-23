x = int(input("Enter a number : "))
c = 0
i = 1
while i <= x/2:
    if x%i == 0:
        c = c+1
    i = i +1
if c == 1:
    print("prime")
else:
    print("composite")