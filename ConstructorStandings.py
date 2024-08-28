import customtkinter
import requests

def ConstructorStandingsMenu(frame, BackButton):
    
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