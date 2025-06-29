from lib.calculator import sum, minus, multiply, divide
from lib.quotes import get_todays_random_quote

def main():
    print("Welcome to the CLI Calculator:")

    while True:
        print("1. Add, 2.Subtract, 3. Multiply, 4. Divide, 5.Exit ")
        choice = input("Choose Operation:")

        if choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter Second number"))
                if choice == '1':
                    result = sum(a, b)
                    print(f"{a} + {b}= {result}")
                elif choice == '2':
                    result = minus(a, b)
                    print(f"{a} - {b} = {result}")
                elif choice == '3':
                    result = multiply(a, b)
                    print(f"{a} x {b} = {result}")
                elif choice == '4':
                    result = divide(a, b)
                    print(f"{a} / {b} = {result}")

            except ValueError as e:
                print ("Invalid input", e)

                
            #operation
        elif choice == '5':
            quote= get_todays_random_quote()
            print(f"Today's Quote: {quote}")
            break
        else:
            print("Invalid choice. Please try again.")




if __name__ =="__main__":
    main()
        