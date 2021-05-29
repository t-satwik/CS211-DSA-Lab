#I have watched a youtube video on hash table implementation

def ascii_sum(word):                    #This function gives sum of ascii values of each charecter
    sum=0
    for achar in word:
        sum+=ord(achar)
    return sum

def hash_function(word, m):             #this is the returns the index value and is given in the question
    return (ascii_sum(word)%m)

def anagrams(query):                    #this returns a list of nagrams of the word
    anagram_lst=[]
    index = hash_function(query, m)
    for word in hash_table[index]:
        if (sorted(word) == sorted(query)):     #if two words are permutations of each other then their sorted strings will be same
            anagram_lst.append(word)
    return anagram_lst


if __name__ == "__main__": 
    import sys

    words_filename = sys.argv[1]                        #using sys for command line arguements
    m=int(sys.argv[2])                                  #size of hash table
    query_filename =  sys.argv[3]
    

    words_ptr = open(words_filename, "r")               #opening files
    query_ptr = open(query_filename, "r")
    output_ptr = open("anagrams.txt", "w")
                               
    hash_table=[]                                       #main has table list

    for i in range(m):                                  #creating m rows/m empty lists in the main table  
        hash_table.append([])

    for word in words_ptr:                              #adding all the keys to the table
        index=hash_function(word.strip(), m)
        hash_table[index].append(word.strip())
    
    queries_lst=query_ptr.readlines()                   #taking a list of all the query words
    for i in range(len(queries_lst)-1):                 
        query=queries_lst[i]
        anagram_lst = anagrams(query.strip())           #calling anagrams, to get list of anagrams for the given word 
        anagram_lst.reverse()                           #since i appended the words to the list, instead of adding at the beginning, the anagrams list is exact opposite of what is required
        if(len(anagram_lst) == 0):                      #if there is no anagram the print an empty line
            output_ptr.write("\n")
            
        else:                                           #printing the anagrams 
            for anagram in anagram_lst:
                if(anagram != anagram_lst[-1]):
                    output_ptr.write("{} ".format(anagram))
                else:
                    output_ptr.write("{}\n".format(anagram))
    
    query=queries_lst[len(queries_lst)-1]              #printing the last query without a straight line
    anagram_lst = anagrams(query.strip())
    anagram_lst.reverse()
    if(len(anagram_lst) == 0):
        output_ptr.write("")
            
    else:
        for anagram in anagram_lst:
            if(anagram != anagram_lst[-1]):
                output_ptr.write("{} ".format(anagram))
            else:
                output_ptr.write("{}".format(anagram))
            
        
    
                
