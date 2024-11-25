import random
import string
import os

# Create terminal color codes
class bc:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WHITE = '\u001b[37m'
    FAIL = '\033[91m'
    RESETC = '\033[0m'
    YELLOW = '\033[93m'
    PURPLE = '\033[95m'

# Creating a function that removes everything except numbers
def no(s, default=None):
    if not s:
        return default
    return int(''.join(filter(str.isdigit, s)))

# Function to generate a random string based on user input
def generate_random_string(length, char_type_input):
    character_type = ''
    if '1' in char_type_input:
        character_type += string.ascii_lowercase
    if '2' in char_type_input:
        character_type += string.ascii_uppercase
    if '3' in char_type_input:
        character_type += string.digits
    if '4' in char_type_input:
        character_type += string.punctuation
    if '5' in char_type_input:
        character_type = string.ascii_letters + string.digits + string.punctuation

    # If the user didn't enter 1-5, print an error
    if not character_type:
        print(f"{bc.FAIL}Invalid character types selected. Please try again.{bc.RESETC}")
        return None

    # Generate the string based on users input
    random_string = ''.join(random.choice(character_type) for _ in range(length))
    return random_string

# Main function to handle user input and generate strings
def main():
    length = None
    char_type_input = None

    while True:
        if length is None or char_type_input is None:
            length = no(input(f"Enter the length of the string:\n{bc.PURPLE}- {bc.RESETC}"))
            os.system('cls' if os.name == 'nt' else 'clear')
            char_type_input = str(no(input(f"Enter the types of characters you want\n(i.e 123 = Lowercase, Uppercase, and Numbers)\n{bc.GREEN}1 = Lowercase\n2 = Uppercase\n3 = Numbers\n4 = Special Characters\n5 = All of the above\n{bc.PURPLE}- {bc.RESETC}")))
            os.system('cls' if os.name == 'nt' else 'clear')
        gen_amount_input = no(input(f"How many strings do you want to generate\nLeave empty for 1:\n{bc.PURPLE}- {bc.RESETC}"), default=1)

        os.system('cls' if os.name == 'nt' else 'clear')

        # Say 'Strings' if the user want to generate more than one.
        print(f"Generated {gen_amount_input}x {length} character {'string' if gen_amount_input == 1 else 'strings'}:")

        for _ in range(gen_amount_input):
            random_string = generate_random_string(length, char_type_input)

            if random_string:
                print(f"{bc.PURPLE} - {random_string}{bc.RESETC}")

        # Prompt user for next action
        user_choice = no(input(f"{bc.GREEN}1 = Start over\n2 = Generate new string\n3 = I'm finished\n{bc.PURPLE}- {bc.RESETC}"))

        if user_choice == 1:
            length = None
            char_type_input = None
            os.system('cls' if os.name == 'nt' else 'clear')
            continue  # Start over
        elif user_choice == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue  # Generate new string
        elif user_choice == 3:
            print(f"{bc.GREEN}Exiting the code.{bc.RESETC}")
            break  # End the code

if __name__ == "__main__":
    main()
