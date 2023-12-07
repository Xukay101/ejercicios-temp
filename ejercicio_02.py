'''
Por lo que entiendo en la consigna, el ejercicio es sin utilizar `pandas` 

El output que me dio de las tres estaciones mas 'calientes' fue:
* id: 130BAEcobici, name: 130 - RETIRO II, frequency: 12043
* id: 175BAEcobici, name: 147 - Constitución, frequency: 11830
* id: 14BAEcobici, name: 014 - Pacifico, frequency: 8087
'''
import csv

from typing import List
from datetime import datetime
from collections import Counter

DATASET_FILE_PATH = './trips_2022.csv'
MIN_HOUR = "06:00:00"
MAX_HOUR = "11:59:00"

def get_hot_routes(path: str, min_hour: str, max_hour: str, top: int = 3):
    '''
    Analyzes the routes dataset and returns the most 'hot' origin stations
    in the specified time range.

    :param path: Path to the dataset CSV file.
    :param min_hour: Minimum hour in format HH:MM:SS.
    :param max_hour: Maximum hour in format HH:MM:SS.
    :param top: Number of top stations to retrieve.
    '''

    # Convert hours to time type
    min_hour = datetime.strptime(min_hour, "%H:%M:%S").time()
    max_hour = datetime.strptime(max_hour, "%H:%M:%S").time()

    stations_counter = Counter()

    with open(path, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            hour_route = datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S").time()
            if min_hour <= hour_route <= max_hour:
                station_id = row[5]
                station_name = row[6]
                stations_counter[(station_id, station_name)] += 1

    return stations_counter.most_common(top)
    

if __name__ == '__main__':
    hot_routes = get_hot_routes(DATASET_FILE_PATH, MIN_HOUR, MAX_HOUR)
    
    print('Hottest stations:')
    for station, freq in hot_routes:
        print(f'* id: {station[0]}, name: {station[1]}, frequency: {freq}')
