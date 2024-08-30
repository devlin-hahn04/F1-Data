import customtkinter
import requests
import tkinter as tk
from tkinter import font as tkFont
import NextRace
from DriverStandings import DriverStandingsMenu
from ConstructorStandings import ConstructorStandingsMenu
from DriverResults import DriverResultsMenu



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root= customtkinter.CTk()
root.geometry("800x400")

custom_font= customtkinter.CTkFont(family= "FormulaFont", size= 24, weight= "bold")

def BackButton():
    
    for widget in frame.winfo_children():
        widget.destroy()

    MainMenu()


#Main Menu after login button pressed
def MainMenu():

    # Clear previous widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Create and grid the welcome label
    WelcomeLabel = customtkinter.CTkLabel(master=frame, text=f"Welcome", font=("FormulaFont.ttf", 24, "bold"))
    WelcomeLabel.grid(row=0, column=0, columnspan=2, pady=12, padx=10)

    NextRaceInfo= NextRace.NextRace()
    NextRaceLabel= customtkinter.CTkLabel(master= frame, text=NextRaceInfo, font=("FormulaFont.ttf", 18))
    NextRaceLabel.grid(row=1, column=4, columnspan=2, pady=12, padx=10)

    #Vertcial Lines to separate buttons from next race info
    SeparatorFrame = customtkinter.CTkFrame(master=frame, width=2)
    SeparatorFrame.grid(row=0, column=2, rowspan=3, pady=12, sticky="ns")

    SeparatorFrame = customtkinter.CTkFrame(master=frame, width=2)
    SeparatorFrame.grid(row=1, column=2, rowspan=3, pady=12, sticky="ns")

    SeparatorFrame = customtkinter.CTkFrame(master=frame, width=2)
    SeparatorFrame.grid(row=2, column=2, rowspan=3, pady=12, sticky="ns")


    WDCButton = customtkinter.CTkButton(master=frame, text=f"Drivers Standings", command=lambda: DriverStandingsMenu(frame, BackButton))
    WDCButton.grid(row=1, column=0, padx=12, pady=12, sticky="w")

    WCCButton = customtkinter.CTkButton(master=frame, text="Constructors Standings", command=lambda: ConstructorStandingsMenu(frame, BackButton))
    WCCButton.grid(row=1, column=1, padx=12, pady=12, sticky="e")

    DriverResultsButton= customtkinter.CTkButton(master= frame, text= "Driver Results", command= lambda: DriverResultsMenu(frame, BackButton))
    DriverResultsButton.grid(row= 2, column= 0, padx=12, pady=12, sticky="w")

    



#Initial Screen

frame= customtkinter.CTkFrame(master= root)
frame.pack(pady= 20, padx= 60, fill= "both", expand= True)



label= customtkinter.CTkLabel(master= frame, text= "Formula 1 Data", font= custom_font)
label.pack(pady= 12, padx= 10)

entry1= customtkinter.CTkEntry(master= frame, placeholder_text= "Username")
entry1.pack(pady= 12, padx= 10)

entry2= customtkinter.CTkEntry(master= frame, placeholder_text= "Password", show= "*")
entry2.pack(pady= 12, padx= 10)

button= customtkinter.CTkButton(master= frame, text= "Login", command= MainMenu)
button.pack(pady= 12, padx= 10)

root.mainloop()