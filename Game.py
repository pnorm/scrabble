from random import randint


class Game(object):
    points_for_letter = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 
                        'I': 1, 'J': 7, 'K': 4, 'L': 2, 'M': 3, 'N': 2, 'O': 1, 'P': 3, 
                        'Q': 10, 'R': 1, 'S': 1, 'T': 2, 'U': 1, 'V': 7, 'W': 4, 'X': 10,
                        'Y': 4, 'Z': 3}
    alphabet = list(points_for_letter.keys())


    def __init__(self, name):
        self.name = name
        self.n_drawed_letters = 0
        self.your_drawed_letters = []
        self.total_points = 0
        self.letters_to_replace = 3


    def start(self):
        print(f'Hello {self.name}!! Let\'s start the game!')
        print("Remember! Over the whole game you can replace 2 letters! :)")
        print("If you want to replace letter, for example 'h' type '#h'")
        print("Good luck!")


    def open_dictionary(self, filename):
        '''
        Opens file and save to the variable
        Args:
            filename (str): filename of the dictionary
        Returns:
            dictionary (list): 
        '''
        with open(file=filename, mode='r', encoding='UTF-8') as f:
            dictionary = f.read().splitlines()
        return dictionary
        

    def draw_letters(self):
        '''
        Draws n letters from alphabet
        '''
        temp_alphabet = self.alphabet
        while self.n_drawed_letters < 7:
            random_number = randint(0, len(temp_alphabet)-1)
            random_letter = temp_alphabet[random_number]
            self.your_drawed_letters.append(random_letter)
            self.n_drawed_letters += 1


    def print_player_letters(self):
        print(f"Your letters: {self.your_drawed_letters}")


    def check_if_word_exists_in_dictionary(self, dictionary, word):
        '''
        Checks if the player used the word which is in the dictionary
        Args:
            dictionary (list):
            word (str): word typed by the player 
        '''
        if word.lower() in dictionary:
            self.check_if_drawed_letters_used(word)
        else:
            print("You typed the word which doesn't exist in the dictionary :((")
            print('Please try again.')


    def check_if_drawed_letters_used(self, word):
        '''
        Checks if the player used his letters
        '''
        temp_letters = self.your_drawed_letters.copy()
        i = 0
        for char in list(word):
            if char.upper() in self.your_drawed_letters:
                self.your_drawed_letters.remove(char)
                self.n_drawed_letters -= 1
            else:
                i += 1
        if i == 0:
            print("Yeah! You're correct. This word exists in the dictionary!")
            occurences_of_letters = dict((letter, word.count(letter)) for letter in set(word))
            self.count_points(occurences_of_letters)
        else:
            print('Sorry man, but you don\'t have some of these letters.')
            print('Try again.')
            self.your_drawed_letters = temp_letters
            self.n_drawed_letters = 7


    def count_points(self, occurences_of_letters):
        '''
        Counts points for the word and update total number of points
        Args:
            occurences_of_letters (dict):
        '''
        points = 0
        for (k, v) in occurences_of_letters.items():
            points += self.points_for_letter[str(k).upper()] * v
        print(f"You got {points} points for this word")
        self.total_points += points
        print(f"Your total number of points is {self.total_points}")


    def replace_letter(self, letter):
        self.your_drawed_letters.remove(str(letter))
        self.n_drawed_letters -= 1
        self.draw_letters()
        self.letters_to_replace -= 1


    def run(self):
        '''Run script'''
        self.start()
        dictionary = self.open_dictionary('slowa.txt')
        self.draw_letters()
        while True:
            self.print_player_letters()
            your_word = str(input("Please enter your word: ")).upper()
            if len(your_word) == 2 and your_word[0] == '#' and self.letters_to_replace > 0:
                self.replace_letter(your_word[1])
            elif len(your_word) == 2 and your_word[0] == '#' and self.letters_to_replace == 0:
                print("You can't replace more letters")
            else:
                self.check_if_word_exists_in_dictionary(dictionary, your_word)
                self.draw_letters()
            if self.total_points >= 50:
                print("Congratulations!! You won!!!!! :-DD")
                break
            elif self.total_points <= -50:
                print("I'm so sorry. You lost :((((")
                break
    

if __name__ == '__main__':
    game = Game(name='Pawel')
    game.run()

