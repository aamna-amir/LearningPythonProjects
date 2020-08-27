# 8. Binary Search Algorithm

# Have you ever heard the proverb, “finding a needle in a haystack.” 
# This program is designed to do just that- by using a binary search algorithm. 
# You can create a list of random numbers between 0 to 100, with every succeeding number having a difference of 2 between them.
# When the user inputs a random number, the program will check if that number is included in the list. 
# It will do so by creating two halves of the list. If the program finds the number in the first half of the list, 
# it will eliminate the other half and vice versa. The search will continue until the program finds the number input of the 
# user or until the subarray size becomes 0 (this means that the number is not in the list). 
# This python project idea will help you create an implement an algorithm that searches for an element in a list. 

numbers = []
for i in range(1, 100, 2):
    numbers.append(i)

print(numbers)

user = int(input("Enter a number for searching: "))

if user in numbers:
    print("Number Found.")