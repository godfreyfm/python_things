# from helper import get_conversion_unit, get_positive_integer_list, days_to_units
from helper import *

def main():
    """Main program loop for user interaction."""
    while True:
        days_to_convert = get_positive_integer_list()
        unit_details = get_conversion_unit()
        days_to_units(days_to_convert, unit_details)

        # Option to continue or exit
        continue_choice = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Exiting the program. Goodbye!")
            break


# Run the main loop
if __name__ == "__main__":
    main()
