#test2 Mora game

a = int(input("Please A enter 0-2: "))
b = int(input("Please B enter 0-2: "))
C = a-b
hand=['Stone','Paper','Scissors']
if C == -2 or C == 1:
    print("A is ",hand[a],",B is ",hand[b],",A is winner")
elif C == -1 or C == 2:
    print("A is ",hand[a],",B is ",hand[b],",B is winner")
elif C == 0:
    print("try again")
else:
    print("Error")
