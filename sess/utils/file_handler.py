# file_handler.py

import json
import os

BASE = os.path.dirname(os.path.dirname(__file__))
EVENT_FILE = os.path.join(BASE, "data", "events.json")
ROOM_FILE = os.path.join(BASE, "data", "rooms.json")

def save_events(events):
    with open(EVENT_FILE, "w") as f:
        json.dump([e.__dict__ for e in events], f)

def load_events():
    try:
        from sess.models.event import Event
        with open(EVENT_FILE) as f:
            data = json.load(f)
            return [Event(**e) for e in data]
    except:
        return []

def save_rooms(rooms):
    data = []

    for r in rooms:
        data.append({
            "room_id": r.room_id,
            "capacity": r.capacity,
            "features": list(r.features)   # ✅ MUST BE list()
        })

    with open(ROOM_FILE, "w") as f:
        json.dump(data, f)

def load_rooms():
    try:
        from sess.models.room import Room
        with open(ROOM_FILE) as f:
            data = json.load(f)

            return [
                Room(
                    r["room_id"],
                    r["capacity"],
                    ",".join(r["features"])   # ✅ convert back to string
                )
                for r in data
            ]
    except:
        return []

BOOKING_FILE = os.path.join(BASE, "data", "bookings.json")

def save_bookings(bookings):
    data = []

    for b in bookings:
        data.append({
            "event_title": b.event.title,
            "room_id": b.room.room_id
        })

    with open(BOOKING_FILE, "w") as f:
        json.dump(data, f)


def load_bookings(events, rooms):
    bookings = []
    try:
        from sess.models.booking import Booking

        with open(BOOKING_FILE) as f:
            data = json.load(f)

        for b in data:
            event = next((e for e in events if e.title == b["event_title"]), None)
            room = next((r for r in rooms if r.room_id == b["room_id"]), None)

            if event and room:
                bookings.append(Booking(event, room))

    except:
        pass

    return bookings
