def relax(e, d, p):
    if d[e['v']] > d[e['u']] + e['w']:
        d[e['v']] = d[e['u']] + e['w']
        p[e['v']] = e['u']

import sys
if __name__=="__main__":
    file_ptr=open(sys.argv[1], "r")         #Openeing the input file
    # file_ptr=open("input2.graph", "r")         #Openeing the input file
    write_ptr=open("sd.txt", "w")           #opening the write file
    temp_lst=file_ptr.readlines()      
    n, m = temp_lst[0].strip().split()      #n and m are the number of vertices and edges respectively
    n=int(n)
    m=int(m)
    V=[i for i in range(n)]                 #List of all vertices
    d=[float('inf')  for i in range(n)]     #initializing all the distances to inf
    p=[None for i in range(n)]              #initializing the parent list to None
    d[0]=0                                  #setting the distance of source vertex to 0
    E=[]                                    #This list contains all the edge, where each edge is a dict having u, v, w as keys

    for temp_str in temp_lst[1:]:          #taking the input from the file
        u, v, w=temp_str.strip().split()
        dic={'u':int(u), 'v':int(v), 'w':int(w)}
        E.append(dic)
        
    # I have implemted the pseudo code which was explained
    # in the lecture by prof. Srini devdas

    for i in range(1, n):       #relaxing each edge             
        for e in E:
            relax(e, d, p)

    for e in E:                              # if any edge can be further relaxed even after the above step, 
        if d[e['v']]>d[e['u']]+e['w']:       #then there is a negative cycle
            d[e['v']]=float('-inf')          #fixing the distance from source to to this v as -inf
            for vertex in V:                 #then we check if a vertex is a child of this v
                if e['v']==p[vertex]:        #If this is a child then
                    d[vertex]=float('-inf')  #then we set its distance also to be -inf
    
    #Suppose a->b->c->a is a negative cycle 
    #then we set a, b to be -inf in first iteration
    #then we set b, c to be -inf, then c, a.
    #in this way all the elements in cycle are set as -inf

    for i in range(n-1):                    #writing the distance to the sd.txt
        if d[i]==float('inf'):
            d[i]="+inf"
        write_ptr.write("{} {}\n".format(i, d[i]))
    write_ptr.write("{} {}\n".format(n-1, d[n-1]))
    