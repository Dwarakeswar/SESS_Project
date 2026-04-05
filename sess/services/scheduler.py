# scheduler.py

from sess.models.event import Event
from sess.models.room import Room
from sess.models.booking import Booking

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