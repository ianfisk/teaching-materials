#!/usr/bin/env python3

def count_vowels(text):
	vowels = "aeiou"
	count = 0
	for vowel in vowels:
		count += text.count(vowel)
	return count

def count_consonants(text):
	vowels = "aeiou"
	count = 0
	for char in text:
		if char not in vowels:
			count += 1
	return count

sentence = input("Enter a sentence: ")
print(f"Number of vowels {count_vowels(sentence)}")
print(f"Number of consonants {count_consonants(sentence)}")
