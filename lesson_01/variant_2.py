def days_to_unit(value, unit):
    # Define conversion factors for each unit
    conversion_factors = {
        "seconds": 24 * 60 * 60,
        "minutes": 24 * 60,
        "hours": 24
    }

    # Retrieve the conversion factor for the specified unit
    conversion_factor = conversion_factors.get(unit)

    # Check if the unit is valid and perform the calculation
    if conversion_factor:
        calculation_to_units = value * conversion_factor
        print(f"There are {calculation_to_units} {unit} in {value} days")
    else:
        print("Unsupported unit")

# Get user input and convert the number to an integer
try:
    number_to_convert = int(input("Please input the number of days you are interested in: "))
except ValueError:
    print("Invalid number input. Please enter a valid integer.")
    exit()

# Display unit options
print("Select the unit you want to convert to:")
print("1. Seconds")
print("2. Minutes")
print("3. Hours")

# Get unit choice from the user
unit_choice = input("Enter the number corresponding to your choice: ")

# Map the user's choice to the unit
unit_map = {
    "1": "seconds",
    "2": "minutes",
    "3": "hours"
}

# Retrieve the unit based on the user's choice
unit_of_interest = unit_map.get(unit_choice)

if unit_of_interest:
    days_to_unit(number_to_convert, unit_of_interest)
else:
    print("Invalid choice. Please select a valid option from the list.")