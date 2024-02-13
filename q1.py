def getPrimeNumbers(n):
    prime_numbers = [num for num in range(2, n+1) 
                     if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
    return prime_numbers

try:
    n = int(input("Enter a number to check for prime numbers up to that value: "))
    prime_numbers = getPrimeNumbers(n)
    
    if prime_numbers:
        print(f"Prime numbers between 2 and {n}: {prime_numbers}")
    else:
        print(f"There are no prime numbers between 2 and {n}")
except ValueError:
    print("Please enter a valid integer.")
