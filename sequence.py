#sequence.py
n = int(input("Enter the length of the sequence: ")) # Do not change this line
count_number = 1
num1 = 1
num2 = 2
num3 = 3
while  count_number <= n:
    summa = num1+num2+num3
    print(summa)
    count_number += 1

    num1=num2
    num2=num3
    num3=summa
