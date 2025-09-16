import random
import datetime

def generate_data():
    stations = ["Mumbai", "Delhi", "Nagpur"]
    trains = []

    for i in range(5):
        train_id = f"T{i+1:03}"
        origin, destination = random.sample(stations, 2)
        departure = datetime.datetime.now() + datetime.timedelta(minutes=30*i)
        arrival = departure + datetime.timedelta(hours=random.randint(4, 12))

        trains.append({
            "train_id": train_id,
            "name": f"Express {i+1}",
            "origin": origin,
            "destination": destination,
            "departure": departure.strftime("%Y-%m-%d %H:%M"),
            "arrival": arrival.strftime("%Y-%m-%d %H:%M"),
            "status": random.choice(["On Time", "Delayed", "Cancelled"])
        })

    return stations, trains
