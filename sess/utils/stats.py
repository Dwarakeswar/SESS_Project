# stats.py

import pandas as pd
import numpy as np

def generate_stats(bookings):

    data = []

    for b in bookings:
        start, end = b.event.get_times()
        duration = int(end.split(":")[0]) - int(start.split(":")[0])

        data.append({
            "room": b.room.room_id,
            "duration": duration,
            "department": b.event.department
        })

    df = pd.DataFrame(data)

    return {
        "Room Usage": df["room"].value_counts(),
        "Total Hours": np.sum(df["duration"]),
        "Department Usage": df["department"].value_counts()
    }