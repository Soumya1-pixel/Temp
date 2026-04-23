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
-----------------------------------------
x = [10,20,30,20,10,40]
y = []
for i in x:
    if i not in y:
        y.append(i)
print(y)
---------------------------------------
row = 5
for i in range(1,row+1):
    print("*" * i)