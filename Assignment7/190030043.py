# I have implemented the code, explained int he video lecture.
# we store the order in which in we visit the vertices and
# then reverse it to get the topological sort.

import sys

def dfs_visit(adj, s, parent, order):           #dfs visit as explained in the lecture
    for v in adj[s]:
        if v not in parent.keys():
            parent[v]=s
            dfs_visit(adj, v, parent, order)
    order.append(s)                             #when the recursion completes we append the vertex tot he order list

if __name__=="__main__":
    file_ptr=open(sys.argv[1], "r")         #Openeing the input file
    # file_ptr=open("custom.graph", "r")         #Openeing the input file
    write_ptr=open("ts.txt", "w")           #opening the write file
    temp_lst=file_ptr.readlines()      
    n, m = temp_lst[0].strip().split()      #n and m are the number of vertices and edges respectively
    n=int(n)
    m=int(m)
    
    vertices=range(int(n))                  #list of all the vertices
    adj=[]                                  #adjacency list
    for i in range(n):                      #Appending n emty lists to the adjacency list(one for each vertex) 
        adj.append([])

    for str in temp_lst[1:]:               #iterating through each given edge
        num1, num2 = str.strip().split() 
        adj[int(num1)].append(int(num2))    #Since the given graph is directed, there is a relation from one side only    

    parent={}    
    order=[]                                #Initializing the order list as an empty list

    for s in vertices:                          #for each vertex in vertices
        if s not in parent:                     #if it is not in parent (unvisited)
            parent[s]=None                      #setting tis parent to be none
            dfs_visit(adj, s, parent, order)    #and visiting its neighbours
    

    order.reverse()                             #reversing the order in which they are visited, to get topological sort.
    
    for i in range(n):                          #writing them to ts.txt
        if i!=n-1:                   
            write_ptr.write("{}\n".format(order[i]))          
        else:                                  
            write_ptr.write("{}".format(order[i]))   
    