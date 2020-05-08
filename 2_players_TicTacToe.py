# -*- coding: utf-8 -*-
"""
Created on Fri May  8 21:43:52 2020

@author: Tisana
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:30:04 2019

@author: CINO
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:25:28 2019

@author: CINO
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 12:08:35 2019

@author: CINO
"""
#import library
import numpy as np
import  turtle as t
while True:
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.pensize(1)
    t.pencolor("black")
    #create initial table
    table=np.zeros((3,3))
    
    
    #draw table in turtle
    t.speed(5)
    
    t.left(180)
    t.penup()
    t.forward(100)
    t.right(90)
    t.forward(300)
    t.right(180)
    t.pendown()
    t.forward(600)
    
    t.penup()
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(600)
    t.left(180)
    t.pendown()
    t.forward(600)
    
    t.right(90)
    t.penup()
    t.forward(400)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.pendown()
    t.forward(600)
    
    t.right(90)
    t.penup()
    t.forward(200)
    t.right(90)
    t.forward(600)
    t.right(180)
    t.pendown()
    t.forward(600)
    
    
    
    
    #function that convert position number to index of row and column 
    def converter(position):
        if position==1:
            row=0
            column=0      
        elif position==2:
            row=0
            column=1
        elif position==3:
            row=0
            column=2        
        elif position==4:
            row=1
            column=0
        elif position==5:
            row=1
            column=1
        elif position==6:
            row=1
            column=2
        elif position==7:
            row=2
            column=0
        elif position==8:
            row=2
            column=1
        elif position==9:
            row=2
            column=2
        list=[row,column]
        return list
    
    
    #converter_for_turtle
    def X_position_converter_for_turtle(position):
        if position==1:
            x=-125
            y=125
        elif position==2:
            x=75
            y=125
        elif position==3:
            x=275
            y=125     
        elif position==4:
            x=-125
            y=-75
        elif position==5:
            x=75
            y=-75
        elif position==6:
            x=275
            y=-75
        elif position==7:
            x=-125
            y=-275
        elif position==8:
            x=75
            y=-275
        elif position==9:
            x=275
            y=-275
        list=[x,y]
        return list
        
    def O_position_converter_for_turtle(position):
        if position==1:
            x=-200
            y=125
        elif position==2:
            x=0
            y=125
        elif position==3:
            x=200
            y=125     
        elif position==4:
            x=-200
            y=-75
        elif position==5:
            x=0
            y=-75
        elif position==6:
            x=200
            y=-75
        elif position==7:
            x=-200
            y=-275
        elif position==8:
            x=0
            y=-275
        elif position==9:
            x=200
            y=-275
        list=[x,y]
        return list
    
    
    #draw x function
    def draw_x(position):
        import math
        t.penup()
        t.goto(position[0],position[1])
        t.pendown()
        t.left(135)
        length=math.sqrt((150**2)+(150**2))
        t.forward(length)
        t.right(135)
        t.penup()
        t.forward(150)
        t.right(135)
        t.pendown()
        t.forward(length)
        t.left(135)
    
    table=table.tolist()
    
    
    #game start
    i=1
        
        
    while True:
        
        if i==1:   
            print("Player 1 turn")
            print("Available position are : ")
            available_position_list=[[1,2,3],
                                     [4,5,6],
                                     [7,8,9]]
            
            
            for each_row in range(0,3):
                for each_column in range(0,3):
                    if table[each_row][each_column]!=0:
                        available_position_list[each_row][each_column]="-"
            
            available_position_df=np.array(available_position_list)
            print(available_position_df)
        
            human_available_position_list=[]
            for each_row in range(0,3):
                for each_column in range(0,3):
                    if available_position_list[each_row][each_column]!="-":
                        human_available_position_list.append(available_position_list[each_row][each_column])        
            while True:
                position=int(input("Selection position : "))
                if position in human_available_position_list:
                    break
            row_column_list=converter(position)
            table[row_column_list[0]][row_column_list[1]]=1
        
        elif i==2:
            print("Player 2 turn")
            print("Available position are : ")
            available_position_list=[[1,2,3],
                                     [4,5,6],
                                     [7,8,9]]
            
            
            for each_row in range(0,3):
                for each_column in range(0,3):
                    if table[each_row][each_column]!=0:
                        available_position_list[each_row][each_column]="-"
            
            available_position_df=np.array(available_position_list)
            print(available_position_df)
            
            human_available_position_list=[]
            for each_row in range(0,3):
                for each_column in range(0,3):
                    if available_position_list[each_row][each_column]!="-":
                        human_available_position_list.append(available_position_list[each_row][each_column])        
            while True:
                position=int(input("Selection position : "))
                if position in human_available_position_list:
                    break
            row_column_list=converter(position)
            table[row_column_list[0]][row_column_list[1]]=2
            
            
        #draw on turtle
        if i==1:
            #draw for player 1 (x)
            position_x_turtle=X_position_converter_for_turtle(position)
            draw_x(position_x_turtle)
    
        elif i==2:
            #draw for player 2 (o)
            position_o_turtle=O_position_converter_for_turtle(position)
            t.penup()
            t.goto(position_o_turtle)
            t.pendown()
            t.circle(75)   
        
        #check terminate condition
        
        #check for win condition
        win_position_list=[[1,4,7],
                           [2,5,8],
                           [3,6,9],
                           [1,2,3],
                           [4,5,6],
                           [7,8,9],
                           [3,5,7],
                           [1,5,9]]
        win=0
        for each_win_position in win_position_list:
            score=0
            for each_position in each_win_position:
                position=converter(each_position)
                if table[position[0]][position[1]]==i:
                    score=score+1
            if score==3:
                win_position=each_win_position
                win=1
            #print(each_win_position)
            #print(score)  
        if win==1:
            break
        print("no winner")
        
        
        #check draw condition
        draw=0
        check_available_position_list=[]
        for each_row in range(0,3):
            for each_column in range(0,3):
                if table[each_row][each_column]==0:
                    check_available_position_list.append(available_position_list[each_row][each_column])
        print(check_available_position_list)
        if len(check_available_position_list)==0:
            draw=1
            break
        print("no draw")
        
        
        #alternate player
        if i==1:
            i=2
        elif i==2:
            i=1
    
    if draw==1:
        print("________","\n")
        print("DRAW !")
        print("________")
    elif i==1:
        print("___________","\n")
        print("PLAYER 1 WIN !!!")
        print("___________")
    elif i==2:
        print("__________","\n")
        print("PLAYER 2 WIN !!!")
        print("__________")
    #draw termination animation
    if draw!=1:
        for each_win_position in win_position:
            
            
            if i==1:
                position_x_turtle=X_position_converter_for_turtle(each_win_position)
                t.speed(11)
                t.pencolor("red")
                t.pensize(10)
                draw_x(position_x_turtle)
            elif i==2:
                position_o_turtle=O_position_converter_for_turtle(each_win_position)
                t.penup()
                t.goto(position_o_turtle)
                t.pendown()
                t.pencolor("blue")
                t.pensize(10)
                t.speed(11)
                t.circle(75)          
        
    #restart option
    option=input("END GAME (Yes / No) ??")
    if option=="yes" or option=="y":
        break
    t.clear()
      
  