# -*- coding: utf-8 -*-
"""
@author: SAMUEL GANDAANUO
"""

import numpy as np
import GUI_Influence_Lines
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_tkagg import(FigureCanvasAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


"""
for influence lines two user inputs are required, the total length of the beam(Length_Of_Span) and the
length of the unit load(Length_Of_Points) from the left support (support A) whhich changes
"""
def Back_End(Length_Of_Span, Length_Of_Points):    
    Points_Along_Span = np.arange(0, Length_Of_Span+1, None)
    #Points_Along_Span = np.linspace(0, Length_Of_Span, 20) #this will generate 20 points between 0 and the total length of the beam
    Reaction_At_A = (Length_Of_Span - Points_Along_Span)/Length_Of_Span
    Reaction_At_B = Points_Along_Span/Length_Of_Span
    
    #the unit load is 1KN
    Max_Reaction_A = max(Reaction_At_A)
    print(Max_Reaction_A)
    Max_Reaction_At_B = max(Reaction_At_B)
    print(Max_Reaction_At_B)

    First_Length = np.arange(Length_Of_Points+1)
    Second_Length = np.arange(Length_Of_Points, Length_Of_Span+1)
    Distance = First_Length.tolist() + Second_Length.tolist()
    
    First_Shear_Force = -First_Length/Length_Of_Span
    Second_Shear_Force = (Length_Of_Span-Second_Length)/Length_Of_Span   
    Shear_Force_At_Y = First_Shear_Force.tolist() + Second_Shear_Force.tolist()
    """    
    alternative for writing the numpy where function
    for j in Points_Along_Span:
        if j <= Length_Of_Points:
            Bending_Moment = ((((Length_Of_Span-Points_Along_Span)/Length_Of_Span)*Length_Of_Points) - (Length_Of_Points-Points_Along_Span))
        elif j >= Length_Of_Points:
            Bending_Moment =  ((((Length_Of_Span-Points_Along_Span)/Length_Of_Span)*Length_Of_Points))
    """       
    Bending_Moment = np.where(Points_Along_Span<=Length_Of_Points, 
                              ((((Length_Of_Span-Points_Along_Span)/Length_Of_Span)*Length_Of_Points) - (Length_Of_Points-Points_Along_Span)),
                              ((((Length_Of_Span-Points_Along_Span)/Length_Of_Span)*Length_Of_Points)))
    Max_Bending_Moment = max(Bending_Moment)
    print(Max_Bending_Moment)
           
    print(f"The Bending Moment is:  {Bending_Moment} \n")
    print(f"The reaction at A is: {Reaction_At_A} \n")
    print(f"The reaction at B is: {Reaction_At_B} \n")
        
    plt.subplot(4,1,1)
    plt.plot(Points_Along_Span, Bending_Moment)
    plt.plot([0, Length_Of_Span], [0,0])
    plt.title("Influence Line for Bending Moment")
    plt.ylabel("Bending Moment")
    plt.xlabel("Distance(m)")
    
    plt.subplot(4,1,2)
    #plt.plot("Influence Line for Shear Force")
    plt.plot(Distance, Shear_Force_At_Y)  
    plt.plot([0, Length_Of_Span], [0,0])
    #plt.plot([0, Reaction_At_A], [0,0])
    plt.ylabel("Shear Force")
    plt.xlabel("Distance(m)")
    
    """
    def Second_Plot():
        plt.plot(1,1,1)
        #plt.plot("Influence Line for Reaction at A")
        plt.plot(Points_Along_Span, Reaction_At_A)
        #plt.plot([0, Length_Of_Span], [0,0])
        plt.ylabel("Reaction")
        plt.xlabel("Distance(m)")
        
        plt.plot(1,2,2)
        #plt.plot("Influence Line for Reaction at B")
        plt.plot(Points_Along_Span, Reaction_At_B)
       # plt.plot([0, Length_Of_Span], [0,0])
        plt.ylabel("Reaction")
        plt.xlabel("Distance(m)")
    Second_Plot()
    """       
    plt.subplot(4,1,3)
    #plt.plot("Influence Line for Reaction at A")
    plt.plot(Points_Along_Span, Reaction_At_A)
    plt.plot([0, Length_Of_Span], [0,0])
    plt.plot([0,0], [1,0])
    plt.ylabel("Reaction")
    plt.xlabel("Distance(m)")
    
    plt.subplot(4,1,4)
    #plt.plot("Influence Line for Reaction at B")
    plt.plot(Points_Along_Span, Reaction_At_B)
    plt.plot([Length_Of_Span, 0], [0,0])
    plt.plot([0,0], [0,0])
    plt.ylabel("Reaction")
    plt.xlabel("Distance(m)")    
    

#Back_End(Length_Of_Span, Length_Of_Points)