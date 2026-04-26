class Booking:

    def __init__(self, event, room):
        self.event = event
        self.room = room

    def display_booking(self):
        print(self.event.get_title(), "->", self.room.get_room_id())


# =========================
# validators.py
# =========================

class InvalidInputError(Exception):
    pass

class BookingConflictError(Exception):
    pass

def validate_time(start, end):
    if start >= end:
        raise InvalidInputError("Start time must be before end time")

def validate_capacity(capacity):
    if capacity <= 0:
        raise InvalidInputError("Capacity must be greater than 0")
