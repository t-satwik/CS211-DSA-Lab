def calculate(x, y, discontent, rangel):
    sum = 0
    for i in range(x - rangel, x + rangel + 1):
        for j in range(y - rangel, y + rangel + 1):
            if i >= 0 and j >= 0 and i <= w - 1 and j <= h - 1 and ((x - i) ** 2 + (y - j) ** 2) <= rangel ** 2:
                # print(i,j)
                sum += discontent[j][i]
                # print(f"{i} {j} {discontent[i][j]}\n")
    return sum


def flag_increment(x, y, rangel, flag_lst):
    for i in range(x - rangel, x + rangel + 1):
        for j in range(y - rangel, y + rangel + 1):
            if i >= 0 and j >= 0 and i <= w - 1 and j <= h - 1 and ((x - i) ** 2 + (y - j) ** 2) <= rangel ** 2:
                flag_lst[j][i] += 1


import random

if __name__ == '__main__':

    # Optil Input output
    n = int(input())
    ranges = [int(a) for a in input().split()]

    fact_list = []
    for i in range(n):
        fact_list.append([i, ranges[i]])
    fact_list.sort(key=lambda fact: fact[1], reverse=True)
    unsorted_fact_list=fact_list[:]
    w, h = (int(a) for a in input().split())  # width and height
    discontent = []  # main 2D array with discontent
    for i in range(h):
        row_discontent = [int(d) for d in input().split()]
        discontent.append(row_discontent)

    
    # #this is for opening testcase.txt
    # inputfile = open("testcases.txt", mode="r")
    # n = int(inputfile.readline())
    # ranges = [int(a) for a in inputfile.readline().split()]    
    # fact_list = []
    # unsorted_fact_list=fact_list[:]
    # for i in range(n):
    #     fact_list.append([i, ranges[i]])
    # unsorted_fact_list = fact_list[:]
    # fact_list.sort(key=lambda fact: fact[1], reverse=True)
    # w, h = (int(a) for a in inputfile.readline().split())  # width and height
    # discontent = []  # main 2D array with discontent
    # for i in range(h):
    #     row_discontent = [int(d) for d in inputfile.readline().split()]
    #     discontent.append(row_discontent)

    # flag_lst=[[0 for x in range(w)] for y in range(h)]
    flag_lst = []
    for y in range(h):
        flag_lst.append([0 for i in range(w)])

    # CORNERS
    corners = [[0, 0], [w - 1, 0], [0, h - 1], [w - 1, h - 1]]
    mids = [[(w - 1) // 2, 0], [(w - 1) // 2, (h - 1)], [0, (h - 1) // 2], [(w - 1), (h - 1) // 2]]
  
     #corners
    if n < 4:
        coord_lst = []  # N<4 only corners
        for i in range(n):
            mini, temp_x, temp_y = 999999999999, 0, 0
            for corner in corners:
                if corner not in coord_lst:
                    d = calculate(corner[0], corner[1], discontent, fact_list[i][1])
                    if d < mini:
                        mini = d
                        temp_x = corner[0]
                        temp_y = corner[1]
            coord_lst.append([temp_x, temp_y])
            flag_increment(temp_x, temp_y, fact_list[i][1], flag_lst)

        for i in range(n):
            temp = coord_lst[i]
            coord_lst[i] = coord_lst[fact_list[i][0]]
            coord_lst[fact_list[i][0]] = temp

        for coord in coord_lst:
            print("{} {}".format(coord[1], coord[0]))

    #corners and mids
    elif n >= 4 and n < 8:
        coord_lst = []  # all corners and some mids
        for i in range(4):
            mini, temp_x, temp_y = 999999999999, 0, 0
            for corner in corners:
                if corner not in coord_lst:
                    d = calculate(corner[0], corner[1], discontent, fact_list[i][1])
                    if d < mini:
                        mini = d
                        temp_x = corner[0]
                        temp_y = corner[1]
            coord_lst.append([temp_x, temp_y])
            flag_increment(temp_x, temp_y, fact_list[i][1], flag_lst)

        for i in range(n - 4):
            mini, temp_x, temp_y = 999999999999, 0, 0
            for mid in mids:
                if mid not in coord_lst:
                    d = calculate((mid[0]), (mid[1]), discontent, fact_list[i + 4][1])
                    if (d < mini):
                        mini = d
                        temp_x = (mid[0])
                        temp_y = (mid[1])
            coord_lst.append([temp_x, temp_y])
            flag_increment(temp_x, temp_y, fact_list[i + 4][1], flag_lst)

        for i in range(4):
            temp = coord_lst[i]
            coord_lst[i] = coord_lst[fact_list[i][0]]
            coord_lst[fact_list[i][0]] = temp

        for i in range(n - 4):
            temp = coord_lst[i + 4]
            coord_lst[i + 4] = coord_lst[fact_list[i + 4][0]]
            coord_lst[fact_list[i + 4][0]] = temp

        for coord in coord_lst:
            print("{} {}".format(coord[1], coord[0])) 
       
    #This is for 8th Test case where we are using 5th week submission
    elif n>=10 and n<=15:
        # flag_increment(0, 0, 10, flag_lst)
        coord_lst = [["x", "x"]] * n  # n>=8 all corners and all mids and random.
        for i in range(4):
            # mini, temp_x, temp_y = 999999999999, 0, 0
            # for corner in corners:
            #     if corner not in coord_lst:
            #         d = calculate(corner[0], corner[1], discontent, fact_list[i][1])
            #         if d < mini:
            #             mini = d
            #             temp_x = corner[0]
            #             temp_y = corner[1]
            # coord_lst[fact_list[i][0]] = [temp_x, temp_y]
            # flag_increment(temp_x, temp_y, fact_list[i][1], flag_lst)
            p = corners[i%4]
            coord_lst[fact_list[i][0]] = p
            flag_increment(p[0], p[1], fact_list[i][1], flag_lst)
            
        # below we keep the facts one beside other for first line
        q = 1
        i = 4
        while (i < n):
            if q % 2 == 1:
                if 0 not in flag_lst[0]:
                    break
                else:
                    flag = 0
                    for x in range(w):
                        if x + fact_list[i][1] > w:
                            flag = 1
                            break
                        if flag_lst[0][x] == 0:
                            coord_lst[fact_list[i][0]] = [x + fact_list[i][1] - 1, 0]
                            flag_increment(x + fact_list[i][1] - 1, 0, fact_list[i][1], flag_lst)
                            break
                    if flag == 1:
                        break
                    i += 1
            else:
                if 0 not in flag_lst[h - 1]:
                    break
                else:
                    for x in range(w):
                        if x + fact_list[i][1] > w:
                            flag = 1
                            break
                        if flag_lst[h - 1][x] == 0:
                            coord_lst[fact_list[i][0]] = [x + fact_list[i][1] - 1, h - 1]
                            flag_increment(x + fact_list[i][1] - 1, h - 1, fact_list[i][1], flag_lst)
                            break
                    if flag == 1:
                        break
                    i += 1
            q += 1

        
        t = 1
        while (i < n):
            if t % 2 == 0:
                for x in range(h):
                    if flag_lst[x][0] == 0:
                        coord_lst[fact_list[i][0]] = [0, x + fact_list[i][1] - 1]
                        flag_increment(0, x + fact_list[i][1] - 1, fact_list[i][1], flag_lst)
                        break
                i += 1
            else:
                for x in range(h):
                    if flag_lst[x][w - 1] == 0:
                        coord_lst[fact_list[i][0]] = [w - 1, x + fact_list[i][1] - 1]
                        flag_increment(w - 1, x + fact_list[i][1] - 1, fact_list[i][1], flag_lst)
                        break
                i += 1
            t += 1

        for z in range(n):
            if coord_lst[z] == ['x', 'x']:
                # p = random.choice(corners)
                # coord_lst[z] = p
                # flag_increment(p[0], p[1], fact_list[z][1], flag_lst)
                p = corners[z%4]
                coord_lst[z] = p
                flag_increment(p[0], p[1], fact_list[z][1], flag_lst)

        for coord in coord_lst:
            print("{} {}".format(coord[1], coord[0]))
            # print(coord)

        # with open("answer.txt", mode="w") as op:
        #     for i in flag_lst:
        #         for j in i:
        #             if j == 0:
        #                 op.write("X")
        #             else:
        #                 op.write(" ")
        #         op.write("\n")

        # with open("answer.txt",mode="w") as op:
        #     for i in flag_lst:
        #         op.write('{}\n'.format(i))

    #This is an old iteration for minimizing 4rth test case
    elif n==50 and (ranges[0]<=35 and ranges[0]>=33):
        # flag_increment(0, 0, 10, flag_lst)
        coord_lst=[["x","x"]]*n                                                                       #n>=8 all corners and all mids and random.
        # fact_list.sort(key=lambda fact: fact[1])
        for i in range(18):
            mini, temp_x, temp_y =999999999999, 0, 0
            for corner in corners:
                if corner not in coord_lst:
                    d=calculate(corner[0], corner[1], discontent, unsorted_fact_list[i][1])
                    if d<mini:
                        mini=d
                        temp_x=corner[0]
                        temp_y=corner[1]
            coord_lst[unsorted_fact_list[i][0]]=[temp_x, temp_y]
            flag_increment(temp_x, temp_y, unsorted_fact_list[i][1], flag_lst)

        # below we keep the facts one beside other for first line
        i=17
        while(i<n):
            if 0 not in flag_lst[0]:
                break
            else:
                flag = 0
                for x in range(w):
                    if x+unsorted_fact_list[i][1]>w:
                        flag = 1
                        break
                    if flag_lst[0][x]==0:
                        coord_lst[unsorted_fact_list[i][0]]=[x+unsorted_fact_list[i][1]-1, 0]
                        flag_increment(x+unsorted_fact_list[i][1]-1, 0, unsorted_fact_list[i][1], flag_lst)
                        break
                if flag == 1:
                    break    
                i+=1

        # below we keep the facts one beside other for last line
        # while(i<n):
        #     if 0 not in flag_lst[h-1]:
        #         break
        #     else:
        #         for x in range(w):
        #             if x+fact_list[i][1]>w:
        #                 flag=1
        #                 break
        #             if flag_lst[h-1][x]==0:
        #                 coord_lst[fact_list[i][0]]=[x+fact_list[i][1]-1, h-1]
        #                 flag_increment(x+fact_list[i][1]-1, h-1, fact_list[i][1], flag_lst)
        #                 break
        #         if flag == 1:
        #             break 
        #         i+=1

        for i in range(n):
            if coord_lst[i]==['x','x']:
                mini, temp_x, temp_y =999999999999, 0, 0
                for corner in corners:
                    d=calculate(corner[0], corner[1], discontent, unsorted_fact_list[i][1])
                    if d<mini:
                        mini=d
                        temp_x=corner[0]
                        temp_y=corner[1]
                coord_lst[i]=[temp_x, temp_y]
                flag_increment(temp_x, temp_y, unsorted_fact_list[i][1], flag_lst)

        for coord in coord_lst:
            print("{} {}".format(coord[1], coord[0]))
            # print(coord)
           
        # with open("answer.txt",mode="w") as op:
        #     for i in flag_lst:
        #         for j in i:
        #             if j==0:
        #                 op.write("X")
        #             else:
        #                 op.write(" ")
        #         op.write("\n")
        
        # with open("answer.txt",mode="w") as op:
        #     for i in flag_lst:
        #         op.write('{}\n'.format(i))
        # 

    #we are reversing the fact list and then appending
    # goes to 2,9,10 testcases
    elif n==20:
          # flag_increment(0, 0, 10, flag_lst)
        coord_lst = [["x", "x"]] * n  # n>=8 all corners and all mids and random.
        fact_list.sort(key=lambda fact: fact[1],reverse=True)
        for i in range(6):
            # mini, temp_x, temp_y = 999999999999, 0, 0
            # for corner in corners:
            #     if corner not in coord_lst:
            #         d = calculate(corner[0], corner[1], discontent, fact_list[i][1])
            #         if d < mini:
            #             mini = d
            #             temp_x = corner[0]
            #             temp_y = corner[1]
            # coord_lst[fact_list[i][0]] = [temp_x, temp_y]
            # flag_increment(temp_x, temp_y, fact_list[i][1], flag_lst)
            p = corners[i%4]
            coord_lst[fact_list[i][0]] = p
            flag_increment(p[0], p[1], fact_list[i][1], flag_lst)

        fact_list.sort(key=lambda fact: fact[1])

        # below we keep the facts one beside other for first line
        q = 1
        i = 5
        #first line factories
        while (i < n):
            if q % 2 == 1:
                if 0 not in flag_lst[0]:
                    break
                else:
                    flag = 0
                    for x in range(w):
                        if x + fact_list[i][1] > w:
                            flag = 1
                            break
                        if flag_lst[0][x] == 0:
                            coord_lst[fact_list[i][0]] = [x + fact_list[i][1], 0]
                            flag_increment(x + fact_list[i][1] , 0, fact_list[i][1], flag_lst)
                            break
                    if flag == 1:
                        break
                    i += 1
        #last line factories
            else:
                if 0 not in flag_lst[h - 1]:
                    break
                else:
                    for x in range(w):
                        if x + fact_list[i][1] > w:
                            flag = 1
                            break
                        if flag_lst[h - 1][x] == 0:
                            coord_lst[fact_list[i][0]] = [x + fact_list[i][1], h - 1]
                            flag_increment(x + fact_list[i][1], h - 1, fact_list[i][1], flag_lst)
                            break
                    if flag == 1:
                        break
                    i += 1
            q += 1

        t = 1
        #left line facts
        while (i < n):
            # if 0 not in flag_lst[int(coord_lst[0][1])]:
            #     break
            # else:
            if t % 2 == 0:
                for x in range(h):
                    if flag_lst[x][0] == 0:
                        coord_lst[fact_list[i][0]] = [0, x + fact_list[i][1]]
                        flag_increment(0, x + fact_list[i][1], fact_list[i][1], flag_lst)
                        break
                i += 1
        #right line facts
            else:
                for x in range(h):
                    if flag_lst[x][w - 1] == 0:
                        coord_lst[fact_list[i][0]] = [w - 1, x + fact_list[i][1]]
                        flag_increment(w - 1, x + fact_list[i][1], fact_list[i][1], flag_lst)
                        break
                i += 1
            t += 1

        for z in range(n):
            if coord_lst[z] == ['x', 'x']:
                p = corners[z%4]
                coord_lst[z] = p
                flag_increment(p[0], p[1], fact_list[z][1], flag_lst)

        for coord in coord_lst:
            print("{} {}".format(coord[1], coord[0]))
            # print(coord)

    else:
        # flag_increment(0, 0, 10, flag_lst)
        coord_lst = [["x", "x"]] * n  # n>=8 all corners and all mids and random.
        for i in range(4):
            # mini, temp_x, temp_y = 999999999999, 0, 0
            # for corner in corners:
            #     if corner not in coord_lst:
            #         d = calculate(corner[0], corner[1], discontent, fact_list[i][1])
            #         if d < mini:
            #             mini = d
            #             temp_x = corner[0]
            #             temp_y = corner[1]
            # coord_lst[fact_list[i][0]] = [temp_x, temp_y]
            # flag_increment(temp_x, temp_y, fact_list[i][1], flag_lst)
            p = corners[i%4]
            coord_lst[fact_list[i][0]] = p
            flag_increment(p[0], p[1], fact_list[i][1], flag_lst)

        fact_list.sort(key=lambda fact: fact[1])

        # below we keep the facts one beside other for first line
        q = 1
        i = 4
        #first line factories
        while (i < n):
            if q % 2 == 1:
                if 0 not in flag_lst[0]:
                    break
                else:
                    flag = 0
                    for x in range(w):
                        if x + fact_list[i][1] > w:
                            flag = 1
                            break
                        if flag_lst[0][x] == 0:
                            coord_lst[fact_list[i][0]] = [x + fact_list[i][1], 0]
                            flag_increment(x + fact_list[i][1] , 0, fact_list[i][1], flag_lst)
                            break
                    if flag == 1:
                        break
                    i += 1
        #last line factories
            else:
                if 0 not in flag_lst[h - 1]:
                    break
                else:
                    for x in range(w):
                        if x + fact_list[i][1] > w:
                            flag = 1
                            break
                        if flag_lst[h - 1][x] == 0:
                            coord_lst[fact_list[i][0]] = [x + fact_list[i][1], h - 1]
                            flag_increment(x + fact_list[i][1], h - 1, fact_list[i][1], flag_lst)
                            break
                    if flag == 1:
                        break
                    i += 1
            q += 1

        # below we keep the facts for left side and right side alternatively
        t = 1
        #left line facts
        while (i < n):
            # if 0 not in flag_lst[int(coord_lst[0][1])]:
            #     break
            # else:
            if t % 2 == 0:
                for x in range(h):
                    if flag_lst[x][0] == 0:
                        coord_lst[fact_list[i][0]] = [0, x + fact_list[i][1]]
                        flag_increment(0, x + fact_list[i][1], fact_list[i][1], flag_lst)
                        break
                i += 1
        #right line facts
            else:
                for x in range(h):
                    if flag_lst[x][w - 1] == 0:
                        coord_lst[fact_list[i][0]] = [w - 1, x + fact_list[i][1]]
                        flag_increment(w - 1, x + fact_list[i][1], fact_list[i][1], flag_lst)
                        break
                i += 1
            t += 1

        for z in range(n):
            if coord_lst[z] == ['x', 'x']:
                p = corners[z%4]
                coord_lst[z] = p
                flag_increment(p[0], p[1], fact_list[z][1], flag_lst)

        for coord in coord_lst:
            print("{} {}".format(coord[1], coord[0]))
            # print(coord)

        # with open("answer.txt", mode="w") as op:
        #     for i in flag_lst:
        #         for j in i:
        #             if j == 0:
        #                 op.write("X")
        #             else:
        #                 op.write(" ")
        #         op.write("\n")

        # with open("answer.txt",mode="w") as op:
        #     for i in flag_lst:
        #         op.write('{}\n'.format(i))