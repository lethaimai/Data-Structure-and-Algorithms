from stack import Stack


####### Create the stacks #######
stacks = []

lef_stack = Stack("Left")
stacks.append(lef_stack)

middle_stack = Stack("Middle")
stacks.append(middle_stack)

right_stack = Stack("Right")
stacks.append(right_stack)

####### Set up the Game #######
num_disks = int(input("""Let's play Towers of Hanoi!!\n
        \nHow many disks do you want to play with?\n"""))

while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))
    if num_disks >= 3:
        break

for disk in range(num_disks, 0, -1):
    lef_stack.push(disk)

num_optimal_moves = 2**num_disks - 1
print("\nThe fastest you can solve this game is in {optimal_moves} moves".format(
    optimal_moves=num_optimal_moves))

####### Get User Input #######


def get_input():
    choices = [stacks_item.get_name()[0] for stacks_item in stacks]
    print(choices)
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {letter} for {stack_name}".format(
                letter=letter, stack_name=name))

        user_input = input()

        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]


####### Play the Game ########
num_user_moves = 0
while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...")
    for stacks_item in stacks:
        stacks_item.print_items()
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()
        if from_stack.is_empty():
            print("\n\nInvalid Move. Try Again")
        elif (to_stack.is_empty()) or (from_stack.peek() < to_stack.peek()):
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again")

print(
    "\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))
    
