list1=input("Enter the first list of integers,separated by spaces:").split()
list2=input("Enter the second list of integers,separated by spaces:").split()
if len(list1)==len(list2):
    print("the list are of the same length")
else:
    print("The lists are of different lengths")