import random
 
def sum_odd_even():
    n = int(input("Enter the numbers: "))
    arr = [random.randint(1, 100) for i in range(n)]
    print("Array:", arr)
 
    even_sum = 0
    odd_sum = 0
 
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_sum += arr[i]
        else:
            odd_sum += arr[i]
 
    return even_sum, odd_sum
 
even, odd = sum_odd_even()
print("Sum of even numbers:", even)
print("Sum of odd numbers:", odd)