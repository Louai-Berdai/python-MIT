# Program to calculate the average of four numbers entered by the user

def main():
    print("Enter four numbers to calculate their average:")
    
    try:
        # Get four numbers from user input
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        num3 = float(input("Third number: "))
        num4 = float(input("Fourth number: "))
        
        # Calculate the average
        average = (num1 + num2 + num3 + num4) / 4
        
        # Display the result
        print(f"The average of {num1}, {num2}, {num3}, and {num4} is: {average:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()