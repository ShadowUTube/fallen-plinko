import random
total = []
lost_list = []
print("Respond with how many caps you want to bet on each option ")

two = int(input("\n2x: "))
three = int(input("3x: "))
five = int(input("5x: "))
ten = int(input("10x: "))

iterations = int(input("\nHow many times of the plinko board running you want to simulate? "))
print("\n")

input_total = two + three + five + ten

def choose_option():
    options = [2, 3, 5, 10]
    probabilities = [3/8, 2/8, 2/8, 1/8]
    
    return random.choices(options, probabilities)[0]

for x in range(1, iterations):
    choice = choose_option()
    if choice == 2:
        multiplied = two
        lost = input_total - two
    elif choice == 3:
        multiplied = three
        lost = input_total - three
    elif choice == 5:
        multiplied = five
        lost = input_total - five
    elif choice == choice == 10:
        multiplied = ten
        lost = input_total - ten
    amount = choice * multiplied

    lost_list.append(lost)
    total.append(amount)

profit = sum(total) - sum(lost_list)
print("\n")
print("\n")
print("\n")
print("You made a total of " + str(sum(total)) + " caps!")
print("You lost a total of " + str(sum(lost_list)) + " caps!")
print("\n")
print("Your total profit was " + str(profit) + " caps!")
print("\n")
