
import sys
if __name__=="__main__":
    file_ptr=open(sys.argv[1], "r")         #Openeing the input file
    write_ptr=open("sd.txt", "w")           #opening the write file
    temp_lst=file_ptr.readlines()      
    n, m = temp_lst[0].strip().split()      #n and m are the number of vertices and eges respectively
    n=int(n)
    m=int(m)
    
    adj=[]                                  #adjacency list
    for i in range(n):                      #Appending n emty lists to the adjacency list(one for each vertex) 
        adj.append([])

    for str in temp_lst[1:]:               #iterating through each given edge
        num1, num2 = str.strip().split()   
        adj[int(num1)].append(int(num2))    #Since the given graph is undirected, there is relation from both sides
        adj[int(num2)].append(int(num1))    #and hence we have to append the value into both the lists.
    
    # print(adj)

    #I have implemented the code which was explained in the 
    s=0                                         #since we are finding distance from vertex 0, s=0                   
    level={s: 0}                                #Initializing, with level of 0 vertex as 0
    parent={s: None}                            #and there is no parent for vertex 0
    i=1                                         #this stores the level number
    frontier=[s]                                #this list stores the immediate neighbours of 0 vertex, initially
    while frontier:                             #we need to loop until there is no elements in frontier, i.e end of the graph
        next=[]                                 #This store the neighbours of u which are not visited already
        for u in frontier:                      #for each neighbour(u)
            for v in adj[u]:                    #for each neghbour(v) of u
                if v not in level:              #if v is not visited already
                    level[v]=i                  #then set the level of v as the current value of i
                    parent[v]=u                 #and parent of v as u
                    next.append(v)              #and append it to next

        frontier=next                           #frontier=next
        i+=1                                    #current level increases.

    #Shortest Distance between a point and base vertex is the level[vertex] if it exists,
    #otherwise there is no path hence distance is infinty(We jeed to print(-1)).
    for i in range(n):                     #For each vertex 
        if i in level.keys():                   #if vertex is in level list(i.e it has a level)
            write_ptr.write("{}\n".format(level[i]))          #shortest distance is same as the level number.
        else:                                   #if vertex doesnt have a level, then there is no path 
            write_ptr.write("-1\n")             #hence we print -1.
    

