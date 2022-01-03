
sumOf = 0
i = 0
array1 = []
array2 = []
array3 = []
sumArray = []

print("Welcome to the Array Summizer!")
print("How this works: Enter any number of numbers into three different arrays and this program will count their sums!")
print("For more fun, let's play a guessing game!")
guess = input("What do you think the sum will be? ")

array1 = [float(item) for item in input("Please enter items for the first array: ").split()]
sumArray.append(array1)
array2 = [float(item) for item in input("Please enter items for the second array: ").split()]
sumArray.append(array2)
array3 = [float(item) for item in input("Please enter items for the third array: ").split()]
sumArray.append(array3)

print("Adding the following numbers:")
print(" " + str(array1))
print(" " + str(array2))
print("+" + str(array3))
print("--------------------------")
sumOf = sum(map(sum, sumArray))

answer = float(sumOf) == float(guess)
print("The sum is: " + str(sumOf))
print("Your guess was: " + str(answer))