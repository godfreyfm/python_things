import datetime
import time
import keyboard  # Ensure this library is installed


# Constants
CHECK_INTERVAL = 5  # seconds for countdown check
CONTINUE_PROMPT_TIMEOUT = 10  # seconds to wait for user input


def display_goal_and_deadline(current_goal, deadline):
    """Prints the user's goal and the countdown deadline."""
    print(f"\nYour goal: {current_goal}")
    print(f"Countdown to: {deadline}")


def calculate_remaining_time(deadline):
    """Calculates the remaining time until the deadline."""
    current_time = datetime.datetime.now()
    return deadline - current_time


def format_time_for_display(remaining_time):
    """Formats the remaining time for display."""
    days, seconds = remaining_time.days, remaining_time.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return days, hours, minutes, seconds


def prompt_to_continue():
    """Asks the user whether to continue the countdown."""
    print("\nDo you want to continue the countdown? (yes/no)")
    start_time = time.time()
    while True:
        if keyboard.is_pressed('y'):
            print("Continuing the countdown...")
            return True
        elif keyboard.is_pressed('n'):
            print("You chose not to continue.")
            return False
        elif time.time() - start_time > CONTINUE_PROMPT_TIMEOUT:
            print("\nNo response detected. Exiting the program due to lack of user input.")
            return None
        time.sleep(0.1)  # Small delay for responsiveness


def countdown(deadline):
    """Main countdown logic."""
    display_goal_and_deadline(user_goal, deadline)
    iteration_count = 0

    while True:
        remaining_time = calculate_remaining_time(deadline)

        if remaining_time <= datetime.timedelta(0):
            print("Time's up!")
            break

        days, hours, minutes, seconds = format_time_for_display(remaining_time)
        print(f"Time remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", flush=True)

        if keyboard.is_pressed('esc'):
            print("\nExiting the countdown.")
            break

        iteration_count += 1

        if iteration_count >= 10:  # Prompt after every 10 iterations
            continue_decision = prompt_to_continue()
            if continue_decision is None:  # No response
                break
            elif not continue_decision:  # User chose not to continue
                break

            iteration_count = 0  # Reset the counter

        time.sleep(CHECK_INTERVAL)


def get_user_goal_and_date():
    """Gets the user's goal description and commitment date."""
    user_goal_input = input("Please enter your goal (e.g., 'Learn Python programming'): ").strip()
    month = int(input("Enter the month (numeric, e.g., 10 for October): ").strip())
    day = int(input("Enter the day (numeric, e.g., 2 for the 2nd): ").strip())
    year = int(input("Enter the year (numeric, e.g., 2024): ").strip())

    deadline = datetime.datetime(year, month, day, 23, 59, 59)  # Set to end of the day
    return user_goal_input, deadline


# Main execution
user_goal, user_deadline = get_user_goal_and_date()  # Using distinct variable names
countdown(user_deadline)
