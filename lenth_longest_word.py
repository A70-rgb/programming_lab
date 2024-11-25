def longest_word_length(word_list):
    return max(len(word)for word in word_list)
word_input=input("enter a list of words separated by spaces:")
word_list=word_input.split()
print("length of the longest word :",longest_word_length(word_list)) 