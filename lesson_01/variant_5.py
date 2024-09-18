def get_positive_integer_list(prompt):
    while True:
        user_input = input(prompt)
        numbers = user_input.split()
        valid_numbers = []

        for number in numbers:
            if number.isdigit() and int(number) > 0:
                valid_numbers.append(int(number))
            else:
                print(f"'{number}' is not a positive integer. Please enter only positive integers.")
                break
        else:
            # Eliminate duplicates
            return list(set(valid_numbers))

def get_conversion_unit():
    while True:
        print("Select the unit you want to convert to:")
        print("1. Seconds")
        print("2. Minutes")
        print("3. Hours")

        choice = input("Enter the number corresponding to your choice: ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please select a valid option from the list.")

def days_to_unit(values, unit_key):
    conversion_factors = {
        "1": 24 * 60 * 60,  # Seconds
        "2": 24 * 60,       # Minutes
        "3": 24             # Hours
    }

    unit_names = {
        "1": "seconds",
        "2": "minutes",
        "3": "hours"
    }

    for value in values:
        calculation_to_units = value * conversion_factors[unit_key]
        unit_name = unit_names[unit_key]

        print(f"There are {calculation_to_units} {unit_name} in {value} days.")

def main():
    while True:
        # Get a list of valid inputs for the number of days
        numbers_to_convert = get_positive_integer_list("Please input a space-separated list of the number of days you are interested in: ")

        # Get valid unit choice from the user
        conversion_unit_key = get_conversion_unit()

        # Perform and display the conversion for each number
        days_to_unit(numbers_to_convert, conversion_unit_key)

        # Option to continue or exit
        continue_choice = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Exiting the program. Goodbye!")
            break

# Run the main loop
if __name__ == "__main__":
    main()