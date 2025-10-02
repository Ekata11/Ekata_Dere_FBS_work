# find all unique words and count freq of occurence from given list of strings.use python date set type

def word_count(words):
    freq={}
    for w in words:
        if w not in freq:
            freq[w] =0
        freq[w] += 1
        
    return freq
print(word_count(["apple","banana","apple","fruits"]))