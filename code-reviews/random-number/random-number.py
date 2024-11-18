import random
import hangman

def random_number_in_range(minValueInclusive, maxValueExclusive):
	offset = round(random.random() * (maxValueExclusive - minValueInclusive)) - 1
	return minValueInclusive + offset

dictionary = ['python', 'array', 'object', 'class', 'random', 'code']
randomIndex = random_number_in_range(0, len(dictionary))
randomWord = dictionary[randomIndex]

# Make a new hangman game.
game = hangman.newGame()

# Play the game.
game.play(randomWord)
