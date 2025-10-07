
s=input("Enter a sentence: ").split()
short_words=[w for w in s if len(w)<5]
print(short_words)