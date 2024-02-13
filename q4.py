def stats_decorator(func):
    def wrapper(numbers):
        count = len(numbers)
        total = sum(numbers)
        average = total / count
        maximum = max(numbers)

        print("Numbers:", numbers)
        print("Count:", count)
        print("Average:", average)
        print("Maximum:", maximum)
        
        return func(numbers)
    
    return wrapper

@stats_decorator
def process_numbers(numbers):
    pass

def printStats(t):
    with open(t, 'r') as file:
        for line in file:
            numbers = [int(num) for num in line.split()]
            process_numbers(numbers)

# Test the function
printStats('numbers.txt')
