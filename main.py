import converter

def display_program_title():
    print("Welcome to the Temperature Conversion Calculator")

def display_conversion_menu():
    print("Please select your conversion option")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")

def main():
    display_program_title()
    
    while True:
        display_conversion_menu()
        user_selection = int(input("\nEnter your choice (1, 2, or 3): "))

        if user_selection == 1:
            fahrenheit_input = float(input("\nEnter your  temperature in Fahrenheit: "))
            celsius_result = converter.convert_fahrenheit_to_celsius(fahrenheit_input)
            print(f"{fahrenheit_input} Fahrenheit is approximately {celsius_result} Celsius.\n")

        elif user_selection == 2:
            celsius_input = float(input("\nEnter your  temperature in Celsius: "))
            fahrenheit_result = converter.convert_celsius_to_fahrenheit(celsius_input)
            print(f"{celsius_input} Celsius is approximately {fahrenheit_result} Fahrenheit.\n")

        elif user_selection == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
