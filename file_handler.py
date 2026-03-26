import json
from event import Event
from room import Room


# Save Events to JSON
def save_events(events):
    data = []

    for e in events:
        data.append({
            "title": e.title,
            "date": e.date,
            "start_time": e.start_time,
            "end_time": e.end_time,
            "department": e.department,
            "event_type": e.event_type
        })

    try:
        with open("events.json", "w") as f:
            json.dump(data, f)
        print("Events saved successfully")

    except Exception as e:
        print("Error saving events:", e)


# Load Events from JSON
def load_events():
    events = []

    try:
        with open("events.json", "r") as f:
            data = json.load(f)

            for item in data:
                event = Event(
                    item["title"],
                    item["date"],
                    item["start_time"],
                    item["end_time"],
                    item["department"],
                    item["event_type"]
                )
                events.append(event)

    except FileNotFoundError:
        print("No event file found, starting fresh")

    except Exception as e:
        print("Error loading events:", e)

    return events


# Save Rooms
def save_rooms(rooms):
    data = []

    for r in rooms:
        data.append({
            "room_id": r.room_id,
            "capacity": r.capacity,
            "features": r.features
        })

    try:
        with open("rooms.json", "w") as f:
            json.dump(data, f)
        print("Rooms saved successfully")

    except Exception as e:
        print("Error saving rooms:", e)


# Load Rooms
def load_rooms():
    rooms = []

    try:
        with open("rooms.json", "r") as f:
            data = json.load(f)

            for item in data:
                room = Room(
                    item["room_id"],
                    item["capacity"],
                    item["features"]
                )
                rooms.append(room)

    except FileNotFoundError:
        print("No room file found, starting fresh")

    except Exception as e:
        print("Error loading rooms:", e)

    return rooms
