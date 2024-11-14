numbers=list(map(int,input("enter a list of integers separated by spaces:").split()))
odd_numbers=[num for num in numbers if num%2!=0]
print("list with even numbers removed:",odd_numbers)