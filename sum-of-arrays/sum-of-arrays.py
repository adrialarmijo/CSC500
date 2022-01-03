
sum = 0
array1 = []
array2 = []
array3 = []

print("Welcome to the Array Summizer!")
print("How this works: Enter any number of numbers into three different arrays and this program will count their sums!")
print("For more fun, let's play a guessing game!")
guess = input("What do you think the sum will be? ")

array1 = [float(item) for item in input("Please enter items for the first array: ").split()]
array2 = [float(item) for item in input("Please enter items for the second array: ").split()]
array3 = [float(item) for item in input("Please enter items for the third array: ").split()]

#Find the length of the longest array
longestArrayLength = max(map(len, (array1, array2, array3)))

i = 0
totalSum = 0
while i < longestArrayLength:
    if(array1[i] is None):
        sum += 0
    if(array2[i] is None):
        sum += 0
    if(array3[i] is None):
        sum += 0
    else:
        sum = array1[i] + array2[i] + array3[i]
        print("\tAdding: " + str(array1[i]) + " + " + str(array2[i]) + " + " + str(array3[i]))

    totalSum += sum
    print("The total so far is: " + str(totalSum))
    i += 1

answer = float(totalSum) is float(guess)
print(str(totalSum) + " " + str(guess))
print("The final total is: " + str(totalSum))
print("Your guess was: " + str(answer))