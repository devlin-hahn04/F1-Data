import customtkinter
import requests

def ShowDriverResults(DriverEntry, frame):
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
    


def DriverResultsMenu(frame, BackButton):

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
    
    SearchButton = customtkinter.CTkButton(master=frame, text="Search", command=lambda: ShowDriverResults(DriverEntry, frame))
    SearchButton.grid(row=1, column=2, padx=(5, 10), pady=5, sticky="w")