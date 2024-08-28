import requests


def NextRace():

    next_race_url = 'http://ergast.com/api/f1/current/next.json'
    response = requests.get(next_race_url)

    if response.status_code == 200:
        data = response.json()
        race_info = data['MRData']['RaceTable']['Races'][0]
        race_name = race_info['raceName']
        race_date = race_info['date']
        race_time = race_info['time']
        circuit_name = race_info['Circuit']['circuitName']
        location = race_info['Circuit']['Location']
        location_str = f"{location['locality']}, {location['country']}"

        return f"Upcoming Race: \n{race_name}\nDate: {race_date}\nCircuit: {circuit_name}\nLocation: {location_str}"
    else:
        return "Failed to fetch next race information"
