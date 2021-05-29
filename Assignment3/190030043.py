def key(num, i):            #this function returns the value in the ith digit of the num
    num=num//(10**(i-1))
    return num%10



def counting_sort(input_arr, digit):    #Counting sort is defined as given in the lecture video, except that it takes a digit parameter
    L=[]                                #This function sorts the given numbers based on its value in the given digit index
    for _ in range(10):                 #each number will be sent into the one of the 10 places(since there are 10 possible digits)
        L.append([])

    for elem in input_arr: 
        (L[key(elem, digit)]).append(elem)

    output=[]
    for elem in L:
        output.extend(elem)
    return(output)

def radix_sort(input_arr, max_digits):      #this takes two inputs, max_digits and input arr
    output=input_arr[:]                        
    for i in range(1, max_digits+1):        #i goes from 1 to the max number of digits. 
        output=counting_sort(output, i)     #for each sorting of counting sort for digits, we update the output list
    return output                           #once we are done sorting by all the digits, we return the output
    

import sys


filename=sys.argv[1]                        #taking command line arguements
max_digits=int(sys.argv[2])                 
file_ptr=open(filename, 'r')                #opening the input file
lst=[]
for elem in file_ptr.readlines():
    lst.append(int(elem.strip()))           #converting numbers to int and stiping to remove newline charecter and appending to lst

sorted_lst=radix_sort(lst, max_digits)      #storing sorted lst

write_ptr=open('radix.txt', 'w')            #opening output file with radix.txt name
for num in sorted_lst[:len(sorted_lst)-1]:
    write_ptr.write("{}\n".format(num))     #writing numbers into output file
write_ptr.write("{}".format(sorted_lst[-1]))

