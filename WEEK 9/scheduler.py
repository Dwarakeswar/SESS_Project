from models.event import Event
from models.room import Room
from models.booking import Booking

class Scheduler:

    def __init__(self, events, rooms, bookings):
        self.events = events
        self.rooms = rooms
        self.bookings = bookings

    def add_event(self):
        e = Event(
            input("Enter Title: "),
            input("Enter Date: "),
            input("Enter Start Time: "),
            input("Enter End Time: "),
            input("Enter Department: "),
            input("Enter Event Type: ")
        )

        if e.validate_event():
            self.events.append(e)
            print("Event added")

    def add_room(self):
        r = Room(
            input("Enter Room ID: "),
            int(input("Enter Capacity: ")),
            input("Enter Features: ")
        )

        if r.validate_room():
            self.rooms.append(r)
            print("Room added")

    def create_booking(self):
        if not self.events or not self.rooms:
            print("Add events and rooms first")
            return

        for i, e in enumerate(self.events):
            print(i, e.get_title())

        e_index = int(input("Select event: "))
        event = self.events[e_index]

        for i, r in enumerate(self.rooms):
            print(i, r.get_room_id())

        r_index = int(input("Select room: "))
        room = self.rooms[r_index]

        booking = Booking(event, room)
        self.bookings.append(booking)

        print("Booking created")

    def view_bookings(self):
        for b in self.bookings:
            b.display_booking()
