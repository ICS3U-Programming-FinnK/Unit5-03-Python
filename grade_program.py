#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: November 26th, 2023
# this program is a grade program that uses return values.
# Function for grades
def calc_mark(level: str) -> int:
    # Converting the level to uppercase for case-insensitive comparison
    level = level.upper()
    # Checking the level and returning the corresponding middle percentage mark
    if level == "1-":
        return 51
    elif level == "1":
        return 54
    elif level == "1+":
        return 58
    elif level == "2-":
        return 61
    elif level == "2":
        return 64
    elif level == "2+":
        return 68
    elif level == "3-":
        return 71
    elif level == "3":
        return 74
    elif level == "3+":
        return 78
    elif level == "4-":
        return 81
    elif level == "4":
        return 84
    elif level == "4+":
        return 98
    else:
        # Invalid response for invalid inputs.
        raise ValueError("Invalid level. Please enter a valid level from 1- to 4+.")


def main() -> int:
    mark = 0
    # User inputs the grade to the terminal
    level_input = input("Enter the level of your grade from 1- to 4+: ")
    # Try catch
    try:
        mark = calc_mark(level_input)
        # Display the mark to the user
        print(f"The middle percentage mark for level {level_input} is {mark}.")
    except ValueError as e:
        print(f"Error: {e}")
    return mark


if __name__ == "__main__":
    main()
