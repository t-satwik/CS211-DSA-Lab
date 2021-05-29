import random

if __name__ == '__main__':
    n=int(input())                              #number of factories
    ranges = [int(a) for a in input().split()]  #ranges of factories
    w ,h = (int(a) for a in input().split())    #width and height
    discontent=[]                               #main 2D array with discontent            
    
    for i in range(h):
        row_discontent = [int(d) for d in input().split()]	#taking discontent of each row 
        discontent.append(row_discontent)			#appending the the row discontent to the main discontent 2d array
    

    lfacts = []							#list of factory coordinates
    
    for i in range(n):						#acquirng the coordinates and storing them into the list
        flag=1
        while(flag==1):						
            p = [random.randint(0, w-1), random.randint(0, h-1)]	
            if p in lfacts:
                flag=1
            else:
                lfacts.append(p)
                flag=0

    for a in lfacts:						#printing the coordinates
        print("{} {}".format(a[1], a[0]))
