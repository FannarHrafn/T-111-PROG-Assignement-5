#Assignment 5
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
#while loop to add user numbers to list as long as they're not negative
num_list = []
while num_int >= 0:
    num_list.append(num_int)
    num_int = int(input(" Input a number:"))
#find biggest number in list and print it
max_int = max(num_list)
print(" The maximum is", max_int)    # Do not change this line