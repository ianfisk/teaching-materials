#!/usr/bin/env python3

VOWELS = "aeiou"

def count_vowels(text):
	if text is None:
		raise ValueError("'text' argument must be provided")

	count = 0
	for vowel in VOWELS:
		count += text.count(vowel)
	return count

def count_consonants(text):
	if text is None:
		raise ValueError("'text' argument must be provided")

	count = 0
	for char in text:
		if char not in VOWELS:
			count += 1
	return count

sentence = input("Enter a sentence: ")
print(f"Number of vowels {count_vowels(sentence)}")
print(f"Number of consonants {count_consonants(sentence)}")
