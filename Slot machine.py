import random


MAX_LINES=3
MIN_LINES=1
MAX_BET=100
MIN_BET=1

ROWS = 3
COLS = 3

symbol_count={
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value={
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_wins(columns,lines,bet,values):
    winnings = 0
    win_lines = []
    for line in range(lines):
        symbols = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbols != symbol_to_check:
                break
        else:
            winnings+= values[symbols] * bet
            win_lines.append(lines + 1)

    return winnings, win_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbols,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbols)

    columns = []
    for _ in range(cols):
        column=[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns    

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end=" | ")
            else:
                print(column[row],end=" | ")
        
        print()
    

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount >0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Enter a digit next time.")
    return amount

def get_lines():
    while True:
        lines = input(f"With how many lines you want to play (1 - {MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES<= lines <=MAX_LINES:
                break
            else:
                print(f"Lines must be between {MIN_LINES} - {MAX_LINES}")
        else:
            print("Enter a digit next time .")
    return lines


def get_bet():
    while True:
        amount = input("How much you want to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <=MAX_BET:
                break
            else:
                print(f"Bet must be betwwen ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter a valid number.")
    return amount

def main():
    balance = deposit()
    while True:
        lines = get_lines()
        bet = get_bet()
        total_bet = bet*lines

        if total_bet > balance:
            print(f"You do not have enough balance to bet the amount. Your total balance is ${balance}")
        else:
            print(f"You are betting ${bet} on {lines} lines. Your total betting amount is ${total_bet}")
            slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
            print_slot_machine(slots)
            winnings, win_lines = check_wins(slots,lines,bet,symbol_value)
            if win_lines:
                print(f"\033[92mYou won ${winnings}\033[0m")
                print(f"You won on line ", *win_lines)
            else:
                print("\033[91mYou didn't win on any lines. \033[0m")
            balance -= total_bet
            print(f"\033[96mRemaing balance is ${balance}\033[0m")

            if balance ==0:
                print("\033[91You RAN OUT of MONEY.\033[0m")
                break

            play_again = input("Do you want to play AGAIN (\033[92my\033[0m/\033[91mn\033[0m)? ").lower()
            if play_again != "y":
                break
     
main()
