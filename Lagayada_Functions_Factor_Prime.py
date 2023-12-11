def smallest_factor():
    while True:
        n = int(input("\nEnter an integer n >= 2: "))
        if n < 2:
            print("Invalid input. Enter a number greater than 2.")
            break
        else:
            is_prime = True
            for i in range(2,n):
                if n % i == 0:
                    is_prime = False
                    print(f"The smallest factor other than 1 for {n} is: {i}")
                    break

            if is_prime:
                print(f"{n} is a prime number.")

def prime_numbers():
    while True:
        start_range = int(input("\nEnter a number [start]: "))

        # terminate the program if the user enters 0
        if start_range == 0:
            print("Program Terminated.")
            break

        # check if the start_range is a non-negative number
        if start_range < 0:
            print("Enter a non-negative number.")
            continue

        end_range = int(input("Enter a number [end]: "))

        # check if the end_range is greater than the start_range
        if end_range <= start_range:
            print(f"Enter a number greater than {start_range}.")
            continue

        # display prime numbers
        print(f"Prime numbers between {start_range} and {end_range} are: ", end=" ")

        # formula in getting prime numbers
        for number in range(start_range, end_range + 1):
            if number > 1:
                for i in range(2, number):
                    if number % i == 0:
                        break
                else:
                    print(number, end=" ")
        print()

def main():
    while True:
        print("\nPlease Select a Choice: ")
        print("[1] Find the smallest factor of a n.")
        print("[2] Find the prime numbers in a range.")
        print("[0] Exit.")

        choice = int(input("\nEnter a choice: "))

        if choice == 0:
            print("Program Terminated.")
            break
        elif choice == 1:
            smallest_factor()
        elif choice == 2:
            prime_numbers()
        else:
            print("Invalid choice. Please enter 1 or 2 only.")

main()

