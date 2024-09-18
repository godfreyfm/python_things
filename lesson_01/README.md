# Days to Units Converter

This project is a Python script designed to convert a specified number of days into seconds, minutes, or hours. It allows users to input a list of days and efficiently calculates the equivalent time in the desired unit while ensuring inputs are unique and valid.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contribution Guidelines](#contribution-guidelines)
- [Support and Contact](#support-and-contact)
- [License](#license)

## Project Overview

The Days to Units Converter is a simple, interactive command-line application designed to assist users in converting time measurements using a straightforward approach. It allows for processing multiple entries simultaneously, providing quick conversion results with options for repeated use.

## Features

- **Time Conversion**: Converts a list of days to seconds, minutes, or hours.
- **Input Validation**: Ensures inputs are positive integers, rejecting invalid entries.
- **Duplicate Handling**: Automatically filters out duplicate day entries for unique results.
- **Interactivity**: Allows users to perform multiple conversions without restarting the application.

## Installation

To use this script, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/days-to-units-converter.git
   cd days-to-units-converter

## Prerequisites
- Ensure you have Python 3.x installed.
## Usage

Run the script using Python from your terminal or command prompt:

    python days_to_units_converter.py

### Input Prompt:
- Enter a space-separated list of positive integers representing days.
- Choose a conversion unit (1 for seconds, 2 for minutes, 3 for hours).
- The script will output conversion results and provide an option for additional conversions.
## Examples
Here's an example interaction with the script:

text

Please input a space-separated list of positive integer days you are interested in: 5 10 15 5
Select the unit you want to convert to:
1. Seconds
2. Minutes
3. Hours
Enter the number corresponding to your choice: 1
There are 432000 seconds in 5 days.
There are 864000 seconds in 10 days.
There are 1296000 seconds in 15 days.
Do you want to perform another conversion? (yes/no): no
Exiting the program. Goodbye!

## Contribution Guidelines
We welcome contributions to enhance this project. To contribute:

1. Fork the project repository.
2. Create a feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a pull request describing your changes.
## Support and Contact
For support, issues, or questions, please reach out through GitHub Issues.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.