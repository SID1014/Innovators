import random
from datetime import datetime, timedelta

# Synthetic dataset (3 stations, 5 trains)
synthetic_trains = [
    # Copy the 5-train synthetic dataset from previous step here
     {
        "train_no": "12000",
        "train_name": "Shatabdi Express",
        "train_type": "Express",
        "priority": 1,
        "route": [
            {"station": "BPL", "sched_arrival": "07:00", "sched_departure": "07:10"},
            {"station": "CNB", "sched_arrival": "09:30", "sched_departure": "09:40"},
            {"station": "NDLS", "sched_arrival": "12:00", "sched_departure": "12:10"}
        ],
        "current_station": "BPL",
        "next_station": "CNB",
        "status": "Delayed",
        "delay_minutes": 10
    },
    {
        "train_no": "12001",
        "train_name": "Rajdhani Express",
        "train_type": "Express",
        "priority": 1,
        "route": [
            {"station": "NDLS", "sched_arrival": "06:30", "sched_departure": "06:40"},
            {"station": "BPL", "sched_arrival": "08:50", "sched_departure": "09:00"},
            {"station": "CNB", "sched_arrival": "11:10", "sched_departure": "11:20"}
        ],
        "current_station": "NDLS",
        "next_station": "BPL",
        "status": "On Time",
        "delay_minutes": 0
    },
    {
        "train_no": "12002",
        "train_name": "Garib Rath",
        "train_type": "Express",
        "priority": 2,
        "route": [
            {"station": "CNB", "sched_arrival": "06:15", "sched_departure": "06:25"},
            {"station": "NDLS", "sched_arrival": "08:40", "sched_departure": "08:50"},
            {"station": "BPL", "sched_arrival": "11:00", "sched_departure": "11:10"}
        ],
        "current_station": "CNB",
        "next_station": "NDLS",
        "status": "On Time",
        "delay_minutes": 0
    },
    {
        "train_no": "12003",
        "train_name": "Passenger 101",
        "train_type": "Passenger",
        "priority": 3,
        "route": [
            {"station": "NDLS", "sched_arrival": "07:10", "sched_departure": "07:20"},
            {"station": "CNB", "sched_arrival": "09:30", "sched_departure": "09:40"},
            {"station": "BPL", "sched_arrival": "12:00", "sched_departure": "12:10"}
        ],
        "current_station": "NDLS",
        "next_station": "CNB",
        "status": "Delayed",
        "delay_minutes": 5
    },
    {
        "train_no": "12004",
        "train_name": "Freight 501",
        "train_type": "Freight",
        "priority": 3,
        "route": [
            {"station": "BPL", "sched_arrival": "07:30", "sched_departure": "07:45"},
            {"station": "CNB", "sched_arrival": "10:00", "sched_departure": "10:15"},
            {"station": "NDLS", "sched_arrival": "12:30", "sched_departure": "12:45"}
        ],
        "current_station": "BPL",
        "next_station": "CNB",
        "status": "Delayed",
        "delay_minutes": 15
    }
]

def train_simulator():
    """Initialize simulator with trains"""
    return synthetic_trains

def str_to_time(s):
    return datetime.strptime(s, "%H:%M")

def update_train(train):
    """Simulate train movement per call"""
    route = train["route"]
    try:
        idx = next(i for i, stop in enumerate(route) if stop["station"] == train["current_station"])
    except StopIteration:
        idx = 0

    sched_dep = str_to_time(route[idx]["sched_departure"]) + timedelta(minutes=train["delay_minutes"])
    current_time = datetime.now().replace(second=0, microsecond=0)

    if current_time >= sched_dep and idx + 1 < len(route):
        next_stop = route[idx + 1]
        train["current_station"] = next_stop["station"]
        train["next_station"] = route[idx + 2]["station"] if idx + 2 < len(route) else None
        train["delay_minutes"] += random.choice([0, 0, 5, 10])
        train["status"] = "On Time" if train["delay_minutes"] == 0 else "Delayed"
    elif idx + 1 >= len(route):
        train["status"] = "Arrived"
        train["next_station"] = None
    else:
        train["status"] = "Departed" if current_time >= str_to_time(route[idx]["sched_departure"]) else "At Station"
