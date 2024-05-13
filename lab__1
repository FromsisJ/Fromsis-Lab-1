def count_occurrences(numbers, target):
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return count

numbers_input = input("Enter a sequence of numbers (separated by spaces): ")
numbers = list(map(int, numbers_input.split()))

target = int(input("Enter a number to be searched: "))

occurrences = count_occurrences(numbers, target)

if occurrences == 0:
    print(f"The number {target} is not present in the array.")
else:
    print(f"The number {target} appears {occurrences} time(s) in the array.")
