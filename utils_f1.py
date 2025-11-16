import fastf1

fastf1.Cache.enable_cache("cache")

def get_last_race_results(year=2024):
    schedule = fastf1.get_event_schedule(year)
    last_event = schedule[schedule['EventFormat'] == 'race'].iloc[-1]

    session = fastf1.get_session(year, last_event['EventName'], "R")
    session.load()

    results = session.results[['DriverNumber', 'Abbreviation', 'Position', 'Time', 'Status']]
    return results.to_string()

def get_driver_lap_times(year, grand_prix, driver_code):
    session = fastf1.get_session(year, grand_prix, "R")
    session.load()

    laps = session.laps.pick_driver(driver_code)
    if laps.empty:
        return f"Nenhum dado encontrado para {driver_code} no GP {grand_prix}."

    summary = laps[['LapNumber', 'LapTime']].head(10)
    return summary.to_string()

def get_race_info(year, grand_prix):
    session = fastf1.get_session(year, grand_prix, "R")
    session.load()

    info = {
        "Circuito": session.event['Location'],
        "País": session.event['Country'],
        "Data": session.event['SessionStartTime'].strftime('%d/%m/%Y'),
    }
    return str(info)
