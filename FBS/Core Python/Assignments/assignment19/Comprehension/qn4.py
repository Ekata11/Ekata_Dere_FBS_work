
s=input("enter a string: ")
no_vowels=''.join(ch for ch in s if ch.lower() not in "aeiou")
print("Without vowels:", no_vowels)