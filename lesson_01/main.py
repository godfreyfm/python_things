
def days_to_unit (value, unit):
    calculation_to_units = ""
    if unit == "seconds":
        calculation_to_units = value * 24 * 60 * 60
    elif unit == "minutes":
        calculation_to_units = value * 24 * 60
    elif unit == "hours":
        calculation_to_units = value * 24
    print(f"There are {calculation_to_units} {unit} in {value} days")


days_to_unit(30, "seconds")
days_to_unit(30, "minutes")
days_to_unit(30, "hours")



