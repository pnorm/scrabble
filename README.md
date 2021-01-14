## Game similar to Scrabble
 - 1st stage - The program draws 7 letters from the set of letters.
 - 2nd stage - The program asks the player to enter a word from the drawn letters (by the way, it checks, if the player used a letter that he does not have).
 - 3rd stage - The program checks the dictionary if a given word exists. The dictionary can be downloaded from the website https://sjp.pl/slownik/growy/ . If the word exists, it returns the numerical value of the word. If it doesn't exist, the player gets -10 points and has to re-form the word. Each letter has some value:
A = 1 B = 3 C = 3 D = 2 E = 1 F = 4 G = 2 H = 4
I = 1 J = 7 K = 4 L = 2 M = 3 N = 2 O = 1 P = 3
Q = 10 R = 1 S = 1 T = 2 U = 1 V = 7 W = 4 X = 10
X = 10 Y = 4 Z = 3
 - 4th stage - The program checks how many letters a word has been made up of, adds the missing letters and asks the player to enter another word.
 - 5ht stage - The game ends when the player scores 50 or -50 points.
