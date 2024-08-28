import customtkinter
import requests

def DriverStandingsMenu(frame, BackButton):

    # Endpoint to get current driver standings
    DriversUrl = 'http://ergast.com/api/f1/current/driverStandings.json'

    # Make a request to the API
    response = requests.get(DriversUrl)

    for widget in frame.winfo_children():
        widget.destroy()

    Back= customtkinter.CTkButton(master= frame, text= "Back", command= BackButton)
    Back.grid(row=0, column=0, padx=10, sticky="w")

    TitleLabel= customtkinter.CTkLabel(master=frame, text= "WDC Standings", font=("FormulaFont.ttf", 24, "bold"))
    TitleLabel.grid(row=0, column=0, padx=10, sticky="e")

    standings_frame = customtkinter.CTkFrame(master=frame)
    standings_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    if response.status_code == 200:
        data = response.json()

        # Extract driver standings
        standings_list = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']

         # Split the standings list into two halves
        half_index = len(standings_list) // 2
        standings_list_1 = standings_list[:half_index]
        standings_list_2 = standings_list[half_index:]

        # Create frames for the two columns
        column_frame_1 = customtkinter.CTkFrame(master=standings_frame)
        column_frame_1.grid(row=0, column=0, padx=10, sticky="n")
        column_frame_2 = customtkinter.CTkFrame(master=standings_frame)
        column_frame_2.grid(row=0, column=1, padx=10, sticky="n")

        # Display the first half of the standings in the first column
        position = 1
        for driver in standings_list_1:
            driver_name = f"{driver['Driver']['givenName']} {driver['Driver']['familyName']}"
            driver_team = driver['Constructors'][0]['name']
            driver_points = driver['points']

            StandingsLabel = customtkinter.CTkLabel(master=column_frame_1, text=f"{position}. {driver_name} ({driver_team}) - {driver_points} points", font=("FormulaFont.ttf", 12, "bold"))
            StandingsLabel.grid(row=position, column=0, padx=10, sticky="w")
            position += 1

        # Display the second half of the standings in the second column
        for driver in standings_list_2:
            driver_name = f"{driver['Driver']['givenName']} {driver['Driver']['familyName']}"
            driver_team = driver['Constructors'][0]['name']
            driver_points = driver['points']

            StandingsLabel = customtkinter.CTkLabel(master=column_frame_2, text=f"{position}. {driver_name} ({driver_team}) - {driver_points} points", font=("FormulaFont.ttf", 12, "bold"))
            StandingsLabel.grid(row=position, column=0, padx=10, sticky="w")
            position += 1

