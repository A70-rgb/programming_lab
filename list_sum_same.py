list1=map(int.input("Enter the first list of integers,separated by spaces:").split())
list2=map(int.input("Enter the second list of integers,separated by spaces:").split())
if sum(list1)==sum(list2):
    print("the list sum to the same value")
else:
    print("The lists do not sun to the value")