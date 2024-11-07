Word=str(input("Enter the Word:"))
for letter in Word:
if 'aeiou' in Word:
    print()
else:
    print("no vowels in the word ",str(Word))

sentence = input('Enter your sentence: ' )
for letter in sentence:
    if letter in 'aeiou':
        print(letter)