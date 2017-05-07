from Deque import Deque
# Deque is already defined in Deque.py

def is_pallindrome(word):
    d = Deque()

    if len(word) > 1:
        for char in word:
            d.add_rear(char)

        equal = True
        while d.size() > 1 and equal:
            first_char = d.remove_front()
            last_char = d.remove_rear()
            if first_char == last_char:
                equal = True
            else:
                return False

        return True
    else:
        return 'The word should consist of at least two chars.'

if __name__ == '__main__':
    while True:
        print('Please, input the word to check:')
        print(is_pallindrome(input()))