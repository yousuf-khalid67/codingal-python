

#months

import calendar

# Program to display all the month names


# Get all month names
months = list(calendar.month_name)[1:]  # Exclude the first empty string

# Display the month names
for month in months:
    print(month)





#check the frequency


def check_frequency(test_dict, value):
    """
    Check the frequency of a value in the given dictionary.
    
    Args:
        test_dict: The dictionary to search
        value: The value to count
    
    Returns:
        The frequency (count) of the value
    """
    frequency = list(test_dict.values()).count(value)
    return frequency


# Example usage:
test_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 1}
target_value = 1

result = check_frequency(test_dict, target_value)
print(f"Frequency of {target_value}: {result}")

#circumference


import math

def calculate_circumference(radius):
    return 2 * math.pi * radius

# Example usage
if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    circumference = calculate_circumference(radius)
    print(f"The circumference of the circle is: {circumference}")

#set symmetric difference



# Method 1: Using the ^ operator
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

symmetric_diff = set1 ^ set2
print("Symmetric Difference:", symmetric_diff)

# Method 2: Using the symmetric_difference() method
symmetric_diff2 = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_diff2)

# Method 3: Using symmetric_difference_update()
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
set3.symmetric_difference_update(set4)
print("Symmetric Difference:", set3)







