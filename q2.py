
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###

str_list = []
shortest_word = None
longest_word = None

while True:
    user_input = input("Enter a string: ")
    if user_input in ['stop', 'STOP']:
        break
    if shortest_word == None:
        shortest_word = user_input
    if longest_word == None:
        longest_word = user_input

    if len(user_input) < len(shortest_word):
        shortest_word = user_input
    if len(user_input) > len(longest_word):
        longest_word = user_input

    str_list.append(user_input)


print(longest_word, shortest_word)
