from sess.models.event import Event
from sess.models.room import Room
from sess.models.booking import Booking
from sess.utils.validators import (
    validate_time, validate_capacity,
    InvalidInputError, BookingConflictError
)

class Scheduler:

    def __init__(self, events, rooms, bookings):
        self.events = events
        self.rooms = rooms
        self.bookings = bookings

    def check_conflict(self, new_event, room):
        for b in self.bookings:
            if b.room.get_room_id() == room.get_room_id():
                s1, e1 = new_event.get_times()
                s2, e2 = b.event.get_times()

                if (s1 < e2) and (e1 > s2):
                    return True
        return False

    def add_event(self):
        try:
            e = Event(
                input("Enter Title: "),
                input("Enter Date: "),
                input("Enter Start Time: "),
                input("Enter End Time: "),
                input("Enter Department: "),
                input("Enter Event Type: ")
            )

            validate_time(e._start_time, e._end_time)

            if e.validate_event():
                self.events.append(e)
                print("Event added")

        except InvalidInputError as e:
            print("Error:", e)

        except Exception as e:
            print("Unexpected error:", e)

    def add_room(self):
        try:
            capacity = int(input("Enter Capacity: "))
            validate_capacity(capacity)

            r = Room(
                input("Enter Room ID: "),
                capacity,
                input("Enter Features: ")
            )

            if r.validate_room():
                self.rooms.append(r)
                print("Room added")

        except InvalidInputError as e:
            print("Error:", e)

        except ValueError:
            print("Capacity must be a number")

        except Exception as e:
            print("Unexpected error:", e)

    def create_booking(self):
        try:
            if not self.events or not self.rooms:
                print("Add events and rooms first")
                return

            for i, e in enumerate(self.events):
                print(i, e.get_title())

            event = self.events[int(input("Select event: "))]

            for i, r in enumerate(self.rooms):
                print(i, r.get_room_id())

            room = self.rooms[int(input("Select room: "))]

            if self.check_conflict(event, room):
                raise BookingConflictError("Booking conflict detected!")

            booking = Booking(event, room)
            self.bookings.append(booking)

            print("Booking created")

        except BookingConflictError as e:
            print("Error:", e)

        except ValueError:
            print("Invalid input")

        except IndexError:
            print("Invalid index selected")

        except Exception as e:
            print("Unexpected error:", e)

    def view_bookings(self):
        for b in self.bookings:
            b.display_booking()
