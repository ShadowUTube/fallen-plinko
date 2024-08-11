import streamlit as st
import random

total = []
lost_list = []
gained_back = []
st.title("Fallen Plinko Testing")
st.write("*To start fill out the imformation, and click rerun button*")
st.write("Respond with how many caps you want to bet on each option")

two = st.number_input("2x:", step=1)
three = st.number_input("3x:", step=1)
five = st.number_input("5x:", step=1)
ten = st.number_input("10x:", step=1)

iterations = st.number_input("How many times of the plinko board running do you want to simulate?", step=1)

input_total = two + three + five + ten
total_spent = input_total*iterations

def choose_option():
    options = [2, 3, 5, 10]
    probabilities = [3/8, 2/8, 2/8, 1/8]
    
    return random.choices(options, probabilities)[0]

for x in range(1, iterations + 1):  # Notice that I changed `iterations` to `iterations + 1` to include the last iteration.
    choice = choose_option()
    if choice == 2:
        multiplied = two
        gained_back.append(two)
    elif choice == 3:
        multiplied = three
        gained_back.append(three)
    elif choice == 5:
        multiplied = five
        gained_back.append(five)
    elif choice == 10:
        multiplied = ten
        gained_back.append(ten)

    amount = choice * multiplied
    lost = input_total - multiplied

    lost_list.append(lost)
    total.append(amount)

spent = total_spent -  sum(gained_back)

profit = (sum(total) - sum(lost_list)) - spent

def get_data():
    st.write("You made a total of " + str(sum(total)) + " caps!")
    st.write("You lost a total of " + str(sum(lost_list) + gained_back) + " caps!")

    st.write("Your total profit was " + str(profit) + " caps!")

if st.button("Rerun"):
    get_data()
