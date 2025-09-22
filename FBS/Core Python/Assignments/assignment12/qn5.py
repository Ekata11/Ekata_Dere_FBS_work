# count the no of vowels in str

def vowels(str1):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in(str1):
        for v in vowels:
            if ch==v:
                count += 1
                break
        
    return count

text = "Firstbit Solution, Pune"
print(vowels(text))   


