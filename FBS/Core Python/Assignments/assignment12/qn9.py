# cal no of words and no of char present in str


def count_words_char(str1):
    w=0                  #word and char count
    c=0
    in_word=0
    for ch in str1:
        if ch != " ":
            c += 1
            if in_word==0:
                w += 1
                in_word=1
        else:
            in_word=0
    print("Words :", w)
    print("Char : ", c)
    
count_words_char("Hello world")
      
      
      
      
      
      
        
        