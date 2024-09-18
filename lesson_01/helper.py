def get_positive_integer_list():
    """Prompt the user for a list of positive integers and return the list."""
    while True:
        user_input = input("Please input a space-separated list of positive integer days you are interested in: ")
        numbers = user_input.split()

        if all(n.isdigit() and int(n) > 0 for n in numbers):
            return list(set(int(n) for n in numbers))  # Converting to a set removes duplicates
        else:
            print("All items must be positive integers greater than zero. Please try again.")


def get_conversion_unit():
    """Prompt the user for a unit of conversion and return the selected unit."""
    units = {
        "1": ("seconds", 24 * 60 * 60),
        "2": ("minutes", 24 * 60),
        "3": ("hours", 24)
    }
    while True:
        print("Select the unit you want to convert to:")
        for key, (name, _) in units.items():
            print(f"{key}. {name.capitalize()}")

        choice = input("Enter the number corresponding to your choice: ")
        if choice in units:
            return units[choice]
        else:
            print("Invalid choice. Please select a valid option from the list.")


def days_to_units(days, unit_details):
    """Convert days to the specified units and print the result."""
    unit_name, conversion_factor = unit_details
    for day_count in days:
        calculated_units = day_count * conversion_factor
        print(f"There are {calculated_units} {unit_name} in {day_count} days.")

