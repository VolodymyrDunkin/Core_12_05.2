from random import choice

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
    
    match error_nums:
        case 1:
            gallows[2][4] = 'O'
        case 2:
            gallows[3][3] = '/'
        case 3:
            gallows[3][4] = '|'
        case 4:
            gallows[3][5] = '\\'
        case 5:
            gallows[4][3] = '/'
        case 6:
            gallows[4][5] = '\\'
  
    return draw()

def find_all(text:str, substring):
    result = []
    start_position = 0
    for i in range(len(text)):
        position = text.find(substring, start_position)
        if position > -1:
            result.append(position)
            start_position = position + 1
    return result



def main():
    word = choice(["pizza", "lasagna", "banana", "shaurma", "burger", "borsch"])
    answer_word = ["_" for _ in range(len(word))]
    errors_count = 0
    lose = False
    
    print(draws_gallows())
    print(" ".join(answer_word))
    
    while "".join(answer_word) != word:        
        user_input = input("Type your letter >>>").lower()
        
        if user_input in word:
            letter_indexes = find_all(word, user_input)
            for i in letter_indexes:
                answer_word[i] = user_input
            print(draws_gallows())
            print(" ".join(answer_word))
        else:
            errors_count += 1
            print(draws_gallows(errors_count))
            print(" ".join(answer_word))

        if errors_count >= 6:
            lose = True
            break
    if lose:
        print("Game over \nYou lose!!!")
    else:
        print("You win!!!")
    

if __name__ == "__main__":
    main()
