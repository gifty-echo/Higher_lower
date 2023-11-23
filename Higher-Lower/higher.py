from art import logo, vs
from game_data import data
import random


def formatted_data(account):
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name},a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_continue = True
account_b = random.choice(data)
# guess = input("Who has more followers? Type A or B: ").lower()


while game_continue:

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A :{formatted_data(account_a)}")
    print(vs)
    print(f"Against B :{formatted_data(account_b)}")
    guess = input("Who has more followers? Type A or B: ").lower()

    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']

    is_correct = check_answer(guess=guess, a_followers=a_followers, b_followers=b_followers)
    # Score keeping
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
