import random
import msvcrt
from colorama import Fore
from os import system
title = "bingle dong"
system("title "+title)
def generate_card_number(card_bin, randomnums):
    card_suffix = ''.join(str(random.choice(randomnums)) for _ in range(6))
    card_num = card_bin + card_suffix
    return card_num
def luhn_checksum(card_num):
    digits = [int(d) for d in card_num]
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    checksum = sum(digits) % 10
    return checksum == 0
def genKey(): 
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4',
           '5', '6', '7', '8', '9']
    x = 0
    newKey = ""
    while x < 17:
        digit = random.randint(0, 34)
        if x == 5 or x == 11:
            newKey = '-'
        else:
            newKey = symbols[digit]
        x = 1
    return newKey
Logo = '''
██████╗ ██╗███╗   ██╗ ██████╗ ██╗     ███████╗    ██████╗  ██████╗ ███╗   ██╗ ██████╗ 
██╔══██╗██║████╗  ██║██╔════╝ ██║     ██╔════╝    ██╔══██╗██╔═══██╗████╗  ██║██╔════╝ 
██████╔╝██║██╔██╗ ██║██║  ███╗██║     █████╗      ██║  ██║██║   ██║██╔██╗ ██║██║  ███╗
██╔══██╗██║██║╚██╗██║██║   ██║██║     ██╔══╝      ██║  ██║██║   ██║██║╚██╗██║██║   ██║
██████╔╝██║██║ ╚████║╚██████╔╝███████╗███████╗    ██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝
╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ 
'''
print(Fore.BLUE+Logo)
print(Fore.LIGHTGREEN_EX+f"[•] Crazy skid leak by nexus#0101")
while True:
    try:
        card_type = int(
            input(Fore.MAGENTA+f"[▼] Select the type of card to generate:\n1. [■] $1k Amazon Store Card\n2. [■] $5k Amazon Store Card\n3. [■] $10k Amazon Store Card\n4. [■] $50k Amazon Store Card\n5. [■] $100k Amazon Store Card\n6. [■] Best Buy Store Card\n7. [■] Target Store Card\n8. [■]  Aged amzn acc gen\n    [►] Choose the option you want: "))
        if card_type in [1, 2, 3, 4, 5, 6, 7, 8]:
            break
        else:
            print(Fore.RED+f"Invalid option.")
    except ValueError:
        print(Fore.RED+f"Invalid option.")
if card_type == 1:
    card_amount = 1000
    card_bin = "6045781142"
elif card_type == 2:
    card_amount = 5000
    card_bin = "6045781185"
elif card_type == 3:
    card_amount = 10000
    card_bin = "6045781123"
elif card_type == 4:
    card_amount = 50000
    card_bin = "6045781143"
elif card_type == 5:
    card_amount = 100000
    card_bin = "6045781131"
elif card_type == 6:
    card_amount = 10000
    card_bin = "702126"
elif card_type == 7:
    card_amount = 10000
    card_bin = "5859752142"
elif card_type == 8:
    card_amount = 1
file_name = input(Fore.GREEN+f"Enter the log file name: ")
while True:
    try:
        num_cards = int(input(Fore.BLUE+f"How many cards do you want to generate: "))
        if 1 <= num_cards:
            break
        else:
            print(Fore.RED+f"Enter a valid number.")
    except ValueError:
        print(Fore.RED+f"Enter a valid number.")
card_amount = "{:,}".format(card_amount)
file_path = f"{file_name}"+'.txt'
randomnums = range(10)
with open(file_path, 'w') as f:
    for i in range(num_cards):
        if card_type == 8: card_num = genKey()
        else: card_num = generate_card_number(card_bin, randomnums)
        if i == 0:
            print(Fore.LIGHTCYAN_EX+f"{num_cards} card numbers have been generated and saved to {file_path}.\n")
            print(f"{'-'*50}")
            print(Fore.GREEN+f"| {'Type':<10} | {'Code':<25} | {'Amount ($)':<12} |")
            print(f"{'-'*50}")
        if card_type != 8 and luhn_checksum(card_num):
            print(Fore.GREEN+f"| {'Valid':<10} | {card_num:<25} | ${card_amount:<11} |")
            f.write(Fore.GREEN+f"| {'Valid':<10} | {card_num:<25} | {card_amount:<12} |\n")
        else:
            print(f"| {'Invalid':<10} | {card_num:<25} | {'$0':<12} |")
            #f.write(f"| {'Invalid':<10} | {card_num:<25} | {'$0':<12} |\n")
system(f"title bingle dong - cards: {num_cards}")
print(Fore.RED+f"\nPress any key to close", end=" ")
msvcrt.getch()
