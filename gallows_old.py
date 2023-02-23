gallows = [['-', '-', '-', '-', '-', '-'],
           [' ', '|', ' ', ' ', '|', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           ['/', ' ', '\\', ' ', ' ', ' ']]

def draws_gallows(error_nums=0):
    
    def draw():
        str_gallows = ''
        for lst in gallows:
            str_gallows += ''.join(lst) + '\n'
        return str_gallows
    
    if error_nums == 1:
        gallows[2][4] = 'O'
     
    if error_nums == 2:
        gallows[3][3] = '/'
   
    if error_nums == 3:
        gallows[3][4] = '|'

    if error_nums == 4:
        gallows[3][5] = '\\'
     
    if error_nums == 5:
        gallows[4][3] = '/'
   
    if error_nums == 6:
        gallows[4][5] = '\\'
  
    return draw()
    

for lst in gallows:
    print(''.join(lst))
    
# print('\n'.join([''.join(ch) for ch in gallows]))

word = "pizza"

# print("_" * len(word))

answer_word = ["_" for _ in range(len(word))]

# print(("_ " * len(word)).rstrip())

print(" ".join(answer_word))

# user_input = input("Type your letter >>>")

def find_all(text:str, substring):
    result = []
    start_position = 0
    for i in range(len(text)):
        position = text.find(substring, start_position)
        if position > -1:
            result.append(position)
            start_position = position + 1
    return result

errors_count = 0

while "".join(answer_word) != word:
    
    user_input = input("Type your letter >>>")
    
    if user_input in word:
        letter_indexes = find_all(word, user_input)
        # print(letter_indexes)
        for i in letter_indexes:
        # letter_index = word.find(user_input)
            answer_word[i] = user_input
        print(draws_gallows())
        print(" ".join(answer_word))
    else:
        errors_count += 1
        print(draws_gallows(errors_count))
        print(" ".join(answer_word))

    if errors_count >= 6:
        print("Game over \nYou lose!!!")
        break

print('You win!!!')
