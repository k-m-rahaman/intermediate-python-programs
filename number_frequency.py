numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Number Frequency:")

for key, value in frequency.items():
    print(key, ":", value)
