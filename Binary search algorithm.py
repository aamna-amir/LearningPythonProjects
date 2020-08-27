# 8. Binary Search Algorithm

# Have you ever heard the proverb, “finding a needle in a haystack.” 
# This program is designed to do just that- by using a binary search algorithm. 
# You can create a list of random numbers between 0 to 100, with every succeeding number having a difference of 2 between them.
# When the user inputs a random number, the program will check if that number is included in the list. 
# It will do so by creating two halves of the list. If the program finds the number in the first half of the list, 
# it will eliminate the other half and vice versa. The search will continue until the program finds the number input of the 
# user or until the subarray size becomes 0 (this means that the number is not in the list). 
# This python project idea will help you create an implement an algorithm that searches for an element in a list. 

numbers = [i for i in range(1, 100, 2)]

print(numbers)
user = 45

def BinarySearch(lists, num):
    flag = False
    high = len(lists)-1
    low = 0
    while low < high and not flag:
        mid = (low + high)//2
        if lists[mid] == num:
            flag = True 
        else:
            if num < lists[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return lists[mid], mid

print(BinarySearch(numbers, user))