def get_positive_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        else:
            print("Please enter a positive integer greater than zero.")


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


def days_to_unit(value, unit_key):
    conversion_factors = {
        "1": 24 * 60 * 60,  # Seconds
        "2": 24 * 60,  # Minutes
        "3": 24  # Hours
    }

    unit_names = {
        "1": "seconds",
        "2": "minutes",
        "3": "hours"
    }

    calculation_to_units = value * conversion_factors[unit_key]
    unit_name = unit_names[unit_key]

    print(f"There are {calculation_to_units} {unit_name} in {value} days.")


# Get valid input for the number of days, ensuring it is a positive integer
number_to_convert = get_positive_integer_input("Please input the number of days you are interested in: ")

# Get valid unit choice from the user
conversion_unit_key = get_conversion_unit()

# Perform and display the conversion
days_to_unit(number_to_convert, conversion_unit_key)