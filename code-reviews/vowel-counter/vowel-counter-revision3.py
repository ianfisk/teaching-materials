#!/usr/bin/env python3

# Students haven't learned about Sets yet, so for now use string constants to
# store character sets.
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def count_characters(text, charsToCount):
	if text is None:
		raise ValueError("'text' argument must be provided")
	if charsToCount is None:
		raise ValueError("'charsToCount' argument must be provided")

	count = 0
	for char in text:
		if char in charsToCount:
			count += 1
	return count

def count_vowels(text):
	return count_characters(text, VOWELS)

def count_consonants(text):
	return count_characters(text, CONSONANTS)

sentence = input("Enter a sentence: ")
print(f"Number of vowels {count_vowels(sentence)}")
print(f"Number of consonants {count_consonants(sentence)}")
