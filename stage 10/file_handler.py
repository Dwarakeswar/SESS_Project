import pandas as pd

def save_events(events):
    data = []
    for e in events:
        data.append({
            "title": e.get_title(),
            "date": e._date,
            "start": e._start_time,
            "end": e._end_time,
            "department": e._department,
            "type": e._event_type
        })

    df = pd.DataFrame(data)
    df.to_csv("sess/data/events.csv", index=False)


def load_events():
    events = []
    try:
        from sess.models.event import Event
        df = pd.read_csv("sess/data/events.csv")

        for _, row in df.iterrows():
            events.append(Event(
                row["title"],
                row["date"],
                row["start"],
                row["end"],
                row["department"],
                row["type"]
            ))
    except:
        print("No events file found")

    return events


def save_rooms(rooms):
    data = []
    for r in rooms:
        data.append({
            "room_id": r.get_room_id(),
            "capacity": r._capacity,
            "features": r._features
        })

    df = pd.DataFrame(data)
    df.to_csv("sess/data/rooms.csv", index=False)


def load_rooms():
    rooms = []
    try:
        from sess.models.room import Room
        df = pd.read_csv("sess/data/rooms.csv")

        for _, row in df.iterrows():
            rooms.append(Room(
                row["room_id"],
                int(row["capacity"]),
                row["features"]
            ))
    except:
        print("No rooms file found")

    return rooms

