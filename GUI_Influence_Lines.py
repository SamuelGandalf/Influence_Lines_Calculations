# -*- coding: utf-8 -*-
"""
@author: SAMUEL GANDAANUO
"""
import tkinter as tk
from tkinter import Menu
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import Backend_Influence_Lines

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure




Window = tk.Tk()
Window.title("INFLUENCE LINES")
#Window.iconbitmap("Helmet.Ico")#this is to set an icon for the title of the programme
Window.resizable(False, False)
Window.geometry("1500x650+0+0")

My_Menu_Bar = Menu(Window) #this is to create the menu bar for the programme
Window.config(menu = My_Menu_Bar,background="grey")

#this is to add the individual menu items
File_Menu = Menu(My_Menu_Bar, tearoff=0)
My_Menu_Bar.add_cascade(label = "FILE", menu = File_Menu,)
#this is to add sub menu under the FILE menu
File_Menu.add_command(label = "New File",)
File_Menu.add_separator()
File_Menu.add_command(label = "Recent",)
File_Menu.add_command(label = "Open",)
File_Menu.add_command(label = "Open Last Closed",)
File_Menu.add_separator()
File_Menu.add_command(label = "Save",)
File_Menu.add_command(label = "Save As",)
File_Menu.add_command(label = "Save All",)
File_Menu.add_command(label = "Save Copy As",)
File_Menu.add_separator()

def ExitWindow():
    Window.quit()
    Window.destroy()
File_Menu.add_command(label = "Exit", command = ExitWindow)

View_Menu = Menu(My_Menu_Bar, tearoff=0)
My_Menu_Bar.add_cascade(label = "VIEW", menu = View_Menu)
View_Menu.add_command(label = "")

Structure_Menu = Menu(My_Menu_Bar, tearoff=0)
My_Menu_Bar.add_cascade(label = "STRUCTURE", menu = Structure_Menu)
Structure_Menu.add_command(label = "Members")
Structure_Menu.add_command(label = "Supports")

Analysis_Menu = Menu(My_Menu_Bar, tearoff=0)
My_Menu_Bar.add_cascade(label = "ANALYSIS", menu = Analysis_Menu)
#this is to add sub menu list to the ANALYSIS menu
Analysis_Menu.add_command(label = "Static Analysis")
Analysis_Menu.add_separator()
Analysis_Menu.add_command(label = "Modal Analysis")
Analysis_Menu.add_separator()
Analysis_Menu.add_command(label = "Dynamic Analysis")

Draw_Menu = Menu(My_Menu_Bar, tearoff=0)
My_Menu_Bar.add_cascade(label = "DRAW", menu = Draw_Menu)
#this is to add sub menu list to the DRAW  menu
Draw_Menu.add_command(label = "Structure")
Draw_Menu.add_command(label = "Load")
Draw_Menu.add_command(label = "Mass")
Draw_Menu.add_separator()
Draw_Menu.add_command(label = "Define Grid")
Draw_Menu.add_command(label = "Show Grid")
Draw_Menu.add_separator()
Draw_Menu.add_command(label = "Settings")

Help_Menu = Menu(My_Menu_Bar, tearoff=0)
My_Menu_Bar.add_cascade(label = "HELP", menu = Help_Menu)
#this is to add sub menu list to the HELP menu
Help_Menu.add_command(label = "About The Software")
Help_Menu.add_command(label = "Online Support")
Help_Menu.add_separator()
Help_Menu.add_command(label = "Report Bug")


Span_Entered= tk.IntVar()
Unit_Distance_Entered = tk.IntVar()
def Beam_Details():
    #this frame is to contain the beam details
    Details_Frame = ttk.LabelFrame(Window, text="Provide the Beam Details", height=10, width=50, labelanchor="n", relief= tk.GROOVE)
    Details_Frame.grid(row=0, column=0, padx=200, pady=200,)
    Details_Frame.grid_propagate(1)
    #Details_Frame.focus_force()
    
    
    Span_Label = ttk.Label(Details_Frame, text = "Enter Length Of Span: ",relief= tk.GROOVE, background="powder blue",font="bold")
    Span_Label.grid(row=1, column=0, padx=30, pady=30)
    Span_Entry = ttk.Entry(Details_Frame, textvariable=Span_Entered, foreground= "blue", validate="focusout",justify="center",width=12,font="bold")
    Span_Entry.focus()
    #Span_Entry.delete(first=None, last=None)
    Span_Entry.grid(row=1, column=1, padx=150, pady=30)
    
    Unit_Label = ttk.Label(Details_Frame, text = "Enter distance x of Unit Load from Left Suport: ", relief= tk.GROOVE,background="powder blue", font="bold")
    Unit_Label.grid(row=2, column=0, padx=30, pady=30, )
    Unit_Entry = ttk.Entry(Details_Frame, textvariable=Unit_Distance_Entered, foreground= "blue", validate="focusout", justify="center",width=12, font="bold",)
    Unit_Entry.grid(row=2, column=1, padx=150, pady=30)   
    #def Solve():
        #global Span_Value
        #global Unit_Distance_Value
        #Span_Value = Span_Entered.get()
        #Unit_Distance_Value = Unit_Distance_Entered.get()

        
    #this exception handling is used for the attribute error that occurs  
    try:                   
        Solve_Button = ttk.Button(Details_Frame, text="SOLVE", cursor="plus", default= "active", 
                                  command= lambda:Backend_Influence_Lines.Back_End(Span_Entered.get(), Unit_Distance_Entered.get()))
        Solve_Button.grid(row=5, column=4)
    except AttributeError:
        print("There is no such attribute!")   

    """
    f = Figure(figsize=(5,5), dpi = 100)
    a = f.add_subplot(111)
    try:
        a.plot(RealInfluenceLince.Back_End().Points_Along_Span, RealInfluenceLince.Back_End().Bending_Moment )
    except AttributeError:
        print("No such attribute exists")
        
    canvas= FigureCanvasTkAgg(f, Window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=1)
    
    Toolbar = NavigationToolbar2Tk(canvas, Window)
    Toolbar.update()
    canvas._tkcanvas.grid(row=2, column=1)
    """
        
Beam_Details()
Window.mainloop()

