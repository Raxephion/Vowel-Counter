# -*- coding: utf-8 -*-


s=input("Please enter a word and press enter: ")
vowelcount=0
for char in s:
    if char == "i" \
        or char == "e" \
        or char == "u" \
        or char == "a" \
        or char == "o" :
        vowelcount+=1
print("Number of vowels", vowelcount)
