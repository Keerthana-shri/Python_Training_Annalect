#QUESTION: TAKE N NUMBER OF RANDOM NUMBRS FROM 1 T0 100 AND CREATE A LIST.PRINT THE SUM OF ALL EVEN NUMBERS AND ODD NUMBERS OF IT SEPARATELY

import random
 
def create_random_array():
    n = int(input("Enter the number of elements: "))
    arr=[]
    for i in range(n):
        arr.append(random.randint(1,100))
    print("Array:", arr)
    return arr
 
def sum_odd_even(arr):
    even_sum = 0
    odd_sum = 0
    for num in arr:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum
 
def display_sums(even_sum, odd_sum):
    print("Sum of even numbers:", even_sum)
    print("Sum of odd numbers:", odd_sum)
 
def main():
    array = create_random_array()
    even_sum, odd_sum = sum_odd_even(array)
    display_sums(even_sum, odd_sum)
 
main()