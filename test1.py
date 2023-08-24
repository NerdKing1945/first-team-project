def check_all_ones(number):
    # Convert the given number to a string to check each digit.
    number_str = str(number)
    
    # Check each digit to see if it's not equal to 1.
    for digit in number_str:
        if digit != '1':
            return False
    
    # Return True if all digits are 1.
    return True

# Test
input_number = int(input("Enter a positive number: "))
result = check_all_ones(input_number)

if result:
    print("All digits in the positive number are 1.")
else:
    print("The positive number contains digits other than 1.")
