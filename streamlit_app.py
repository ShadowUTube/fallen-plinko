import streamlit as st
import random

total_profit = 0
st.title("Fallen Plinko Testing")
st.write("*To start, fill out the information, and click the rerun button*")
st.write("Respond with how many caps you want to bet on each option")

two = st.number_input("2x:", step=1)
three = st.number_input("3x:", step=1)
five = st.number_input("5x:", step=1)
ten = st.number_input("10x:", step=1)

iterations = st.number_input("How many times of the plinko board running do you want to simulate?", step=1)

def choose_option():
    options = [2, 3, 5, 10]
    probabilities = [3/8, 2/8, 2/8, 1/8]
    
    return random.choices(options, probabilities)[0]

for x in range(1, iterations + 1):
    choice = choose_option()
    if choice == 2:
        bet = two
    elif choice == 3:
        bet = three
    elif choice == 5:
        bet = five
    elif choice == 10:
        bet = ten

    winnings = choice * bet
    profit = winnings - bet  # Calculate profit for this round
    total_profit += profit

def get_data():
    st.write("You made a total profit of " + str(total_profit) + " caps!")

if st.button("Rerun"):
    get_data()
