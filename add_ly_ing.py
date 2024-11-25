def add_suffix(s):
    if s.endswith('ing'):
        return s+'ly'
    return s+'ing'
user_input=input("enter the string:")
result= add_suffix(user_input)
print("modified string :",result)