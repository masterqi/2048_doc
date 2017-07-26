import random


def show_table(table):
    for i in range(4):
        print '%4d,%4d,%4d,%4d' % (table[i][0],table[i][1],table[i][2],table[i][3])


def up_table(table):
    for i in range(4):
        if table[0][i] == table[1][i] == table[2][i] == table[3][i] == 0:
            pass
        else:
            for j in range(3):
                times = 0
                while (table[j][i] == 0):
                    z = 0
                    while ((z + j) < 3):
                        table[z + j][i] = table[z + 1 + j][i]
                        z = z + 1
                    table[3][i] = 0
                    times = times + 1
                    if times > 3:
                        break
                    # show_table(table)
                if table[j][i] == table[j + 1][i]:
                    table[j][i] = table[j][i] * 2
                    z = 1
                    while ((z + j) < 3):
                        table[z + j][i] = table[z + j + 1][i]
                        z = z + 1
                    table[3][i] = 0
                else:
                    pass
    return table
    
def down_table(table):
    for i in range(4):
        if table[0][i] == table[1][i] == table[2][i] == table[3][i] == 0:
            pass
        else:
            for j in range(3):
                times = 0
                while (table[3 - j][i] == 0):
                    z = 0
                    while ((z + j) < 3):
                        table[3 - j - z][i] = table[2 - j - z][i]
                        z = z + 1
                    table[0][i] = 0
                    times = times + 1
                    if times > 3:
                        break
                    # show_table(table)
                if table[3 - j][i] == table[2 - j][i]:
                    table[3 - j][i] = table[3 - j][i] * 2
                    z = 1
                    while ((z + j) < 3):
                        table[3 - z - j][i] = table[2 - z - j][i]
                        z = z + 1
                    table[0][i] = 0
                else:
                    pass
    return table

def right_table(table):
    for i in range(4):
        if table[i][0] == table[i][1] == table[i][2] == table[i][3] == 0:
            pass
        else:
            for j in range(3):
                times = 0
                while (table[i][3 - j] == 0):
                    z = 0
                    while ((z + j) < 3):
                        table[i][3 - j - z] = table[i][2 - j - z]
                        z = z + 1
                    table[i][0] = 0
                    times = times + 1
                    if times > 3:
                        break
                    # show_table(table)
                if table[i][3 -j] == table[i][2 - j]:
                    table[i][3 - j] = table[i][3 - j] * 2
                    z = 1
                    while ((z + j) < 3):
                        table[i][3 - z - j] = table[i][2 - z - j]
                        z = z + 1
                    table[i][0] = 0
                else:
                    pass
    return table

def left_table(table):
    for i in range(4):
        if table[i][0] == table[i][1] == table[i][2] == table[i][3] == 0:
            pass
        else:
            for j in range(3):
                times = 0
                while (table[i][j] == 0):
                    z = 0
                    while ((z + j) < 3):
                        table[i][z + j] = table[i][z + j + 1]
                        z = z + 1
                    table[i][3] = 0
                    times = times + 1
                    if times > 3:
                        break
                    #show_table(table)
                if table[i][j] == table[i][j + 1]:
                    table[i][j] = table[i][j] * 2
                    z = 1
                    while ((z + j) < 3):
                        table[i][z + j] = table[i][z + j + 1]
                        z = z + 1
                    table[i][3] = 0
                else:
                    pass
    return table

def make_table(table_value, table):
    rand_value = random.randint(1, 2) * 2
    if table_value == 1:
        table_make = up_table(table)
    elif table_value == 2:
        table_make = down_table(table)
    elif table_value == 3:
        table_make = left_table(table)
    else:
        table_make = right_table(table)
    for i in range(4):
        for j in range(4):
            if table_make[i][j] == 0:
                rand_table = 1
                break
            else:
                rand_table = 0
        if rand_table == 1:
            # print rand_table , i, j
            break
    while rand_table:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if table_make[x][y] == 0:
            table_make[x][y] = rand_value
            rand_table = 0
        else:
            rand_table = rand_table + 1   
    return table_make

table_1 = [[0,2,2,0],[0,2,0,0],[2,0,0,0],[2,0,0,0]]
table_2 = [[0,0,0,2],[0,0,0,2],[0,0,0,0],[0,0,0,0]]
a = random.randint(1, 2)
if a == 1:
    table = table_1
else:
    table = table_2
while True:
    show_table(table)
    print '1:up,2:down,3:left,4:right','\n'
    table_value = raw_input('input your choose:')
    try:
        table_value = int(table_value)
        if table_value in (1,2,3,4):
            table = make_table(table_value, table)
        else:
            print 'the number must be (1,2,3,4)','\n'
    except Exception, e:
        print 'the input must be number!','\n'
        print '%s' % e
