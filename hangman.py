from nltk.corpus import PlaintextCorpusReader
import random

def play_loop():
    print "\n\n\n\n\nWelcome to Hangman! \nThe game where you get to hang a man!"
    newgame = Game()
    while not newgame.check_win() and not newgame.check_lose(): 
        print newgame
        newgame.guesses() 
    if raw_input('Do you want to play again?> ').upper() == 'Y':
        play_loop()
    else:
        print "Ok, I don't want to play with you either."

def get_word():
    corpus_root = "/home/aria/projects/hangman/outsidecorpus/"
    wordlists = PlaintextCorpusReader(corpus_root, '.*')
    word = random.choice(wordlists.words('corpus.txt')).lower()
    while not word.isalpha():
        word = random.choice(wordlists.words('corpus.txt')).lower()
    return word

class Game(object):
    
    def __init__(self):
        self.word = get_word()
        self.pre = []
        self.hangman = HangMan()
    
    def prepstring(self):
        res = []
        for ch in self.word:
            if ch not in self.pre:
                res.append('_ ')
            elif not ch.isalnum():
                res.append(ch)
            else:
                res.append(ch)
        return ''.join(res)

    def guesses(self):
        guess = raw_input("> ").lower()
        if guess in self.pre:
            print "You've already guessed that letter"
            self.guesses()
        else:
            self.pre.append(guess)
            if guess in self.word:
                return True
            else:
                self.hangman.bad_guess()
                return False 

    def __str__(self):
        s = self.hangman.__str__()
        p = self.prepstring()
        ch = [ ch for ch in self.pre if ch not in self.word ]
        return "\n\n%s\n\n\nGuess this word!   %s\n\nWrong guesses%s" % (s,p,str(ch))

    def check_win(self):
        if all(c in self.pre for c in self.word):
            print "\n\n\nCongrats, you've won!"
            print self.__str__()
            return True
        else:
            return False

    def check_lose(self):
        if self.hangman.total == self.hangman.num:
            print "You're not very good at this....\n"
            print self.__str__()
            print "\nThe word you were tring to guess was %s" % (self.word)
            return True
        else:
            return False

class HangMan(object):

    def __init__(self, num=6):
        self.num = num
        self.poss = {self.num:num}
        self.total = 0
        self.rep = self.man()

    def __str__(self):
        return self.rep

    def bad_guess(self):
        self.poss[self.num] -= 1
        self.rep = self.man()

    def man(self):
        self.total = self.num - self.poss[self.num]
        dude = { 0 :"""                 ____
                |    |
                |     
                |   
                |
            ____|____ 
           |         |_
           |           |_
           |_____________|""",

        1  : """                 ____
                |    |
                |    0 
                |   
                |
            ____|____
           |         |_
           |           |_
           |_____________| """,

         2 : """                 ____
                |    |
                |    0 
                |    |
                |
            ____|____
           |         |_
           |           |_
           |_____________|  """,

        3 :  """                 ____
                |    |
                |   \\0 
                |    |
                |
            ____|____
           |         |_
           |           |_
           |_____________|  """,

         4 : """                 ____
                |    |
                |   \\0/ 
                |    |
                |
            ____|____ 
           |         |_
           |           |_
           |_____________| """,

        5 :  """                 ____
                |    |
                |   \\0/ 
                |    |
                |   /
            ____|____ 
           |         |_
           |           |_
           |_____________| """,

        6 :  """                 ____
                |    |
                |   \\0/ 
                |    |
                |   / \\
            ____|____ 
           |         |_
           |           |_
           |_____________| """}
        return dude[self.total]

if __name__ == "__main__":

    play_loop()
    #print get_word()

    # newgame = Game()
    # if newgame.guesses():
    #     print newgame.word
    # else:
    #     print newgame.pre

    # print newgame