from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

# Disk 3 is larger than Disk 1
for disk in range(num_disks,0,-1):
    left_stack.push(disk)

#For towers of hanoi, the number of optimal moves is always 2Number of Disks - 1.
num_optional_moves = 2 ** num_disks - 1
print(f"\nThe fastest you can solve this game is in {num_optional_moves} moves")

#Get User Input

        
#Play the Game