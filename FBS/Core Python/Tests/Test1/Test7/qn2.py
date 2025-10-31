#.takes list of str as ip and new list contain uppercase of str using list comp

words=["ekata","neha","mansi"]
uppercase_words=[w.upper() for w in words]

print("Original: ", words)
print("Uppercase: ", uppercase_words)