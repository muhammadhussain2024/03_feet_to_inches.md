def main():
    # Ask the user for the number of feet
    feet = float(input("Enter the number of feet: "))

    # Convert feet to inches
    inches = feet * 12

    # Print the result
    print(feet, "feet is", inches, "inches.")

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
