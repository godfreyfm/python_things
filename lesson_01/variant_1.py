# Get user input and convert the number to an integer
number_to_convert = input("Enter the number of days you are interested in converting: ")
# Attempt to convert to an integer, handle exceptions if the conversion fails
try:
    number_to_convert = int(number_to_convert)
except ValueError:
    print("Invalid number input. Please enter a valid integer.")
    exit()

unit_of_interest = input("Enter one of the following units (seconds || minutes || hours): ")

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

# Call the function with the converted number
days_to_unit(number_to_convert, unit_of_interest)