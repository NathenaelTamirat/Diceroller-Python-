import random  # We need this to generate random numbers for the dice rolls

def roll_dice(sides=6, rolls=1):
    """
    Simulates rolling a dice.
    - sides: Number of sides on the dice (default is 6).
    - rolls: Number of times to roll the dice (default is 1).
    Returns a list of roll results.
    """
    results = []  # This will store the results of each roll
    for _ in range(rolls):  # Loop for the number of rolls
        result = random.randint(1, sides)  # Roll the dice (get a random number between 1 and sides)
        results.append(result)  # Add the result to the list
    return results  # Return the list of results

def main():
    """
    Main function to interact with the user and roll the dice.
    """
    print("Hey there! welcome to Nathenael Tamirat's roll dice game \n Lets roll some dice! 🎲")

    # Ask the user for the number of sides on the dice
    sides = input("How many sides should the dice have? (e.g., 6 for a standard dice): ")
    # Ask the user for the number of rolls
    rolls = input("How many times do you want to roll it? ")

    # Check if the inputs are valid positive integers
    if sides.isdigit() and rolls.isdigit():  # Check if the inputs are numbers
        sides = int(sides)  # Convert sides to an integer
        rolls = int(rolls)  # Convert rolls to an integer

        if sides > 0 and rolls > 0:  # Make sure the numbers are positive
            results = roll_dice(sides, rolls)  # Roll the dice!
            print(f"\nHere are your results for rolling a {sides}-sided dice {rolls} time(s):")
            print(", ".join(map(str, results)))  # Print the results in a nice format
        else:
            print("Oops! Please enter numbers greater than 0.")  # Handle invalid inputs
    else:
        print("Hmm, that doesn't look right. Please enter whole numbers only.")  # Handle non-number inputs

# Run the program
if __name__ == "__main__":
    main()