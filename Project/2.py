def calculate(x, y, discontent, rangel):
    sum=0
    for i in range(x-rangel,x+rangel+1):
        for j in range(y-rangel,y+rangel+1):
            if i>=0 and j>=0 and i<=w-1 and j<=h-1 and ((x-i)**2+(y-j)**2)<=rangel**2:
                # print(i,j)
                sum+=discontent[j][i]
                #print(f"{i} {j} {discontent[i][j]}\n")
    return sum  

# def check(x, y, a, b, r):
#     return (x-a)**2 + (y-b)**2 - r**2

# def New_calculate(a, b, disc, r):
#     sum=0
#     for x in range(w):
#         for y in range(h):
#             if check(x, y, a, b, r)<=0:
#                 sum+=disc[y][x]
#                 # print(x, y)
                
#     return sum

# def tp_func(discontent):
#     for i in range(w):
#         for j in range(h):
#             print(discontent[j][i])



    
import random
if __name__ == '__main__':
    
    n=int(input()) 
    ranges = [int(a) for a in input().split()]  

    fact_list=[]     
    for i in range(n):                                          
        fact_list.append([i, ranges[i]])

    fact_list.sort(key=lambda fact:fact[1], reverse=True) 
    # print(fact_list)

    # fact={}
    # for i in range(n):
    #     fact[i]=ranges[i]  #ranges of factories

    w ,h = (int(a) for a in input().split())    #width and height
    discontent=[]                                            #main 2D array with discontent            

    for i in range(h):                  
        row_discontent = [int(d) for d in input().split()]
        discontent.append(row_discontent)

    # sorted_fact={k: v for k,v in sorted(fact.items(),key=lambda item:item[1], reverse=True)}
    # print(sorted_fact)

    
    corners=[[0,0],[w-1,0],[0,h-1],[w-1,h-1]]
    
    coord_lst=[]
    
    #print(calculate(0, 0, discontent, 980))
    
    for i in range(4):
        maxi, temp_x, temp_y =0, 0, 0
        for corner in corners:
            if corner not in coord_lst:
                d=calculate(corner[0], corner[1], discontent, fact_list[i][1])
                if(d>maxi):
                    maxi=d
                    temp_x=corner[0]
                    temp_y=corner[1]
        coord_lst.append([temp_x, temp_y])

    for i in range(n-4):
        flag=1
        while(flag==1):
            p = [random.randint(0, w-1), random.randint(0, h-1)]
            if p in coord_lst:
                flag=1
            else:
                coord_lst.append(p)
                flag=0

    for i in range(4):
        temp=coord_lst[i]
        coord_lst[i] = coord_lst[fact_list[i][0]]
        coord_lst[fact_list[i][0]]=temp
    
    
    for coord in coord_lst:
        print("{} {}".format( coord[1], coord[0]))
    
    # print(list(sorted_fact.values()))

    # print(New_calculate(0, 0, discontent, 980))
    # print(tp_func(discontent))tp_func 1732396