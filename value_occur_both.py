list1=set(map(int.input("Enter the first list of integers,separated by spaces:").split()))
list2=set(map(int.input("Enter the second list of integers,separated by spaces:").split()))
common_values= list1 & list2
if common_values:
    print("common values found:",common_values)
else:
    print("no coomon value found")