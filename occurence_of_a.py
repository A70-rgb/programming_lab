names= input("Enter the first list of integers ,separated by spaces:").split()
a_count=0
for name in names:
    a_count+=name.lower().count('a')
print("Total occurence of 'a': ",a_count)