# scheduler.py

from models.event import Event
from models.room import Room
from models.booking import Booking

class Scheduler:

    def __init__(self, events, rooms, bookings):
        self.events = events
        self.rooms = rooms
        self.bookings = bookings

    def check_conflict(self, new_event, room):
        for b in self.bookings:

            if new_event.date != b.event.date:
                continue

            if room.room_id == b.room.room_id:
                s1, e1 = new_event.get_times()
                s2, e2 = b.event.get_times()

                if (s1 < e2) and (e1 > s2):
                    return True
        return False

    def add_event(self):
        e = Event(
            input("Title: "),
            input("Date: "),
            input("Start Time: "),
            input("End Time: "),
            input("Department: "),
            input("Type: ")
        )
        self.events.append(e)
        print("Event added")

    def add_room(self):
        r = Room(
            input("Room ID: "),
            int(input("Capacity: ")),
            input("Features: ")
        )
        self.rooms.append(r)
        print("Room added")

    def create_booking(self):

        for i, e in enumerate(self.events):
            print(i+1, e.title)
        event = self.events[int(input("Select event: "))-1]

        for i, r in enumerate(self.rooms):
            print(i+1, r.room_id)
        room = self.rooms[int(input("Select room: "))-1]

        if self.check_conflict(event, room):
            print("❌ Conflict detected!")
            return

        self.bookings.append(Booking(event, room))
        print("✅ Booking successful")

    def view_bookings(self):
        for b in self.bookings:
            print(b.event.title, "->", b.room.room_id)

    def delete_event(self):
        for i, e in enumerate(self.events):
            print(i + 1, e.title)

        idx = int(input("Select event to delete: ")) - 1
        event = self.events.pop(idx)


        self.bookings = [b for b in self.bookings if b.event != event]

        print(" Event deleted")

    def update_event(self):
        for i, e in enumerate(self.events):
            print(i + 1, e.title)

        idx = int(input("Select event to update: ")) - 1
        e = self.events[idx]

        e.title = input(f"New title ({e.title}): ") or e.title
        e.date = input(f"New date ({e.date}): ") or e.date
        e.start_time = input(f"Start time ({e.start_time}): ") or e.start_time
        e.end_time = input(f"End time ({e.end_time}): ") or e.end_time
        e.department = input(f"Department ({e.department}): ") or e.department
        e.event_type = input(f"Type ({e.event_type}): ") or e.event_type

        print("✏ Event updated")

    def delete_room(self):
        for i, r in enumerate(self.rooms):
            print(i + 1, r.room_id)

        idx = int(input("Select room to delete: ")) - 1
        room = self.rooms.pop(idx)

        # Remove related bookings
        self.bookings = [b for b in self.bookings if b.room != room]

        print("🗑 Room deleted")

    def update_room(self):
        for i, r in enumerate(self.rooms):
            print(i + 1, r.room_id)

        idx = int(input("Select room to update: ")) - 1
        r = self.rooms[idx]

        r.room_id = input(f"Room ID ({r.room_id}): ") or r.room_id

        cap = input(f"Capacity ({r.capacity}): ")
        if cap:
            r.capacity = int(cap)

        features = input(f"Features ({','.join(r.features)}): ")
        if features:
            r.features = set(features.lower().split(","))

        print(" Room updated")

    def delete_booking(self):
        for i, b in enumerate(self.bookings):
            print(i + 1, b.event.title, "->", b.room.room_id)

        idx = int(input("Select booking to delete: ")) - 1
        self.bookings.pop(idx)

        print(" Booking deleted")

    def search_booking(self):
        keyword = input("Enter keyword (event/room): ").lower()

        found = False

        for b in self.bookings:
            if keyword in b.event.title.lower() or keyword in b.room.room_id.lower():
                print(b.event.title, "->", b.room.room_id)
                found = True

        if not found:
            print("No matching bookings found")