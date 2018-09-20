import random
colours = ["green", "red", "blue"]
dozen = ["1st","2nd","3rd"]
choice = ["number", "dozen", "colour", "other"]

total_money = 10000
bet = 0

def __init__(total_money):

        #sets 2 variables that will store the results of each outcome (colour, number etc)
        global result_number
        global result_colour

        #generates the results to each outcome
        result_colour = random.choice(colours)
        result_number = random.randint(0, 36)

        #sets the total money to the outcome of new money(the )
        total_money = place_bet(total_money)

def place_bet(new_money):
    bet = int(input("how much money do you want to bet"))

    #if you are betting more money than you have
    if bet > new_money:
        print("invalid")
        #user re-enters their bet amount until it is valid
        while bet > new_money:
            bet = int(input("how much money do you want to bet"))

    #user chooses what outcome they would like to bet on
    choice = input("what choice do you want to make (choose from: number, dozen, colour or other)")
    choice = choice.lower()

    #stores the new money as the result of the game
    new_money = get_result(choice, new_money, bet)
    return new_money

def get_result(choice, totalMoney, bet):
    if choice == "number":
           print(result_number)
           input_number = int(input("choose a number"))
           if input_number == result_number:
               print("you won")
               totalMoney += bet
               print("your total money is", totalMoney)
               return total_money
           else:
               print("you lost, unlucky")
               totalMoney -= bet
               print("your total money is:", totalMoney)
    elif choice == "colour":
        print(result_colour)
    else:
        print("test")
    __init__(total_money)

__init__(total_money)
