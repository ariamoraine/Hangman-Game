import random

words = 'Lollygag Widdershins Ornery Nincompoop Aardvark Bacon Banjo Aardvark Abacus Abundance Ache Acupuncture Airbrush Alien Anagram Angle Amazing Ankle Alphabet Antenna Aqua Asphalt Bacon Banana Bangles Banjo Bankrupt Bar Barracuda Basket Beluga Binder Birthday Bisect Blizzard Blunderbuss Boa Bog Bounce Broomstick Brought Bubble Budgie Bug Bugger Buff Burst Butter Buzz Cabana Cake Calculator Camera Candle Carnival Carpet Casino Cashew Catfish Ceiling Celery Chalet Chalk Chart Cheddar Chesterfield Chicken Chinchill Chocolate Chowder Coal Compass Compress Computer Conduct Contents Cookie Copper Corduroy Cow Cracker Crackle Croissant Cube Cupcake Curly Curtain Cushion Cuticle Daffodil Delicious Dictionary Dimple Disk Dodo Dolphin Dong Donuts Dork Dracula Effigy Egad Elastic Elephant Encasement Erosion Eyelash Fabulous Fantastic Feather Fetish Financial Finger Finite Fish Fizzle Fizzy Flash Flavour Flick Flock Flour Flower Foamy Foot Fork Fritter Fudge Funny Fuse Fusion Fuzzy Garlic Gelato Ghetto Glebe Glitter Glossy Groceries Goulashes Guacamole Gumdrop Haberdashery Hamster Happy Highlight Hippopotamus Hobbit Hold Hooligan Hydrant Icicles Idiot Implode Implosion Indeed Issue Itchy Jewel Jump Kabob Kasai Kite Kiwi Ketchup Knob Laces Lacy Laughter Laundry Leaflet Legacy Leprechaun Lollypop Lumberjack Macadamia Magenta Magic Magnanimous Mango Margarine Medicine Meh Melon Meow Mesh Metric Microphone Minnow Mitten Mozzarella Muck Mumble Mushy Mustache Nanimo Noodle Nostril Nuggets Oatmeal Oboe Octopus Odour Ointment Olive Overhead Oxen Pajamas Pancake Pansy Paprika Parmesan Pasta Pattern Pecan Pen Pepper Pepperoni Peppermint Perfume Periwinkle Photograph Pie Pierce Pillow Pimple Pineapple Pistachio Plush Polish Pompom Poodle Pop Popsicle Prism Prospector Prosper Pudding Puppet Puzzle Queer Query Radish Rainbow Ribbon Rotate Salami Sandwich Saturday Saturn Saxophone Scissors Scooter Scrabbleship Scrunchie Scuffle Shadow Sickish Silicone Slippery Smash Smooch Smut Snap Snooker Socks Soya Spaghett Sparkle Spatula Spiral Splurge Spoon Sprinkle Square Squiggle Squirrel Statistics Stuffing Sticky Sugar Sunshine Super Swirl Taffy Tangy Tape Tat Teepee Telephone Television Thinkable Tip Tofu Toga Trestle Tulip Turnip Turtle Tusks Ultimate Unicycle Unique Uranus Vegetable Waddle Waffle Wallet Walnut Wagon Window Whatever Whimsical Wobbly Yellow Zap Zebra Zigzag'.split()

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

def get_word(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex].lower()

class Game(object):
    
    def __init__(self):
        self.word = get_word(words)
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