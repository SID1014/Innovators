from fastapi import FastAPI
import random
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from synthetic_data import generate_data

app = FastAPI()

# Enable CORS so React can talk to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

stations, trains = generate_data()

@app.get("/stations")
def get_stations():
    return {"stations": stations}

@app.get("/trains")
def get_trains():
    return {"trains": trains}

async def update_trains_periodically():
    while True:
        for train in trains:
            train["status"] = random.choice(["On Time", "Delayed", "Cancelled"])
            train["last_update"] = time.time()
        await asyncio.sleep(30)  # update every 30s

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(update_trains_periodically())