import random
colours = ["green", "red", "blue"]
dozen = ["1st","2nd","3rd"]
choice = ["number", "dozen", "colour", "other"]

total_money = 10000
bet = 0




def __init__(total_money):
    while 0 == 0:
        global result_number
        global result_colour
        result_colour = random.choice(colours)
        result_number = random.randint(0, 36)
        total_money = place_bet(total_money)

def place_bet(new_money):
    bet = int(input("how much money do you want to bet"))
    if bet > new_money:
        print("invalid")
        while bet > new_money:
            bet = int(input("how much money do you want to bet"))
    choice = input("what choice do you want to make (choose from: number, dozen, colour or other)")
    choice = choice.lower()
    new_money = get_result(choice, new_money, bet)
    return new_money

def get_result(choice, totalMoney, bet):
    if choice == "number":
        print(result_number)
        input_number = int(input("choose a number"))
        if input_number == result_number:
            print("you won")
            total_money = totalMoney + bet
            print("your total money is", total_money)
            return total_money
        else:
            print("you lost, unlucky")
            total_money = totalMoney - bet
            print("your total money is:", total_money)
    elif choice == "colour":
        print(result_colour)
    else:
        print("test")
    __init__()

__init__(total_money)
