import inflect
p = inflect.engine()

LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def getLetterScore(letter):
    return LETTERS.find(letter) + 1

def getWordScore(word):
    word = word.replace(",", "").replace('-', " ").replace('thous ', 'thousand ')
    score = 0
    for char in word:
        score += getLetterScore(char)
    return score


if __name__ == '__main__':
    #Arbitrary number pulled from riddle
    limit = 3140276
    counter = 0
    while counter < limit:
        num = str(counter)
        word = p.number_to_words(num, andword="")
        score = getWordScore(word)
        if score > counter:
            print("Score: {}, Number: {}, Word: {}".format(score, counter, word))
        counter += 1




