import numpy as np
from typing import Dict, Tuple, Sequence, List, Any
import matplotlib.pyplot as plt
import folium
# from dictionaries import Dict 
def format_coords(coords: np.ndarray) -> str:
    """
    Formats numpy array of (lat, lon) coordinates into a concatenated string formatted
    for the OSRM server.
    """
    coords = ";".join([f"{lon:f},{lat:f}" for lat, lon in coords])
    return coords

def format_options(options: Dict[str, str]) -> str:
    """
    Formats dictionary of additional options to your OSRM request into a
    concatenated string format.
    """
    options = "&".join([f"{k}={v}" for k, v in options.items()])
    return options

class Connection:
    """Interface for connecting to and interacting with OSRM server.
    
    Default units from raw JSON response are in meters for distance and seconds for
    time. I will convert these to miles/hours respectively.
    """
    METERS_PER_MILE = 1609.344
    SEC_PER_HOUR = 3600
    def __init__(self, host: str, port: str):
        self.host = host
        self.port = port

def make_request(
        self,
        service: str,
        coords: np.ndarray,
        options: dict=None
    ) -> Dict[str, Any]:
    """
    Forwards your request to the OSRM server and returns a dictionary of the JSON
    response.
    """
    coords = format_coords(coords)
    options = format_options(options) if options else ""
    url = f"http://{self.host}:{self.port}/{service}/v1/car/{coords}?{options}"
    r = requests.get(url)
    return r.json()

def route_dt(self, coords: np.ndarray):
    """Returns the distance/time to travel a given route.
    """
    x = self.make_request(
        service='route',
        coords=coords,
        options={'steps': 'false', 'overview': 'false'}
    )
    x = x['routes'][0]
    return (x['distance']/self.METERS_PER_MILE, x['duration']/self.SEC_PER_HOUR)


def route_polyline(self, coords: np.ndarray, resolution: str='low'
    ) -> List[Tuple[float, float]]:
    """Returns polyline of route path as a list of (lat, lon) coordinates.
    """
    assert resolution in ('low', 'high')
    if resolution == 'low':
        options = {'overview': 'simplified'}
    elif resolution == 'high':
        options = {'overview': 'full'}
    x = self.make_request(service='route', coords=coords, options=options)
    return polyline.decode(x['routes'][0]['geometry'])

# id = ["A","A","A","A","A"]
# latitude = [35.237665, 35.274080, 35.286103, 35.290060, 35.326816]
# longtitude = [-81.343199, -81.520423, -81.540567, -81.53398, -81.758327]
# arrival_time = ["2019-11-11-11 12:53:22", "2019-11-11-11 13:28:46", "2019-11-11-11 13:45:13", "2019-11-11-11 13:56:34", "2019-11-11-11 14:18:30" ]
# departure_time = ["2019-11-11 13:10:00", "2019-11-11 13:31:06", "2019-11-11 13:50:48", "2019-11-11 13:59:23", "2019-11-11 14:22:12"]

import pandas as pd 
coordinates = 12.345,67.891;-23.456,78.912;34.567,89.123

raw_df = [ 
["A",  35.237665, -81.343199, "2019-11-11 12:53:22", "2019-11-11 13:10:00"], 
["A",  35.274080, -81.520423, "2019-11-11 13:28:46", "2019-11-11 13:31:06"],
["A",  35.286103, -81.540567, "2019-11-11 13:45:13", "2019-11-11 13:50:48"],
["A",  35.290060, -81.535398, "2019-11-11 13:56:34", "2019-11-11 13:59:23"],
["A",  35.326816, -81.758327, "2019-11-11 14:18:30", "2019-11-11 14:22:12"]
]

raw_df = pd.DataFrame(raw_df, columns = [  "route_id","latitude","longitude","arrival_time","departure_time"]) 

# raw_df = []
# raw_df['id'] = id
# raw_df['latitude'] = latitude
# raw_df['longtitude'] = longtitude
# raw_df['arrival_time'] = arrival_time
# raw_df['departure_time'] = departure_time

raw_df['arrival_time'] = pd.to_datetime(raw_df['arrival_time'])
raw_df['departure_time'] = pd.to_datetime(raw_df['departure_time'])
print(raw_df.head())

# Fill in null values
stops_df = raw_df.copy()
stops_df['arrival_time'].fillna(stops_df['departure_time'], inplace=True)
stops_df['departure_time'].fillna(stops_df['arrival_time'], inplace=True)

# Assign sequence numbers
df = list()
for route_id, group in stops_df.groupby('route_id'):
    group = group.sort_values(by='arrival_time')
    group['seq_num'] = list(range(len(group)))
    df.append(group)
stops_df = pd.concat(df, axis=0)

x = stops_df['arrival_time']
x = x.dt.hour + x.dt.minute/60 + x.dt.second/3600
plt.hist(x, bins=20)
plt.title("Distribution of stop arrival times")
locs, _ = plt.xticks()
plt.xticks(locs, [f"{int(h)}:00" for h in locs])
plt.xlabel('Time')
plt.ylabel('Count')
plt.show()

x = stops_df.groupby('route_id')['departure_time'].min()
x = x.dt.hour + x.dt.minute/60 + x.dt.second/3600
plt.hist(x, bins=20)
plt.title("Distribution of initial route departure times")
locs, _ = plt.xticks()
plt.xticks(locs, [f"{int(h)}:00" for h in locs])
plt.xlabel('Time')
plt.ylabel('Count')
plt.show()

x = stops_df['departure_time'] - stops_df['arrival_time']
x = x.dt.seconds/60
x = x[x != 0]   # Filter out "stops" at the distribution center
plt.hist(x, bins=100)
plt.title("Distribution of 'layover' times")
plt.xlabel('Time [minutes]')
plt.ylabel('Count')
plt.show()

m = folium.Map(location=stops_df[['latitude','longitude']].mean(), zoom_start=8)
for _, row in stops_df.iterrows():
    lat, lon = row['latitude'], row['longitude']
    folium.Marker(
        location=(lat, lon),
        popup=f"({lat:.4f}, {lon:.4f})"
    ).add_to(m)

print(m)

df = stops_df[stops_df['route_id'] == 'A'].copy()
df.sort_values(by='seq_num', inplace=True)
# Create map
m = folium.Map(location=df[['latitude','longitude']].mean(), zoom_start=9)
# Get polyline from OSRM
coords = df[['latitude','longitude']].values
route_polyline = conn.route_polyline(coords, resolution='high')
# Add polyline between stops
folium.PolyLine(
    locations=route_polyline,
    tooltip="Route A",
    color='#0fa6d9',
    opacity=0.75
).add_to(m)
# Create location markers for stops
for _, row in df.iterrows():
    lat, lon = row['latitude'], row['longitude']
    popup = folium.Popup(f"({lat:.4f}, {lon:.4f})", max_width=9999)
    folium.CircleMarker(
        location=(lat, lon),
        popup=popup,
        tooltip=row['seq_num'],
        radius=4,
        fill=True,
        fill_opacity=.25,
        color='#0fa6d9',
    ).add_to(m)

print(m)