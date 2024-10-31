x = int (input("Enter the number of rows:"))
#Initialize num
num = 1
# For Loops
for row in range (1, x + 1):
    for col in range (1, row + 1):
        print (num, end= " ")
        num += 1
    print()