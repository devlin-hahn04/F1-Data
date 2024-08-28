import customtkinter
import requests
import tkinter as tk
from tkinter import font as tkFont
import NextRace
from DriverStandings import DriverStandingsMenu


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root= customtkinter.CTk()
root.geometry("800x400")

custom_font= customtkinter.CTkFont(family= "FormulaFont", size= 24, weight= "bold")



def ConstructorStandingsMenu():
    
    ConstructorsUrl= 'http://ergast.com/api/f1/current/constructorStandings.json'
    response= requests.get(ConstructorsUrl)

    for widget in frame.winfo_children():
        widget.destroy()

    Back= customtkinter.CTkButton(master= frame, text= "Back", command= BackButton)
    Back.grid(row=0, column=0, padx=10, sticky="w")

    TitleLabel= customtkinter.CTkLabel(master=frame, text= "WCC Standings", font=("FormulaFont.ttf", 24, "bold"))
    TitleLabel.grid(row=0, column=1, padx=10, sticky="e")

    standings_frame = customtkinter.CTkFrame(master=frame)
    standings_frame.grid(row=2, column=1, columnspan=2, sticky="nsew", padx=10, pady=10)


    frame.grid_rowconfigure(2, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    standings_frame.grid_rowconfigure(0, weight=1)
    standings_frame.grid_columnconfigure(0, weight=1)
    standings_frame.grid_columnconfigure(1, weight=1)

    if response.status_code == 200:
        data = response.json()

        # Extract driver standings
        standings_list = data['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']

        half_index = len(standings_list) // 2
        standings_list_1 = standings_list[:half_index]
        standings_list_2 = standings_list[half_index:]

        column_frame_1 = customtkinter.CTkFrame(master=standings_frame)
        column_frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        column_frame_2 = customtkinter.CTkFrame(master=standings_frame)
        column_frame_2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        standings_frame.grid_rowconfigure(0, weight=1)
        standings_frame.grid_columnconfigure(0, weight=1)
        standings_frame.grid_columnconfigure(1, weight=1)


        position = 1
        for constructor in standings_list_1:
            constructor_name = constructor['Constructor']['name']
            constructor_points = constructor['points']

            StandingsLabel = customtkinter.CTkLabel(master=column_frame_1, text=f"{position}. {constructor_name} - {constructor_points} points", font=("FormulaFont.ttf", 18, "bold"))
            StandingsLabel.grid(row=position, column=0, padx=5, pady= 10, sticky="w")
            position += 1

        # Display the second half of the standings in the second column
        for constructor in standings_list_2:
            constructor_name = constructor['Constructor']['name']
            constructor_points = constructor['points']

            StandingsLabel = customtkinter.CTkLabel(master=column_frame_2, text=f"{position}. {constructor_name} - {constructor_points} points", font=("FormulaFont.ttf", 18, "bold"))
            StandingsLabel.grid(row=position, column=0, padx=5, pady= 10, sticky="w")
            position += 1

def ShowDriverResults(DriverEntry):
    import requests
    import customtkinter

    raceList1= []
    raceList2= []


    print(DriverEntry.get())

    # Endpoint to get the race results for the driver
    driver_results_url = f'http://ergast.com/api/f1/current/drivers/{DriverEntry.get()}/results.json'
    response = requests.get(driver_results_url)

    if response.status_code == 200:
        data = response.json()
        races = data['MRData']['RaceTable']['Races']

        half_index = len(races) // 2
        raceList1 = races[:half_index]
        raceList2 = races[half_index:]

        column_frame_1 = customtkinter.CTkFrame(master=frame)
        column_frame_1.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        column_frame_2 = customtkinter.CTkFrame(master=frame)
        column_frame_2.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        frame.grid_rowconfigure(2, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        # Display the driver results
        row = 1
        for race in raceList1:
            race_name = race['raceName']
            race_result = race['Results'][0]
            position = race_result['position']

            result_text = f"{race_name}: {position}th"
            ResultsLabel = customtkinter.CTkLabel(master=column_frame_1, text=result_text, font=("FormulaFont.ttf", 8, "bold"))
            ResultsLabel.grid(row=row, column=0, pady=1, padx=10, sticky="w")
            row += 1

        row = 1
        for race in raceList2:
            race_name = race['raceName']
            race_result = race['Results'][0]
            position = race_result['position']

            result_text = f"{race_name}: {position}th"
            ResultsLabel = customtkinter.CTkLabel(master=column_frame_2, text=result_text, font=("FormulaFont.ttf", 8, "bold"))
            ResultsLabel.grid(row=row, column=0, pady=1, padx=10, sticky="w")
            row += 1
    


def DriverResultsMenu():

    # Clear previous widgets
    for widget in frame.winfo_children():
        widget.destroy()

    
    # Configure grid columns
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)
    frame.grid_columnconfigure(3, weight=1)
    frame.grid_columnconfigure(4, weight=1)
    
    Back = customtkinter.CTkButton(master=frame, text="Back", command=BackButton)
    Back.grid(row=0, column=0, padx=10, sticky="w")
    
    TitleLabel = customtkinter.CTkLabel(master=frame, text="Driver Results", font=("FormulaFont.ttf", 24, "bold"))
    TitleLabel.grid(row=0, column=1, columnspan=3, pady=20, sticky="n")
    
    DriverEntry = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Driver")
    DriverEntry.grid(row=1, column=1, padx=(10, 5), pady=5, sticky="e")
    
    SearchButton = customtkinter.CTkButton(master=frame, text="Search", command=lambda: ShowDriverResults(DriverEntry))
    SearchButton.grid(row=1, column=2, padx=(5, 10), pady=5, sticky="w")

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

    WCCButton = customtkinter.CTkButton(master=frame, text="Constructors Standings", command=ConstructorStandingsMenu)
    WCCButton.grid(row=1, column=1, padx=12, pady=12, sticky="e")

    DriverResultsButton= customtkinter.CTkButton(master= frame, text= "Driver Results", command= DriverResultsMenu)
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