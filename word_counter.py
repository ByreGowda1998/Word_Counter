                       #  Project = WORD_COUNTER

'''
 These project  involves  taking content from the text file  and counting  no of the word in text file
 & and how many times each word is repeated ,creating another file which includes no word and 
how many times each word repeated   in text file
'''



import operator                          # importing operator for sorting dictionary based on values in dictionary

file_S=open("Shakespeare.txt","r")         # file that has content on it  

content=(file_S.read())  
content=content.lower()                   # converting all the content in to lowercase 





file_W=open("countwords.txt","w")          # creating empty file  





def word_counter(str):
    """
    these function called word_counters takes  sentence or paragraph as parameter
    and create list with the words(multiple strings)  ,
    here white space acts as default separtor
    """
    counts = {}
    words = str.split()
   
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts 
counted_words=(word_counter(content))

sorted_word=sorted(counted_words.items(),key=operator.itemgetter(1))  # Sorting dictionary based on  values

sorted_dict=dict(sorted_word)                                         # converting list to dictionary
no_words=len(list(content.split()))
file_W.write(f"No of words in file is --> {no_words} \n ")



for keys,values in reversed(sorted_dict.items()):                     
   counters=(f"{keys}  ---> {values} \n ")                              # each word and how many times word is repeating
   file_W.write(counters)                                               

