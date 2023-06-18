import random
import msvcrt
import time

# ANSI escape codes for text colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
PURPLE = '\033[95m'
RESET_COLOR = "\033[0m"

def generate_card_number(card_bin, randomnums):
    # Generate a random 6-digit number for the card suffix
    card_suffix = ''.join(str(random.choice(randomnums)) for _ in range(6))
    # Concatenate the bin and card suffix to form the complete card number
    card_num = card_bin + card_suffix
    return card_num

def luhn_checksum(card_num):
    """
    Calculates the Luhn checksum for a given card number.
    Returns True if the checksum is valid, False otherwise.
    """
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
            newKey += '-'
        else:
            newKey += symbols[digit]
        x += 1
    return newKey

print(f"{PURPLE}██████╗  █████╗ ████████╗██╗  ██╗███████╗    ███████╗ ██████╗     ██████╗ ███████╗███╗   ██╗")
print(f"██╔══██╗██╔══██╗╚══██╔══╝██║  ██║██╔════╝    ██╔════╝██╔════╝    ██╔════╝ ██╔════╝████╗  ██║")
print(f"██████╔╝███████║   ██║   ███████║███████╗    ███████╗██║         ██║  ███╗█████╗  ██╔██╗ ██║  ")
print(f"██╔══██╗██╔══██║   ██║   ██╔══██║╚════██║    ╚════██║██║         ██║   ██║██╔══╝  ██║╚██╗██║")
print(f"██║  ██║██║  ██║   ██║   ██║  ██║███████║    ███████║╚██████╗    ╚██████╔╝███████╗██║ ╚████║   ")
print(f"╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝ ╚═════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝")
print(RESET_COLOR)

print(f"{PURPLE}[/] Coded by: 𝙧𝙖𝙩𝙝#8595 || (v.2.2.0){RESET_COLOR}\n")

# Set the correct password
password = null

# Loop until the correct password is entered
user_password = input(f"{PURPLE}[/] Please enter the product key to generate Store Card Numbers: {RESET_COLOR}")
if user_password != password:
    print(f"{PURPLE}Key Invalid, Terminating program in 2 seconds{RESET_COLOR}")
    time.sleep(2)
    exit()

if user_password == password:
    # Prompt the user to select the type of card they want to generate
# Prompt the user to select the type of card they want to generate
 while True:
    try:
        card_type = int(
            input(f"{PURPLE}[/] Select the type of card to generate:\n{YELLOW}1. [/] $1k Amazon Store Card\n{YELLOW}2. [/] $5k Amazon Store Card\n{YELLOW}3. [/] $10k Amazon Store Card\n{YELLOW}4. [/] $50k Amazon Store Card\n{YELLOW}5. [/] $100k Amazon Store Card\n{YELLOW}6. [/] Best Buy Store Card\n{YELLOW}7. [/] Target Store Card\n{YELLOW}8. {{*BONUS OPTION*}} Steam Key\n{PURPLE}[☆] Choose the option you want: {RESET_COLOR}"))
        if card_type in [1, 2, 3, 4, 5, 6, 7, 8]:
            break
        else:
            print(f"{PURPLE}Invalid option.{RESET_COLOR}")
    except ValueError:
        print(f"{PURPLE}Invalid option.{RESET_COLOR}")

# Determine the amount and bin for the selected card type
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

# Prompt the user to enter the file name to save the generated card numbers
file_name = input(f"{PURPLE}Enter the name of the text file you want the codes to save to: {RESET_COLOR}")

# Prompt the user to enter the number of cards they want to generate
while True:
    try:
        num_cards = int(input(f"{PURPLE}How many cards do you want to generate: {RESET_COLOR}"))
        if 1 <= num_cards:
            break
        else:
            print(f"{PURPLE}Enter a valid number.{RESET_COLOR}")
    except ValueError:
        print(f"{PURPLE}Enter a valid number.{RESET_COLOR}")

card_amount = "{:,}".format(card_amount)

# Generate and write the specified number of card numbers to the file
file_path = f"{file_name}.txt"
randomnums = range(10)
with open(file_path, 'w') as f:
    for i in range(num_cards):
        if card_type == 8: card_num = genKey()
        else: card_num = generate_card_number(card_bin, randomnums)
        if i == 0:
            print(f"{num_cards} card numbers have been generated and saved to {file_path}.\n")
            print(f"{RED}{'-'*50}")
            print(f"| {RED}{'Type':<10}{RED} | {'Code':<25} | {RED}{'Amount ($)':<12}{RED} |{RESET_COLOR}")
            print(f"{RED}{'-'*50}{RESET_COLOR}")
        if card_type != 8 and luhn_checksum(card_num):
            print(f"| {GREEN}{'Valid':<10}{RED} | {GREEN}{card_num:<25} | {GREEN}${card_amount:<11}{RESET_COLOR} |")
            f.write(f"| {'Valid':<10} | {card_num:<25} | {card_amount:<12} |\n")
        else:
            print(f"| {RED}{'Invalid':<10}{RED} | {RED}{card_num:<25} | {RED}{'$0':<12}{RESET_COLOR} |")
            #f.write(f"| {'Invalid':<10} | {card_num:<25} | {'$0':<12} |\n")

print(f"\n{RED}Press any key to close{RESET_COLOR}", end=" ")
msvcrt.getch()
