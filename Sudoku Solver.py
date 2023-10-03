#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysudoku as sud
def print_sudoku(x):
     for row in range(9):
        for column in range(9):
            print(x[row][column],end=' ')
        print()
def user_sudoku():
    sudoku1=[]
    flag=0
    for i in range(9):
        a=[]
        for j in range(9):
            num=int(input('Enter Number:'))
            if(num>=0 and num<=9):
                a.append(num)
            else:
                print("Invalid Input!!!")
                flag=1
                break
        if(flag==0):
            sudoku1.append(a)
        else:
            break
    return sudoku1
print('----WELCOME TO SUDOKU---')
print()
print()
print('Choose a Sudoku DIfficulty=>')
print('Press 1 For User Input Sudoku')
print('Press 2 For Easy Sudoku')
print('Press 3 For Medium Sudoku')
print('Press 4 For Hard Sudoku')
print()
print()
ch=int(input("Enter Choice:"))
if(ch==1):
    sdk=user_sudoku()

elif(ch==2):
    sdk=sud.easy()


elif(ch==3):
    sdk=sud.medium()

elif(ch==4):
    sdk=sud.hard()

else:
    print()
    print("Invalid Choice!!!")
print()
print()
print("Chosen Sudoku is:")
print_sudoku(sdk)
def possible(row, column, number):
    global sdk
    for i in range(9):
        if sdk[row][i] == number:
            return False

    for i in range(0,9):
        if sdk[i][column] == number:
            return False

    x = (row // 3) * 3
    y = (column // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if sdk[x+i][y+j] == number:
                return False
    return True
def solve():
    global sdk
    for r in range(9):
        for c in range(9):
            if sdk[r][c] == 0:
                for number in range(1,10):
                    if possible(r, c, number):
                        sdk[r][c] = number
                        solve()
                        sdk[r][c] = 0
                return
    print()
    print()
    print('Solved Sudoku is:')
    print_sudoku(sdk)
solve()

