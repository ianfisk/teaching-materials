#!/usr/bin/env python3
def cnt_vowels(x):
	y = "aeiou"
	n = 0
	for v in y:
		n += x.count(v)
	return n
def cnt_consonants(m):
	x = "aeiou"
	for l in m:
		if l not in x:
			print(f"consonant={l}")
input = str(input("Enter a sentence: "))
print(f"Number of vowels {cnt_vowels(input)}")
print("Number of consonants", cnt_consonants(input))
