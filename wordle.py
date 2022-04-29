# Wordle game assignment
# VU - Manav Khanderiya
import random
import string


def test_word(word, guess, alpha, arr, tempList):
    for i in range(5):
        char1, char2 = word[i], guess[i]
        print(char2, "-", sep="", end="")
        if char1 == char2:
            print("🟩")
            if char2 not in tempList:
                tempList.append(char2)
            arr[i] = char2
        elif char2 not in word:
            print("⬛")
            try:
                alpha.remove(char2)
            except ValueError:
                pass
        else:
            w_cnt = 0
            for elem in word:
                if elem == char2:
                    w_cnt += 1
            g_cnt = 0
            for elem in guess[:i]:
                if elem == char2:
                    g_cnt += 1
            if w_cnt - g_cnt > 0:
                print("🟨")
            else:
                print("⬛")
            if char2 not in tempList:
                tempList.append(char2)
    print("Correct letters-", tempList)
    print("Progress-", arr)
    print("Available letters-", end=" ")
    for char in alpha:
        print(char, end="")
    print()


def wordle(word):
    alphabet_string = string.ascii_uppercase
    alpha_list = list(alphabet_string)
    arr = ["_", "_", "_", "_", "_"]
    tempList = []
    count = 6
    i = 1
    while i <= 6:
        print("Guesses Left:", count)
        if i == 1:
            guess = input("Please Enter Your Guess: ")
        else:
            guess = input("Please Enter Your Next Guess: ")

        if len(guess) != 5:
            print("Please enter a valid 5 letter word.")
            i -= 1
            continue

        guess = guess.upper()
        test_word(word, guess, alpha_list, arr, tempList)
        count -= 1

        if word == guess:
            print()
            print("*****************************************")
            print("Hurray!!")
            print("The Word Was ", word, "!", sep="")
            print("You Have Solved The Wordle!!")
            print("*****************************************")
            return
        i += 1

    print("*****************************************")
    print("The Word Was ", word, "!", sep="")
    print("Better Luck Next Time.")
    print("*****************************************")
    return


if __name__ == '__main__':
    alphabet_string = string.ascii_lowercase
    alphabet_string = alphabet_string.upper()
    f = open("words.txt", "r")
    wordList = []
    for elem in f:
        elem = elem.upper()
        wordList.append(elem[:5])
    word = random.choice(wordList)
    print("*****************************************")
    print("Welcome!")
    print("*****************************************")
    wordle(word)
    f.close()
